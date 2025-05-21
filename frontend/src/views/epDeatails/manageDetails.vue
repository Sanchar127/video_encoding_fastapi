<template>
  <DefaultLayout>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
     
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Encode Profiles Details</h1>
          
        </div>
        
        <div class="mt-4 md:mt-0 flex space-x-3">
          <button
            @click="refreshData"
            class="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            <RefreshIcon class="-ml-1 mr-2 h-5 w-5 text-gray-500" />
            Refresh
          </button>
          
          <router-link to="/new/EncodeProfileDetails">
            <button
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              <PlusIcon class="-ml-1 mr-2 h-5 w-5" />
              Add Profile
            </button>
          </router-link>
        </div>
      </div>

      <ProfileMetrics
        :total-profiles="profiles.length"
        :active-profiles="activeProfilesCount"
        :hd-profiles="hdProfilesCount"
        :recent-activity="recentActivityCount"
      />

      <div class="bg-white shadow rounded-lg overflow-hidden">
    
        <div class="px-4 py-5 sm:px-6 border-b border-gray-200">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between">
            <div class="w-full md:w-1/2 mb-4 md:mb-0">
              <label for="search" class="sr-only">Search</label>
              <div class="relative rounded-md shadow-sm">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <SearchIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                </div>
                <input
                  v-model="searchQuery"
                  type="text"
                  name="search"
                  id="search"
                  class="focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 sm:text-sm border-gray-300 rounded-md py-2"
                  placeholder="Search profiles..."
                />
              </div>
            </div>
            
            <div class="flex items-center space-x-3">
              <div>
                <label for="filter" class="sr-only">Filter</label>
                <select
                  id="filter"
                  name="filter"
                  class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md"
                >
                  <option selected>All Formats</option>
                  <option>MP4</option>
                 
                </select>
              </div>
              
              <button
                type="button"
                class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                <FilterIcon class="-ml-0.5 mr-2 h-4 w-4" />
                Filter
              </button>
            </div>
          </div>
        </div>

        <div v-if="loading" class="p-8">
          <div class="space-y-6">
            <div v-for="i in 3" :key="i" class="animate-pulse flex items-center space-x-4">
              <div class="rounded-full bg-gray-200 h-12 w-12"></div>
              <div class="flex-1 space-y-4 py-1">
                <div class="h-4 bg-gray-200 rounded w-3/4"></div>
                <div class="space-y-2">
                  <div class="h-4 bg-gray-200 rounded"></div>
                  <div class="h-4 bg-gray-200 rounded w-5/6"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

   
        <div v-else-if="profiles.length === 0" class="text-center py-12">
          <svg
            class="mx-auto h-12 w-12 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            ></path>
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">No profiles</h3>
          <p class="mt-1 text-sm text-gray-500">Get started by creating a new encode profile.</p>
          <div class="mt-6">
            <router-link to="/new/EncodeProfileDetails">
              <button
                type="button"
                class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                <PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                New Profile
              </button>
            </router-link>
          </div>
        </div>

      
        <ProfileTable
          v-else
          :profiles="filteredProfiles"
          :loading="loading"
          @edit="openEditModal"
          @delete="confirmDeleteProfile"
        />

  
        <ProfileFormModal
          :open="editModalOpen"
          :is-editing="isEditing"
          :profile-data="selectedProfile"
          @submit="handleFormSubmit"
          @close="closeEditModal"
        />
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import axios from 'axios'
import Cookies from 'js-cookie'
import { useRouter } from 'vue-router'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import ProfileMetrics from '../../components/Details/ProfileMetrics.vue'
import ProfileTable from '../../components/Details/ProfileTable.vue'
import ProfileFormModal from '../../components/Details/ProfileFormModal.vue'
import { PlusIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const toast = useToast()
const apiUrl = 'http://localhost:8084'

// State
interface ProfileDetails {
  id: string
  profile: string
  force_format: string
  width?: number
  height?: number
  is_active: boolean
  [key: string]: any // For additional properties
}

const profiles = ref<ProfileDetails[]>([])
const loading = ref(true)
const searchQuery = ref('')

// Modal State
const editModalOpen = ref(false)
const isEditing = ref(false)
const selectedProfile = ref<ProfileDetails | null>(null)

// Computed properties
const filteredProfiles = computed(() => {
  if (!searchQuery.value) return profiles.value
  
  const query = searchQuery.value.toLowerCase()
  return profiles.value.filter(profile => 
    profile.profile.toLowerCase().includes(query) ||
    profile.force_format.toLowerCase().includes(query)
  )
})

const activeProfilesCount = computed(() => 
  profiles.value.filter(p => p.is_active).length
)

const hdProfilesCount = computed(() => 
  profiles.value.filter(p => (p.width || 0) >= 1280).length
)

const recentActivityCount = computed(() => 
  Math.min(5, profiles.value.length)
)

// Helper functions
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

// API functions
const fetchProfiles = async () => {
  loading.value = true
  try {
    const headers = getAuthHeaders()
    const response = await axios.get(`${apiUrl}/encodeprofileDetails`, { headers })
    profiles.value = Array.isArray(response.data) ? response.data : [response.data]
  } catch (error) {
    handleApiError(error, 'Failed to fetch profiles')
    profiles.value = []
  } finally {
    loading.value = false
  }
}

const refreshData = () => fetchProfiles()

// Profile management
const openEditModal = (profile?: ProfileDetails) => {
  isEditing.value = !!profile
  selectedProfile.value = profile ? { ...profile } : null
  editModalOpen.value = true
}

const closeEditModal = () => {
  editModalOpen.value = false
  selectedProfile.value = null
}

const handleFormSubmit = async (formData: ProfileDetails) => {
  try {
    const headers = getAuthHeaders()
    
    if (isEditing.value && selectedProfile.value?.id) {
      await axios.put(
        `${apiUrl}/encodeprofileDetails/update`,
        formData,
        { 
          params: { id: selectedProfile.value.id },
          headers
        }
      )
      toast.success('Profile updated successfully')
    } else {
      await axios.post(
        `${apiUrl}/encodeprofileDetails/create`, 
        formData,
        { headers }
      )
      toast.success('Profile created successfully')
    }
    
    closeEditModal()
    await fetchProfiles()
  } catch (error) {
    handleApiError(error, 'Operation failed')
  }
}

const confirmDeleteProfile = async (id: string) => {
  try {
    const headers = getAuthHeaders()
    await axios.delete(
      `${apiUrl}/encodeprofileDetails/delete`,
      { 
        params: { id },
        headers 
      }
    )
    toast.success('Profile deleted successfully')
    await fetchProfiles()
  } catch (error) {
    handleApiError(error, 'Failed to delete profile')
  }
}

// Lifecycle hooks
onMounted(() => {
  fetchProfiles()
})
</script>
