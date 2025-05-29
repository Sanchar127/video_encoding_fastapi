<template>
  <DefaultLayout>
    <div class="max-w-7xl mx-auto my-8 px-4 sm:px-6 lg:px-8">
      <ProfileHeader 
        :profile-count="filteredProfiles.length"
        @refresh="refreshData"
        @add-profile="openAddModal"
      />
      
      <ProfileLoading v-if="loading" />
      
      <template v-else>
        <ProfileTable 
          v-if="paginatedProfiles.length > 0"
          :profiles="paginatedProfiles"
          @edit-profile="openEditModal"
        />
        <ProfileEmptyState v-else @reset="resetSearch" />
      </template>
      
      <PaginationControls
        v-if="!loading && filteredProfiles.length > 0"
        :pagination="pagination"
        :visible-pages="visiblePages"
        @page-change="goToPage"
      />
      
      <ProfileModal
        v-if="editModal"
        :is-edit-mode="isEditMode"
        :form-data="editForm"
        :users="users"
        @close="editModal = false"
        @submit="submitProfile"
      />
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import Cookies from 'js-cookie'
import { useRouter } from 'vue-router'


// Components
import ProfileHeader from '../../components/profile/ProfileHeader.vue'
import ProfileLoading from '../../components/profile/ProfileLoading.vue'
import ProfileTable from '../../components/profile/ProfilesTable.vue'
import ProfileEmptyState from '../../components/profile/ProfileEmptyState.vue'
import PaginationControls from '../../components/profile/PaginationControls.vue'
import ProfileModal from '../../components/profile/ProfileModal.vue'

const router = useRouter()
const toast = useToast()
const apiUrl = 'http://localhost:8084'

interface Profile {
  id: string
  name: string
  user?: {
    id?: string
    name?: string
    email?: string
    unique_id?: string
  }
}

interface User {
  id: string
  name: string
  email: string
  unique_id: string
}

// State
const profiles = ref<Profile[]>([])
const users = ref<User[]>([])
const loading = ref(true)
const searchQuery = ref('')
const itemsPerPage = 10

// Modal State
const editModal = ref(false)
const isEditMode = ref(false)
const selectedProfileId = ref<string | null>(null)
const editForm = ref({
  name: '',
  user_id: ''
})

// Pagination
const pagination = ref({
  currentPage: 1,
  totalPages: 1,
  start: 1,
  end: 1
})

const filteredProfiles = computed(() => {
  if (!searchQuery.value) return profiles.value

  const query = searchQuery.value.toLowerCase().trim()
  return profiles.value.filter(profile =>
    profile.name.toLowerCase().includes(query) ||
    (profile.user?.name && profile.user.name.toLowerCase().includes(query)) ||
    (profile.user?.email && profile.user.email.toLowerCase().includes(query)) ||
    profile.id.toLowerCase().includes(query)
  )
})


const paginatedProfiles = computed(() => {
  const start = (pagination.value.currentPage - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredProfiles.value.slice(start, end)
})

const visiblePages = computed(() => {
  const total = Math.ceil(filteredProfiles.value.length / itemsPerPage)
  const current = pagination.value.currentPage
  const range = 2
  
  let start = Math.max(1, current - range)
  let end = Math.min(total, current + range)

  if (current <= range + 1) {
    end = Math.min(2 * range + 1, total)
  }
  if (current >= total - range) {
    start = Math.max(1, total - 2 * range)
  }
  
  return Array.from({ length: end - start + 1 }, (_, i) => start + i)
})

// Methods
const getAuthHeaders = () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('Session expired. Please login again.')
    router.push('/login')
    throw new Error('No access token')
  }
  return {
    Authorization: `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  }
}

const handleApiError = (error: unknown, defaultMessage: string) => {
  const errorMsg = (error as any)?.response?.data?.detail || (error as Error)?.message
  toast.error(`${defaultMessage}: ${errorMsg}`)
  console.error(error)
  
  if ((error as any)?.response?.status === 401) {
    router.push('/login')
  }
}

const fetchProfiles = async () => {
  loading.value = true
  try {
    const headers = getAuthHeaders()
    const res = await axios.get(`${apiUrl}/encodeprofile`, { headers })
    profiles.value = Array.isArray(res.data) ? res.data : [res.data]
    updatePagination()
  } catch (error) {
    handleApiError(error, 'Failed to fetch profiles')
    profiles.value = []
  } finally {
    loading.value = false
  }
}

const fetchUsers = async () => {
  try {
    const headers = getAuthHeaders()
    const res = await axios.get(`${apiUrl}/users`, { headers })
    users.value = Array.isArray(res.data) ? res.data : [res.data]
  } catch (error) {
    handleApiError(error, 'Failed to fetch users')
  }
}

const refreshData = () => {
  fetchProfiles()
  fetchUsers()
  searchQuery.value = ''
  pagination.value.currentPage = 1
}

const resetSearch = () => {
  searchQuery.value = ''
  pagination.value.currentPage = 1
}

const updatePagination = () => {
  const totalItems = filteredProfiles.value.length
  const totalPages = Math.ceil(totalItems / itemsPerPage) || 1
  const currentPage = Math.min(pagination.value.currentPage, totalPages)
  const start = (currentPage - 1) * itemsPerPage + 1
  const end = Math.min(currentPage * itemsPerPage, totalItems)

  pagination.value = {
    currentPage,
    totalPages,
    start,
    end
  }
}

const goToPage = (page: number) => {
  if (page < 1 || page > pagination.value.totalPages) return
  pagination.value.currentPage = page
}

const openEditModal = (profile: Profile) => {
  isEditMode.value = true
  selectedProfileId.value = profile.id
  editForm.value = {
    name: profile.name,
    user_id: profile.user?.unique_id || ''
  }
  editModal.value = true
}

const openAddModal = () => {
  isEditMode.value = false
  selectedProfileId.value = null
  editForm.value = {
    name: '',
    user_id: ''
  }
  editModal.value = true
}

const submitProfile = async () => {
  if (isEditMode.value) {
    await updateProfile()
  } else {
    await createProfile()
  }
}

const createProfile = async () => {
  try {
    const headers = getAuthHeaders()
    await axios.post(
      `${apiUrl}/encode-profile`,
      {
        name: editForm.value.name,
        user_id: editForm.value.user_id || null,
      },
      { headers }
    )
    toast.success('Profile created successfully')
    editModal.value = false
    await fetchProfiles()
  } catch (error) {
    handleApiError(error, 'Failed to create profile')
  }
}

const updateProfile = async () => {
  if (!selectedProfileId.value) return

  try {
    const headers = getAuthHeaders()
    await axios.put(
      `${apiUrl}/encodeprofile/update`,
      {
        name: editForm.value.name,
        user_id: editForm.value.user_id || null,
      },
      {
        params: { id: selectedProfileId.value },
        headers
      }
    )

    toast.success('Profile updated successfully')
    editModal.value = false
    await fetchProfiles()
  } catch (error) {
    handleApiError(error, 'Update failed')
  }
}

// Lifecycle
onMounted(() => {
  refreshData()
})

watch(filteredProfiles, () => {
  updatePagination()
})
</script>