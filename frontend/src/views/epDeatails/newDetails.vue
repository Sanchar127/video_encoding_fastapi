<template>
  <DefaultLayout>
    <div class="min-h-screen flex items-center justify-center p-20 ">
      <div class="bg-white shadow-2xl rounded-3xl p-10 w-full max-w-6xl">
        <h2 class="text-3xl font-bold mb-10 text-center text-gray-800">
          Create Encode Profile Details
        </h2>

        <form @submit.prevent="handleSubmit" class="grid grid-cols-1 md:grid-cols-2 gap-8">
     
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">
              Encode Profile Name
            </label>
            <input
              type="text"
              v-model="encodeProfileName"
              class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-100"
              placeholder="e.g., 720p_H264"
              required
            />
          </div>

       
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">
              Select Profile
            </label>
            <select
              v-model="selectedProfile"
              class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-400"
              required
            >
              <option disabled value="">Select a Profile</option>
              <option v-for="user in users" :key="user.id" :value="user.id">
                {{ user.name }}
              </option>
            </select>
          </div>

          <!-- Dynamic Fields -->
          <div
            v-for="(label, key) in fields"
            :key="key"
            class="flex flex-col md:col-span-1"
          >
            <label class="block text-sm font-semibold text-gray-700 mb-2 capitalize">
              {{ label }}
            </label>
            <input
              v-model="form[key]"
              :type="inputTypes[key] || 'text'"
              :step="key === 'level' ? 0.1 : undefined"
              class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200"
            />
          </div>

          <!-- Submit Button -->
          <div class="md:col-span-2">
            <button
              type="submit"
              class="w-full bg-gray-600 text-white font-semibold py-3 rounded-xl hover:bg-gray-300 transition duration-200 shadow-md"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </DefaultLayout>
</template>


<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import Cookies from 'js-cookie'
import DefaultLayout from '@/layout/DefaultLayout.vue'

const apiUrl = 'http://localhost:8084'

const encodeProfileName = ref('')
const selectedProfile = ref('')
const users = ref<any[]>([])
const toast = useToast()

const form = ref({
  width: '',
  height: '',
  video_bitrate: '',
  audio_bitrate: '',
  audio_channel: 2,
  audio_frequency: '44100',
  sc_threshold: 0,
  profile: 'high',
  level: '',
  max_bitrate: '',
  bufsize: '',
  movflags: 'faststart',
  pix_fmt: 'yuv420p',
  acodec: 'aac',
  vcodec: 'libx264',
  force_format: 'mp4'
})

const fields: Record<string, string> = {
  width: 'Width',
  height: 'Height',
  video_bitrate: 'Video Bitrate',
  audio_bitrate: 'Audio Bitrate',
  audio_channel: 'Audio Channel',
  audio_frequency: 'Audio Frequency',
  sc_threshold: 'Scene Change Threshold',
  profile: 'Profile',
  level: 'Level',
  max_bitrate: 'Max Bitrate',
  bufsize: 'Buffer Size',
  movflags: 'Move Flags',
  pix_fmt: 'Pixel Format',
  acodec: 'Audio Codec',
  vcodec: 'Video Codec',
  force_format: 'Force Format'
}

const inputTypes: Record<string, string> = {
  width: 'number',
  height: 'number',
  video_bitrate: 'number',
  audio_bitrate: 'number',
  audio_channel: 'number',
  sc_threshold: 'number',
  level: 'number',
  max_bitrate: 'number',
  bufsize: 'number'
}

const handleSubmit = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }

  try {
    const payload = {
      name: encodeProfileName.value,
      profile_id: selectedProfile.value,
      ...form.value
    }

    const response = await axios.post(`${apiUrl}/encode-profile-details`, payload, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })

    toast.success('Profile Details successfully created!')
    console.log('Profile details created:', response.data)
  } catch (error: any) {
    console.error('Failed to create profile details:', error)
    toast.error('Failed to create profile details: ' + (error.response?.data?.detail || error.message))
  }
}

const fetchUsers = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }

  try {
    const response = await axios.get(`${apiUrl}/encodeprofile`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })
    users.value = response.data
  } catch (error: any) {
    console.error('Failed to fetch encode profiles:', error)
    toast.error('Failed to fetch encode profiles: ' + (error.response?.data?.detail || error.message))
  }
}

onMounted(fetchUsers)
</script>
