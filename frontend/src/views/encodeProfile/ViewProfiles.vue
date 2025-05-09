<template>
  <DefaultLayout>
    <div class="max-w-6xl mx-auto my-12 px-4">
      <!-- Header -->
      <div class="bg-gray-700 shadow-sm rounded-xl p-6 mb-8 border border-gray-100">
        <h1 class="text-3xl font-semibold text-white mb-2">Encode Profiles</h1>
   
      </div>

      <!-- Loading -->
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

      <!-- Profiles -->
      <div v-else-if="profiles.length > 0" class="space-y-4">
        <div
          v-for="profile in profiles"
          :key="profile.id"
          class="bg-gray-500 rounded-xl shadow-sm border border-gray-100 px-2 py-2 flex items-center justify-between hover:shadow-md transition"
        >
          <div class="flex items-center gap-5">
            <div class="w-14 h-14 bg-gray-100 rounded-full flex items-center justify-center text-gray-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M19 21v-2a4 4 0 00-4-4H9a4 4 0 00-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-white">Profile Name  :  {{ profile.name }}</h3>
              
              <p class="text-sm text-white mt-0.5">User Name : {{ profile.user?.name ?? 'Unknown' }}</p>
            </div>
          </div>

          <button
            @click="openEditModal(profile)"
            class="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 transition"
          >
            <EditIcon class="w-4 h-4" />
            Edit
          </button>
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
          class="px-6 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition"
        >
          Refresh
        </button>
      </div>

      <!-- Edit Modal -->
      <div
        v-if="editModal"
        class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50"
      >
        <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-xl">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Edit Profile</h2>
          <label class="block mb-2 text-sm font-medium text-gray-700">Profile Name</label>
          <input
            v-model="editForm.name"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            type="text"
          />
          <div class="mt-6 flex justify-end gap-2">
            <button @click="editModal = false" class="px-4 py-2 bg-gray-100 rounded-md hover:bg-gray-200">Cancel</button>
            <button @click="updateProfile" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500">Save</button>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import EditIcon from '../../components/icons/EditIcon.vue'

const apiUrl = 'http://localhost:8084'
const profiles = ref<any[]>([])
const loading = ref(true)
const toast = useToast()

// Modal State
const editModal = ref(false)
const selectedProfileId = ref<string | null>(null)
const editForm = ref({ name: '', user_id: '' })

const fetchProfiles = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${apiUrl}/encodeprofile`)
    profiles.value = Array.isArray(res.data) ? res.data : [res.data]
  } catch (error: any) {
    toast.error('Failed to fetch profiles: ' + (error.response?.data?.detail || error.message))
    profiles.value = []
  } finally {
    loading.value = false
  }
}

const refreshData = () => fetchProfiles()

const openEditModal = (profile: any) => {
  selectedProfileId.value = profile.id
  editForm.value.name = profile.name
  editForm.value.user_id = profile.user?.unique_id || ''
  editModal.value = true
}

const updateProfile = async () => {
  if (!selectedProfileId.value) return

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
  }
}

onMounted(fetchProfiles)
</script>
