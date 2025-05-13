<template>
  <DefaultLayout>
    <div class="max-w-6xl mx-auto my-1 px-4 justify-start items-center">

      <div class="bg-gradient-to-r from-gray-200 to-gray-200 shadow-lg rounded-2xl p-2 mb-10 border border-gray-100 ">
        <h1 class="text-4xl font-bold text-gray-900 ">Encode Profiles Details</h1>
        
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

 
<div v-else-if="profiles.length > 0" class="overflow-x-auto">
  <table class="min-w-full text-sm text-left text-gray-300 border border-gray-600 rounded-xl overflow-hidden">
    <thead class="bg-gray-700 text-white">
      <tr>
        <th class="px-4 py-2">Details name</th>
        <th class="px-4 py-2">Profile</th>
        <th class="px-4 py-2">Width</th>
        <th class="px-4 py-2">Height</th>
        <th class="px-4 py-2">Bitrate</th>
        <th class="px-4 py-2">Max Bitrate</th>
        <th class="px-4 py-2">Audio Bitrate</th>
        <th class="px-4 py-2">Audio Channel</th>
        <th class="px-4 py-2">Frequency</th>
        <th class="px-4 py-2">SC Threshold</th>
        <th class="px-4 py-2">Level</th>
        <th class="px-4 py-2">Bufsize</th>
        <th class="px-4 py-2">Movflags</th>
        <th class="px-4 py-2">Pix Format</th>
        <th class="px-4 py-2">Force Format</th>
        <th class="px-4 py-2">Actions</th>
      </tr>
    </thead>
    <tbody class="bg-gray-800">
      <tr
        v-for="profile in profiles"
        :key="profile.id"
        class="border-t border-gray-600 hover:bg-gray-700 transition"
      >
        <td class="px-4 py-2 font-semibold">{{ profile.profile }}</td>
        <td class="px-4 py-2 font-semibold">{{ profile.profile_id }}</td>
        <td class="px-4 py-2">{{ profile.width }}</td>
        <td class="px-4 py-2">{{ profile.height }}</td>
        <td class="px-4 py-2">{{ profile.video_bitrate }} kbps</td>
        <td class="px-4 py-2">{{ profile.max_bitrate }}</td>
        <td class="px-4 py-2">{{ profile.audio_bitrate }}</td>
        <td class="px-4 py-2">{{ profile.audio_channel }}</td>
        <td class="px-4 py-2">{{ profile.audio_frequency }} Hz</td>
        <td class="px-4 py-2">{{ profile.sc_threshold }}</td>
        <td class="px-4 py-2">{{ profile.level }}</td>
        <td class="px-4 py-2">{{ profile.bufsize }}</td>
        <td class="px-4 py-2">{{ profile.movflags }}</td>
        <td class="px-4 py-2">{{ profile.pix_fmt }}</td>
        <td class="px-4 py-2">{{ profile.force_format }}</td>
        <td class="px-4 py-2">
          <button
            @click="openEditModal(profile)"
            class="text-sm flex items-center gap-1 px-2 py-1 bg-white text-gray-800 rounded hover:bg-gray-200 transition"
          >
            <EditIcon class="w-4 h-4" />
            Edit
          </button>
        </td>
      </tr>
    </tbody>
  </table>
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
        <p class="text-gray-500 mb-6">There are currently no encode profiles available. Try refreshing or adding a new one.</p>
        <button
          @click="refreshData"
          class="px-6 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition"
        >
          Refresh
        </button>
      </div>

     <!-- Edit Modal -->
<div v-if="editModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
  <div class="bg-white rounded-xl p-6 w-full max-w-2xl shadow-xl max-h-[90vh] overflow-y-auto">
    <h2 class="text-xl font-bold text-gray-900 mb-4">Edit Profile</h2>
    <form @submit.prevent="updateProfile" class="grid grid-cols-2 gap-4">
      <div class="col-span-2">
        <label class="block mb-1 text-sm font-medium text-gray-700">Profile Name</label>
        <input v-model="editForm.profile" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Width</label>
        <input v-model.number="editForm.width" type="number" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Height</label>
        <input v-model.number="editForm.height" type="number" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Video Bitrate (kbps)</label>
        <input v-model="editForm.video_bitrate" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Max Bitrate</label>
        <input v-model="editForm.max_bitrate" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Audio Bitrate</label>
        <input v-model="editForm.audio_bitrate" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Audio Channel</label>
        <input v-model="editForm.audio_channel" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Frequency (Hz)</label>
        <input v-model="editForm.audio_frequency" type="number" class="w-full px-3 py-2 border rounded-md" />
      </div>
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
      <div>
        <label class="block mb-1 text-sm">Movflags</label>
        <input v-model="editForm.movflags" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Pix Format</label>
        <input v-model="editForm.pix_fmt" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div>
        <label class="block mb-1 text-sm">Force Format</label>
        <input v-model="editForm.force_format" type="text" class="w-full px-3 py-2 border rounded-md" />
      </div>
      <div class="col-span-2 flex justify-end gap-3 mt-4">
        <button type="button" @click="editModal = false" class="px-4 py-2 bg-gray-100 text-gray-800 rounded-md hover:bg-gray-200 transition">Cancel</button>
        <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500 transition">Save</button>
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

const apiUrl = 'http://localhost:8084'
const profiles = ref<any[]>([])
const loading = ref(true)
const toast = useToast()


const editModal = ref(false)
const selectedProfileId = ref<string | null>(null)
const editForm = ref({
  profile_id: 0,
  profile: '',
  width: 0,
  height: 0,
  video_bitrate: 0,
  max_bitrate: 0,
  audio_bitrate: 0,
  audio_channel: 0,
  audio_frequency: '', // as string per schema
  sc_threshold: 0,
  level: 3.0,
  bufsize: 0,
  movflags: '',
  pix_fmt: 'yuv420p',
  force_format: 'mp4',
  acodec: 'aac',
  vcodec: 'libx264'
})



const fetchProfiles = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${apiUrl}/encodeprofileDetails`)
    console.log(res)
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


onMounted(fetchProfiles)
</script>




t
