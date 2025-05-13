<template>
  <DefaultLayout>
    <div class="max-w-7xl mx-auto my-8 px-4 sm:px-6 lg:px-8">
      <!-- Header with stats and actions -->
      <div class="bg-white shadow rounded-xl p-6 mb-8 border border-gray-100">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6">
          <div class="flex items-center gap-4">
            <div class="p-3 bg-blue-100 rounded-lg">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">Encode Profiles</h1>
              <p class="text-gray-500">Manage all encoding profiles in the system</p>
            </div>
          </div>
          
          <div class="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
            <div class="relative flex-1">
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Search profiles..."
                class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
              <svg class="absolute left-3 top-2.5 h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <button
              @click="refreshData"
              class="flex items-center gap-2 px-4 py-2 bg-gray-100 border border-gray-300 rounded-lg hover:bg-gray-200 transition"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Refresh
            </button>
          </div>
        </div>
        
        <!-- Stats -->
        <div class="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="bg-blue-50 p-4 rounded-lg border border-blue-100">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-medium text-blue-800">Total Profiles</h3>
              <span class="text-2xl font-bold text-blue-600">{{ filteredProfiles.length }}</span>
            </div>
          </div>
          <div class="bg-green-50 p-4 rounded-lg border border-green-100">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-medium text-green-800">Active Users</h3>
              <span class="text-2xl font-bold text-green-600">{{ uniqueUsersCount }}</span>
            </div>
          </div>
          <div class="bg-purple-50 p-4 rounded-lg border border-purple-100">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-medium text-purple-800">Last Updated</h3>
              <span class="text-sm font-semibold text-purple-600">{{ lastUpdated }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="bg-white shadow rounded-xl p-6">
        <div class="animate-pulse space-y-6">
          <div v-for="i in 3" :key="i" class="flex items-center gap-4">
            <div class="w-16 h-16 bg-gray-200 rounded-full"></div>
            <div class="flex-1 space-y-3">
              <div class="h-4 bg-gray-200 rounded w-3/4"></div>
              <div class="h-4 bg-gray-200 rounded w-1/2"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Profiles Table -->
      <div v-else-if="filteredProfiles.length > 0" class="bg-white shadow rounded-xl overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Profile Name</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created</th>
                <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="profile in filteredProfiles" :key="profile.id" class="hover:bg-gray-50 transition">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10 bg-blue-100 rounded-full flex items-center justify-center">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
                      </svg>
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">{{ profile.name }}</div>
                      <div class="text-sm text-gray-500">ID: {{ profile.id }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ profile.user?.name || 'Unknown' }}</div>
                  <div class="text-sm text-gray-500">{{ profile.user?.email || 'No email' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(profile.created_at) || 'Unknown' }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <button
                    @click="openEditModal(profile)"
                    class="text-blue-600 hover:text-blue-900 mr-4 inline-flex items-center"
                  >
                    <EditIcon class="w-4 h-4 mr-1" />
                    Edit
                  </button>
                 
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <!-- Pagination -->
        <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6 rounded-b-xl">
          <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
            <div>
              <p class="text-sm text-gray-700">
                Showing
                <span class="font-medium">{{ pagination.start }}</span>
                to
                <span class="font-medium">{{ pagination.end }}</span>
                of
                <span class="font-medium">{{ filteredProfiles.length }}</span>
                results
              </p>
            </div>
            <div>
              <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                <button
                  @click="prevPage"
                  :disabled="pagination.currentPage === 1"
                  class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
                >
                  <span class="sr-only">Previous</span>
                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                </button>
                <button
                  v-for="page in visiblePages"
                  :key="page"
                  @click="goToPage(page)"
                  :class="[page === pagination.currentPage ? 'bg-blue-50 border-blue-500 text-blue-600' : 'bg-white border-gray-300 text-gray-500 hover:bg-gray-50', 'relative inline-flex items-center px-4 py-2 border text-sm font-medium']"
                >
                  {{ page }}
                </button>
                <button
                  @click="nextPage"
                  :disabled="pagination.currentPage === pagination.totalPages"
                  class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
                >
                  <span class="sr-only">Next</span>
                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                  </svg>
                </button>
              </nav>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="bg-white shadow rounded-xl p-10 text-center">
        <div class="text-gray-300 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-16 h-16 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
            <circle cx="9" cy="7" r="4"/>
            <path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
          </svg>
        </div>
        <h3 class="text-lg font-semibold text-gray-800 mb-2">No profiles found</h3>
        <p class="text-gray-500 mb-6">There are currently no encode profiles to display.</p>
        <button
          @click="refreshData"
          class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition flex items-center justify-center mx-auto gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh Data
        </button>
      </div>

      <!-- Edit Modal -->
      <div
        v-if="editModal"
        class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50 p-4"
      >
        <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-xl">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-gray-800">Edit Profile</h2>
            <button @click="editModal = false" class="text-gray-400 hover:text-gray-500">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Profile Name</label>
              <input
                v-model="editForm.name"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                type="text"
                placeholder="Enter profile name"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">User</label>
              <select
                v-model="editForm.user_id"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="" disabled>Select user</option>
                <option v-for="user in users" :key="user.id" :value="user.id">
                  {{ user.name }} ({{ user.email }})
                </option>
              </select>
            </div>
          </div>
          
          <div class="mt-6 flex justify-end gap-3">
            <button
              @click="editModal = false"
              class="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 transition"
            >
              Cancel
            </button>
            <button
              @click="updateProfile"
              class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition flex items-center gap-2"
            >
              <svg v-if="updating" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              {{ updating ? 'Saving...' : 'Save Changes' }}
            </button>
          </div>
        </div>
      </div>

    
          </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import EditIcon from '../../components/icons/EditIcon.vue'

const apiUrl = 'http://localhost:8084'
const profiles = ref<any[]>([])
const users = ref<any[]>([])
const loading = ref(true)
const toast = useToast()
const searchQuery = ref('')
const itemsPerPage = 10

// Modal States
const editModal = ref(false)

const updating = ref(false)

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
  
  const query = searchQuery.value.toLowerCase()
  return profiles.value.filter(profile => 
    profile.name.toLowerCase().includes(query) ||
    (profile.user?.name?.toLowerCase().includes(query) || false) ||
    (profile.user?.email?.toLowerCase().includes(query) || false) ||
    profile.id.toLowerCase().includes(query)
  )
})

