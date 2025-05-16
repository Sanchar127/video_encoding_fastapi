<template>
  <DefaultLayout>
    <div class="max-w-full mx-2 my-1 px-4 justify-start items-center">
      <!-- Header with stats and actions -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
        <div class="bg-gradient-to-r from-gray-200 to-gray-200 shadow-lg rounded-2xl p-4 border border-gray-100 flex-1">
          <h1 class="text-3xl font-bold text-gray-900">Manage Encode Profiles Details Page </h1>
          <p class="text-gray-600 mt-1" v-if="!loading">
            Total profiles: <span class="font-semibold">{{ profiles.length }}</span>
          </p>
        </div>
        
        <div class="flex gap-3">
          <button
            @click="refreshData"
            class="flex items-center gap-2 px-4 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition"
          >
           
            Refresh
          </button>
          <button
            @click="openAddModal"
            class="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500 transition"
          >
            <!-- <PlusIcon class="w-5 h-5" /> -->
            Add Profile
          </button>
        </div>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="space-y-6">
        <div v-for="i in 3" :key="i" class="bg-white rounded-2xl p-6 shadow animate-pulse flex items-center gap-4">
          <div class="w-12 h-12 bg-gray-200 rounded-full"></div>
          <div class="flex-1 space-y-2">
            <div class="h-4 bg-gray-200 rounded w-3/4"></div>
            <div class="h-4 bg-gray-200 rounded w-1/2"></div>
          </div>
        </div>
      </div>

      <!-- Profiles Table -->
      <div v-else-if="profiles.length > 0" class="bg-white shadow rounded-2xl overflow-hidden border border-gray-200">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Profile</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">width</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">height</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Video Bitrate</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Max Bitrate</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Audio Bitrate</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Audio Channel</th>
                 <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Audio Frequency</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Format</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Pix</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Level</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="profile in profiles" :key="profile.id" class="hover:bg-gray-50 transition">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="font-medium text-gray-900">{{ profile.profile }}</div>
              
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-gray-900">{{ profile.width }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-gray-900">{{ profile.height }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ profile.video_bitrate }}kbps</div>
                 
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                
                  <div class="text-sm text-gray-500">Max: {{ profile.max_bitrate || '-' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ profile.audio_bitrate }}kbps</div>
                
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
            
                  <div class="text-sm text-gray-500">{{ profile.audio_channel }}chHz</div>
                  
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                 
                  <div class="text-sm text-gray-500">{{ profile.audio_frequency }}Hz</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">
                   {{ profile.force_format }}<br>
                
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">
                    
        {{ profile.pix_fmt }}<br>
          
                  </div>
                </td><td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">
                
                     {{ profile.level }}
                  </div>
                </td>

                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <button
                    @click="openEditModal(profile)"
                    class="text-indigo-600 hover:text-indigo-900 mr-3 flex items-center gap-1"
                  >
                    <!-- <EditIcon class="w-4 h-4" /> -->
                    Edit
                  </button>
                  <button
                    @click="confirmDelete(profile)"
                    class="text-red-600 hover:text-red-900 flex items-center gap-1"
                  >
                    <!-- <TrashIcon class="w-4 h-4" /> -->
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="bg-white shadow rounded-2xl p-12 text-center border border-gray-200">
        <div class="text-gray-400 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-16 h-16 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
            <circle cx="9" cy="7" r="4"/>
            <path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-gray-800 mb-2">No profiles found</h3>
        <p class="text-gray-500 mb-6">There are currently no encode profiles available.</p>
        <button
          @click="openAddModal"
          class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500 transition flex items-center gap-2 mx-auto"
        >
          <PlusIcon class="w-5 h-5" />
          Add New Profile
        </button>
      </div>

      <!-- Edit Modal -->
      <div v-if="editModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-xl p-6 w-full max-w-2xl shadow-xl max-h-[90vh] overflow-y-auto">
          <h2 class="text-xl font-bold text-gray-900 mb-4">
            {{ isEditing ? 'Edit Profile' : 'Add New Profile' }}
          </h2>
          <form @submit.prevent="isEditing ? updateProfile() : createProfile()" class="grid grid-cols-2 gap-4">
            <div class="col-span-2">
              <label class="block mb-1 text-sm font-medium text-gray-700">Profile Name*</label>
              <input v-model="editForm.profile" type="text" required class="w-full px-3 py-2 border rounded-md" />
            </div>
            
            <div class="col-span-2 grid grid-cols-2 gap-4">
              <div>
                <label class="block mb-1 text-sm">Width*</label>
                <input v-model.number="editForm.width" type="number" required class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Height*</label>
                <input v-model.number="editForm.height" type="number" required class="w-full px-3 py-2 border rounded-md" />
              </div>
            </div>
            
            <div class="col-span-2 grid grid-cols-2 gap-4">
              <div>
                <label class="block mb-1 text-sm">Video Bitrate (kbps)*</label>
                <input v-model="editForm.video_bitrate" type="text" required class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Max Bitrate</label>
                <input v-model="editForm.max_bitrate" type="text" class="w-full px-3 py-2 border rounded-md" />
              </div>
            </div>
            
            <div class="col-span-2 grid grid-cols-3 gap-4">
              <div>
                <label class="block mb-1 text-sm">Audio Bitrate*</label>
                <input v-model="editForm.audio_bitrate" type="text" required class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Audio Channel*</label>
                <input v-model="editForm.audio_channel" type="text" required class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Frequency (Hz)*</label>
                <input v-model="editForm.audio_frequency" type="number" required class="w-full px-3 py-2 border rounded-md" />
              </div>
            </div>
            
            <div class="col-span-2 grid grid-cols-3 gap-4">
              <div>
                <label class="block mb-1 text-sm">SC Threshold</label>
                <input v-model="editForm.sc_threshold" type="text" class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Level</label>
                <input v-model="editForm.level" type="text" class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Bufsize</label>
                <input v-model="editForm.bufsize" type="text" class="w-full px-3 py-2 border rounded-md" />
              </div>
            </div>
            
            <div class="col-span-2 grid grid-cols-3 gap-4">
              <div>
                <label class="block mb-1 text-sm">Movflags</label>
                <input v-model="editForm.movflags" type="text" class="w-full px-3 py-2 border rounded-md" />
              </div>
              <div>
                <label class="block mb-1 text-sm">Pix Format*</label>
                <select v-model="editForm.pix_fmt" required class="w-full px-3 py-2 border rounded-md">
                  <option value="yuv420p">yuv420p</option>
                  <option value="yuv422p">yuv422p</option>
                  <option value="yuv444p">yuv444p</option>
                </select>
              </div>
              <div>
                <label class="block mb-1 text-sm">Force Format*</label>
                <select v-model="editForm.force_format" required class="w-full px-3 py-2 border rounded-md">
                  <option value="mp4">mp4</option>
                  <option value="mov">mov</option>
                  <option value="mkv">mkv</option>
                </select>
              </div>
            </div>
            
            <div class="col-span-2 grid grid-cols-2 gap-4">
              <div>
                <label class="block mb-1 text-sm">Video Codec*</label>
                <select v-model="editForm.vcodec" required class="w-full px-3 py-2 border rounded-md">
                  <option value="libx264">libx264</option>
                  <option value="libx265">libx265</option>
                  <option value="h264">h264</option>
                </select>
              </div>
              <div>
                <label class="block mb-1 text-sm">Audio Codec*</label>
                <select v-model="editForm.acodec" required class="w-full px-3 py-2 border rounded-md">
                  <option value="aac">aac</option>
                  <option value="mp3">mp3</option>
                  <option value="opus">opus</option>
                </select>
              </div>
            </div>

            <div class="col-span-2 flex justify-end gap-3 mt-4">
              <button type="button" @click="editModal = false" class="px-4 py-2 bg-gray-100 text-gray-800 rounded-md hover:bg-gray-200 transition">Cancel</button>
              <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500 transition">
                {{ isEditing ? 'Update' : 'Create' }} Profile
              </button>
            </div>
          </form>
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
// import PlusIcon from '../../components/icons/PlusIcon.vue'
// import TrashIcon from '../../components/icons/TrashIcon.vue'
// import RefreshIcon from '../../components/icons/RefreshIcon.vue'

