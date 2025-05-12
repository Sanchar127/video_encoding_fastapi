<template>
  <DefaultLayout>
    <div class="min-h-screen flex items-center justify-center p-6 ">
      <div class="bg-white shadow-2xl rounded-3xl p-10 w-full max-w-4xl">
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
import DefaultLayout from '@/layout/DefaultLayout.vue'

const encodeProfileName = ref('')
const selectedProfile = ref('')
const users = ref([])

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

const fields = {
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

const inputTypes = {
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
  try {
    const payload = {
      name: encodeProfileName.value,
      profile_id: selectedProfile.value,
      ...form.value
    }

    const response = await axios.post('http://localhost:8084/encode-profile-details', payload, {
      headers: {
        'Content-Type': 'application/json'
      }
    })

    console.log('Profile details created:', response.data)
  } catch (error) {
    console.error('Failed to create profile details:', error)
  }
}

const fetchUsers = async () => {
  try {
    const response = await axios.get('http://localhost:8084/encodeprofile', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    users.value = response.data
  } catch (error) {
    console.error('Failed to fetch encode profiles:', error)
  }
}


onMounted(fetchUsers)
</script>
