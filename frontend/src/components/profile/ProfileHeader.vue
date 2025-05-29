<template>
  <div class="bg-white shadow-lg rounded-xl p-6 mb-8 border border-gray-200">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
      <div class="flex items-center gap-4 bg-gray-100 p-4 rounded-lg w-full md:w-auto">
        <div class="p-3 bg-blue-100 rounded-full flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
        </div>
        <div>
          <h1 class="text-2xl font-semibold text-gray-900">Encode Profiles</h1>
          <p class="text-sm text-gray-600 mt-1">Manage all encoding profiles</p>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
        <button
          @click="$emit('refresh')"
          class="flex items-center justify-center gap-2 px-4 py-2 bg-gray-100 border border-gray-300 rounded-lg hover:bg-gray-200 transition whitespace-nowrap"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          <span class="hidden sm:inline">Refresh</span>
        </button>
        <button
          @click="$emit('add-profile')"
          class="flex items-center justify-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition whitespace-nowrap"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          <span class="hidden sm:inline">Add Profile</span>
        </button>
      </div>
    </div>

    <div class="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
      <div class="bg-gray-100 p-4 rounded-lg border border-gray-200 shadow-sm">
        <h3 class="text-sm font-medium text-gray-600">Total Profiles</h3>
        <span class="text-2xl font-bold text-gray-800">{{ profileCount }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  profileCount: {
    type: Number,
    required: true
  }
})

defineEmits(['refresh', 'add-profile'])
</script>