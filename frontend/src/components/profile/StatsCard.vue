<template>
  <div class="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="bg-gray-100 p-4 rounded-lg border border-gray-200 shadow-sm">
      <h3 class="text-sm font-medium text-gray-600">Total Profiles</h3>
      <span class="text-2xl font-bold text-gray-800">{{ profileCount }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  profileCount: number
}>()
</script>