const uniqueUsersCount = computed(() => {
  const userIds = new Set(profiles.value.map(p => p.user?.id).filter(Boolean))
  return userIds.size
})

const lastUpdated = computed(() => {
  if (profiles.value.length === 0) return 'Never'
  
  const dates = profiles.value
    .map(p => new Date(p.updated_at || p.created_at))
    .filter(d => !isNaN(d.getTime()))
    
  if (dates.length === 0) return 'Unknown'
  
  const latestDate = new Date(Math.max(...dates.map(d => d.getTime())))
  return latestDate.toLocaleDateString()
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
  
  const pages = []
  for (let i = start; i <= end; i++) {
    pages.push(i)
  }
  
  return pages
})


const formatDate = (dateString: string) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString()
}

const fetchProfiles = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${apiUrl}/encodeprofile`)
    profiles.value = Array.isArray(res.data) ? res.data : [res.data]
    updatePagination()
  } catch (error: any) {
    toast.error('Failed to fetch profiles: ' + (error.response?.data?.detail || error.message))
    profiles.value = []
  } finally {
    loading.value = false
  }
}

const fetchUsers = async () => {
  try {
    const res = await axios.get(`${apiUrl}/users`) 
    users.value = Array.isArray(res.data) ? res.data : [res.data]
  } catch (error) {
    console.error('Failed to fetch users', error)
  }
}

const refreshData = () => {
  fetchProfiles()
  fetchUsers()
}

const openEditModal = (profile: any) => {
  selectedProfileId.value = profile.id
  editForm.value = {
    name: profile.name,
    user_id: profile.user?.id || ''
  }
  editModal.value = true
}



const updateProfile = async () => {
  if (!selectedProfileId.value) return

  updating.value = true
  try {
    await axios.put(
      `${apiUrl}/encodeprofile/update`,
      {
        name: editForm.value.name,
        user_id: editForm.value.user_id,
      },
      {
        params: { id: selectedProfileId.value },
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )

    toast.success('Profile updated successfully')
    editModal.value = false
    await fetchProfiles()
  } catch (error: any) {
    toast.error('Update failed: ' + (error.response?.data?.detail || error.message))
  } finally {
    updating.value = false
  }
}



const updatePagination = () => {
  const totalItems = filteredProfiles.value.length
  pagination.value.totalPages = Math.ceil(totalItems / itemsPerPage)
  pagination.value.start = (pagination.value.currentPage - 1) * itemsPerPage + 1
  pagination.value.end = Math.min(pagination.value.currentPage * itemsPerPage, totalItems)
}

const goToPage = (page: number) => {
  if (page < 1 || page > pagination.value.totalPages) return
  pagination.value.currentPage = page
  updatePagination()
}

const nextPage = () => {
  if (pagination.value.currentPage < pagination.value.totalPages) {
    pagination.value.currentPage++
    updatePagination()
  }
}

const prevPage = () => {
  if (pagination.value.currentPage > 1) {
    pagination.value.currentPage--
    updatePagination()
  }
}


onMounted(() => {
  refreshData()
})
</script>