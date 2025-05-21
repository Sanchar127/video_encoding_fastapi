<template>
  <div v-if="open" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <!-- Background overlay -->
      <div class="fixed inset-0 transition-opacity" aria-hidden="true">
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>

      <!-- Modal panel -->
      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
              <h3 class="text-lg leading-6 font-medium text-gray-900 mb-6">
                {{ isEditing ? 'Edit Profile' : 'Create New Profile' }}
              </h3>
              
              <form @submit.prevent="submitForm" class="space-y-6">
                <!-- Profile Info Section -->
                <div class="border-b border-gray-200 pb-6">
                  <h4 class="text-md font-medium text-gray-900 mb-4">Profile Information</h4>
                  <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-4">
                      <label for="profile-name" class="block text-sm font-medium text-gray-700">Profile Name</label>
                      <input type="text" v-model="form.profile" id="profile-name" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="width" class="block text-sm font-medium text-gray-700">Width</label>
                      <input type="number" v-model.number="form.width" id="width" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="height" class="block text-sm font-medium text-gray-700">Height</label>
                      <input type="number" v-model.number="form.height" id="height" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                  </div>
                </div>
                
                <!-- Video Settings Section -->
                <div class="border-b border-gray-200 pb-6">
                  <h4 class="text-md font-medium text-gray-900 mb-4">Video Settings</h4>
                  <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="video-bitrate" class="block text-sm font-medium text-gray-700">Video Bitrate (kbps)</label>
                      <input type="text" v-model="form.video_bitrate" id="video-bitrate" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="max-bitrate" class="block text-sm font-medium text-gray-700">Max Bitrate</label>
                      <input type="text" v-model="form.max_bitrate" id="max-bitrate"
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="vcodec" class="block text-sm font-medium text-gray-700">Video Codec</label>
                      <select v-model="form.vcodec" id="vcodec" required
                              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md">
                        <option value="libx264">libx264</option>
                       
                      </select>
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="pix-fmt" class="block text-sm font-medium text-gray-700">Pixel Format</label>
                      <select v-model="form.pix_fmt" id="pix-fmt" required
                              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md">
                        <option value="yuv420p">yuv420p</option>
                        
                      </select>
                    </div>
                  </div>
                </div>
                
                <!-- Audio Settings Section -->
                <div class="border-b border-gray-200 pb-6">
                  <h4 class="text-md font-medium text-gray-900 mb-4">Audio Settings</h4>
                  <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="audio-bitrate" class="block text-sm font-medium text-gray-700">Audio Bitrate (kbps)</label>
                      <input type="text" v-model="form.audio_bitrate" id="audio-bitrate" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="audio-channel" class="block text-sm font-medium text-gray-700">Audio Channels</label>
                      <input type="text" v-model="form.audio_channel" id="audio-channel" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="audio-frequency" class="block text-sm font-medium text-gray-700">Frequency (Hz)</label>
                      <input type="number" v-model.number="form.audio_frequency" id="audio-frequency" required
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="acodec" class="block text-sm font-medium text-gray-700">Audio Codec</label>
                      <select v-model="form.acodec" id="acodec" required
                              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md">
                        <option value="aac">AAC</option>
                        <
                      </select>
                    </div>
                  </div>
                </div>
                
                <!-- Container Settings Section -->
                <div>
                  <h4 class="text-md font-medium text-gray-900 mb-4">Container Settings</h4>
                  <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div class="sm:col-span-3">
                      <label for="force-format" class="block text-sm font-medium text-gray-700">Force Format</label>
                      <select v-model="form.force_format" id="force-format" required
                              class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md">
                        <option value="mp4">MP4</option>
                        
                      </select>
                    </div>
                    
                    <div class="sm:col-span-3">
                      <label for="movflags" class="block text-sm font-medium text-gray-700">MOV Flags</label>
                      <input type="text" v-model="form.movflags" id="movflags"
                             class="mt-1 focus:ring-blue-500 focus:border-blue-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                  </div>
                </div>
                
                <!-- Form Actions -->
                <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                  <button type="submit"
                          class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:col-start-2 sm:text-sm">
                    {{ isEditing ? 'Update Profile' : 'Create Profile' }}
                  </button>
                  <button type="button"
                          @click="$emit('close')"
                          class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:col-start-1 sm:text-sm">
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps({
  open: {
    type: Boolean,
    required: true
  },
  isEditing: {
    type: Boolean,
    default: false
  },
  profileData: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['submit', 'close'])

const form = ref({
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

watch(() => props.profileData, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const submitForm = () => {
  emit('submit', form.value)
}
</script>