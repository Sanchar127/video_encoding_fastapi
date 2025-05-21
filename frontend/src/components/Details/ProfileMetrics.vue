<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
    <!-- Total Profiles Card -->
    <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl p-6 text-white shadow-lg">
      <h3 class="text-sm font-medium">Total Profiles Details</h3>
      <p class="text-3xl font-bold">{{ totalProfiles }}</p>
      <div class="flex items-center mt-2">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path>
        </svg>
        <span class="text-xs ml-1">All time</span>
      </div>
    </div>

   
  </div>
</template>

<script setup lang="ts">
defineProps({
  totalProfiles: {
    type: Number,
    required: true
  },
  activeProfiles: {
    type: Number,
    default: 0
  },
  hdProfiles: {
    type: Number,
    default: 0
  },
  recentActivity: {
    type: Number,
    default: 0
  }
})
</script>