<template>
  <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-200">
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th v-for="header in headers" :key="header.key"
              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              :class="header.class">
              {{ header.label }}
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="profile in profiles" :key="profile.id" class="hover:bg-gray-50 transition-colors">
            <!-- Profile column -->
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-blue-100 flex items-center justify-center">
                  <span class="text-blue-600 font-medium">
                    {{ profile.profile.charAt(0).toUpperCase() }}
                  </span>
                </div>
                <div class="ml-4">
                  <div class="font-medium text-gray-900">{{ profile.profile }}</div>
                  <div class="text-sm text-gray-500">{{ profile.vcodec }} / {{ profile.acodec }}</div>
                </div>
              </div>
            </td>

          
            <td class="px-6 py-4 whitespace-nowrap text-gray-900 font-medium">{{ profile.width }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-900 font-medium">{{ profile.height }}</td>

            <!-- Video -->
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.video_bitrate }}kbps</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.max_bitrate || 'Auto' }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.pix_fmt }}</td>


            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.audio_bitrate }}kbps</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.audio_channel }}ch</td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-900">{{ profile.audio_frequency }}Hz</td>

    
            <td class="px-6 py-4 whitespace-nowrap">
              <span
                class="px-2 py-1 text-xs rounded-full"
                :class="{
                  'bg-blue-100 text-blue-800': profile.force_format === 'mp4',
                  'bg-purple-100 text-purple-800': profile.force_format === 'mov',
                  'bg-gray-100 text-gray-800': !['mp4', 'mov'].includes(profile.force_format)
                }"
              >
                {{ profile.force_format }}
              </span>
            </td>

            <!-- Actions -->
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="$emit('edit', profile)" class="text-indigo-600 hover:text-indigo-900 mr-4">
            <EditIcon/>
              </button>
         
            </td>
          </tr>
        </tbody>
      </table>
    </div>


  </div>
</template>

<script setup lang="ts">

import EditIcon from '../icons/EditIcon.vue'

defineProps({
  profiles: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const headers = [
  { key: 'profile', label: 'Profile', class: '' },
  { key: 'width', label: 'Width', class: '' },
  { key: 'height', label: 'Height', class: '' },
  { key: 'video_bitrate', label: 'Video Bitrate', class: '' },
  { key: 'max_bitrate', label: 'Max Bitrate', class: '' },
  { key: 'pix_fmt', label: 'Pixel Format', class: '' },
  { key: 'audio_bitrate', label: 'Audio Bitrate', class: '' },
  { key: 'audio_channel', label: 'Audio Channel', class: '' },
  { key: 'audio_frequency', label: 'Audio Frequency', class: '' },
  { key: 'format', label: 'Format', class: '' },
  { key: 'actions', label: 'Actions', class: 'text-right' }
]

defineEmits(['edit', 'delete'])
</script>
