<template>
  <div class="bg-white shadow rounded-xl p-8 text-center">
    <div class="text-gray-300 mb-4">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-16 h-16 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
        <circle cx="9" cy="7" r="4"/>
        <path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
      </svg>
    </div>
    <h3 class="text-lg font-semibold text-gray-800 mb-2">No profiles found</h3>
    <p class="text-gray-500 mb-6">There are currently no encode profiles matching your search.</p>
    <button
      @click="$emit('reset')"
      class="px-5 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition flex items-center justify-center mx-auto gap-2"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
      </svg>
      Reset Search
    </button>
  </div>
</template>

<script setup lang="ts">
defineEmits(['reset'])
</script>