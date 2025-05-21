<template>
  <tr class="hover:bg-gray-50 transition-colors duration-150">
    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
      {{ job.video_filename }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ job.user?.name || 'Unknown' }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ job.encode_profile?.name || 'Unknown' }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ profileDetailsName }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ formatDate(job.started_at) }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ formatDate(job.ended_at) }}
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm">
      <span :class="statusClass" class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full">
        {{ job.status }}
      </span>
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      <CheckCircle v-if="job.status === 'completed'" class="text-green-500 w-full"/>
      <ArrowPathIcons 
        v-else
        class="text-rose-500 w-full hover:text-rose-600 transition-transform duration-300 cursor-pointer hover:rotate-180" 
        @click="$emit('retry')" 
      />
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
      {{ calculateDuration(job.started_at, job.ended_at) }}
    </td>
  </tr>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import CheckCircle from '../icons/CheckCircle.vue'
import ArrowPathIcons from '../icons/ArrowPathIcons.vue'

const props = defineProps({
  job: {
    type: Object,
    required: true
  },
  details: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['retry'])

const profileDetailsName = computed(() => {
  return props.details.find(p => p.id === props.job.encoding_profileDetails)?.profile || 'Unknown Profile'
})

const statusClass = computed(() => {
  switch (props.job.status.toLowerCase()) {
    case 'completed': return 'bg-green-100 text-green-800'
    case 'failed': return 'bg-red-100 text-red-800'
    case 'processing': return 'bg-blue-100 text-blue-800'
    default: return 'bg-gray-100 text-gray-800'
  }
})

const formatDate = (dateString: string) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleString()
}

const calculateDuration = (start: string, end: string) => {
  if (!start) return 'N/A'
  const startTime = new Date(start)
  const endTime = end ? new Date(end) : new Date()
  const seconds = Math.floor((endTime.getTime() - startTime.getTime()) / 1000)
  
  if (seconds < 60) return `${seconds}s`
  if (seconds < 3600) return `${Math.floor(seconds / 60)}m ${seconds % 60}s`
  return `${Math.floor(seconds / 3600)}h ${Math.floor((seconds % 3600) / 60)}m`
}
</script>