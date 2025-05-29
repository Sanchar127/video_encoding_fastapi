<template>
  <div class="bg-white shadow rounded-xl p-6">
    <div class="animate-pulse space-y-4">
      <div v-for="i in 5" :key="i" class="flex items-center gap-4">
        <div class="w-12 h-12 bg-gray-200 rounded-full"></div>
        <div class="flex-1 space-y-2">
          <div class="h-4 bg-gray-200 rounded w-3/4"></div>
          <div class="h-4 bg-gray-200 rounded w-1/2"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>