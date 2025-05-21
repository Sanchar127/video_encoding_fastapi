<template>
  <div class="p-12 text-center">
    <div class="mx-auto flex items-center justify-center h-24 w-24 rounded-full bg-gray-100 mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">No jobs found</h3>
    <p class="text-gray-500 max-w-md mx-auto mb-6">
      We couldn't find any jobs matching your current filters. Try adjusting your search or reset the filters.
    </p>
    <button
      @click="$emit('reset')"
      class="px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors duration-200 shadow-sm"
    >
      Reset Filters
    </button>
  </div>
</template>

<script setup lang="ts">
defineEmits(['reset'])
</script>