const apiUrl = 'http://localhost:8084'
const profiles = ref<any[]>([])
const loading = ref(true)
const toast = useToast()

// Modal states
const editModal = ref(false)
const isEditing = ref(false)
const selectedProfileId = ref<string | null>(null)


// Form model
const editForm = ref({
  profile_id: 0,
  profile: '',
  width: 0,
  height: 0,
  video_bitrate: 0,
  max_bitrate: 0,
  audio_bitrate: 0,
  audio_channel: 0,
  audio_frequency: 0,
  sc_threshold: 0,
  level: 3.0,
  bufsize: 0,
  movflags: '',
  pix_fmt: 'yuv420p',
  force_format: 'mp4',
  acodec: 'aac',
  vcodec: 'libx264'
})

// Fetch profiles
const fetchProfiles = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${apiUrl}/encodeprofileDetails`)
    profiles.value = Array.isArray(res.data) ? res.data : [res.data]
  } catch (error: any) {
    toast.error('Failed to fetch profiles: ' + (error.response?.data?.detail || error.message))
    profiles.value = []
  } finally {
    loading.value = false
  }
}


const refreshData = () => fetchProfiles()

// Open modal for editing
const openEditModal = (profile: any) => {
  isEditing.value = true
  selectedProfileId.value = profile.id
  editForm.value = {
    profile_id: profile.profile_id,
    profile: profile.profile,
    width: profile.width,
    height: profile.height,
    video_bitrate: profile.video_bitrate,
    max_bitrate: profile.max_bitrate,
    audio_bitrate: profile.audio_bitrate,
    audio_channel: profile.audio_channel,
    audio_frequency: profile.audio_frequency,
    sc_threshold: profile.sc_threshold,
    level: profile.level,
    bufsize: profile.bufsize,
    movflags: profile.movflags,
    pix_fmt: profile.pix_fmt,
    force_format: profile.force_format,
    acodec: profile.acodec || 'aac',
    vcodec: profile.vcodec || 'libx264'
  }
  editModal.value = true
}



// Update existing profile
const updateProfile = async () => {
  if (!selectedProfileId.value) return

  try {
    await axios.put(
      `${apiUrl}/encodeprofileDetails/update`,
      { ...editForm.value },
      { params: { id: selectedProfileId.value } }
    )
    toast.success('Profile updated successfully')
    editModal.value = false
    await fetchProfiles()
  } catch (error: any) {
    toast.error('Update failed: ' + (error.response?.data?.detail || error.message))
  }
}



// Initialize
onMounted(fetchProfiles)
</script>