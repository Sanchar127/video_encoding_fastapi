<template>
  <div class="bg-white shadow-lg rounded-xl overflow-hidden border border-gray-100 transition-all duration-300 hover:shadow-xl">
    <!-- Header -->
    <div class="p-5 border-b border-gray-100 flex justify-between items-center bg-gradient-to-r from-gray-50 to-white">
      <button 
        @click="$emit('refresh')" 
        class="flex items-center gap-2 px-4 py-2 bg-indigo-50 text-indigo-600 rounded-lg hover:bg-indigo-100 transition-colors duration-200"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Refresh
      </button>
    </div>
    
    <!-- Loading State -->
    <div v-if="loading" class="p-6">
      <div class="animate-pulse space-y-6">
        <div v-for="i in 5" :key="i" class="flex items-center gap-4">
          <div class="w-12 h-12 bg-gray-100 rounded-full"></div>
          <div class="flex-1 space-y-3">
            <div class="h-4 bg-gray-100 rounded w-3/4"></div>
            <div class="h-3 bg-gray-100 rounded w-1/2"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Table -->
    <div v-else-if="filteredJobs.length > 0" class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th v-for="header in headers" :key="header.key" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              {{ header.label }}
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <JobRow 
            v-for="job in filteredJobs" 
            :key="job.id" 
            :job="job"
            :details="details"
            @retry="$emit('retry', job.id)"
          />
        </tbody>
      </table>
    </div>
    
    <!-- Empty State -->
    <JobsEmptyState 
      v-else
      @reset="$emit('reset')"
    />
  </div>
</template>

<script setup lang="ts">
import JobRow from './JobRow.vue'
import JobsEmptyState from './JobsEmptyState.vue'

defineProps({
  loading: Boolean,
  filteredJobs: Array,
  details: Array
})

defineEmits(['refresh', 'retry', 'reset'])

const headers = [
  { key: 'filename', label: 'Filename' },
  { key: 'job_by', label: 'Job By' },
  { key: 'profile', label: 'Profile name' },
  { key: 'profile_details', label: 'Profile Details name' },
  { key: 'start_time', label: 'Start Time' },
  { key: 'end_time', label: 'End Time' },
  { key: 'status', label: 'Status' },
  { key: 'retry', label: 'Retry' },
  { key: 'duration', label: 'Duration' }
]
</script>