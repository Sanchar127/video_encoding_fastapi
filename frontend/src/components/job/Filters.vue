<template>
  <div class="bg-white shadow rounded-xl p-6 mb-8">
    <h3 class="text-lg font-semibold text-gray-800 mb-4">Filters</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Status Filter -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
        <select 
          v-model="filters.status" 
          class="w-full px-3 py-2 border rounded-md"
        >
          <option value="">All Statuses</option>
          <option value="queued">queued</option>
          <option value="processing">processing</option>
          <option value="completed">completed</option>
          <option value="failed">failed</option>
        </select>
      </div>
      
      <!-- Date Range Filter -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Date Range</label>
        <select 
          v-model="filters.date_range" 
          class="w-full px-3 py-2 border rounded-md"
        >
          <option value="all">All Time</option>
          <option value="today">Today</option>
          <option value="week">This Week</option>
          <option value="month">This Month</option>
          <option value="custom">Custom</option>
        </select>
      </div>
      
      <!-- Custom Date Filters -->
      <div v-if="filters.date_range === 'custom'">
        <label class="block text-sm font-medium text-gray-700 mb-1">From</label>
        <input v-model="filters.start_date" type="date" class="w-full px-3 py-2 border rounded-md">
      </div>
      
      <div v-if="filters.date_range === 'custom'">
        <label class="block text-sm font-medium text-gray-700 mb-1">To</label>
        <input v-model="filters.end_date" type="date" class="w-full px-3 py-2 border rounded-md">
      </div>
    </div>
    
    <div class="mt-4 flex justify-end gap-2">
      <button 
        @click="$emit('reset')" 
        class="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200"
      >
        Reset
      </button>
      <button 
        @click="$emit('apply')" 
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500"
      >
        Apply
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  filters: {
    type: Object,
    required: true
  }
})

defineEmits(['reset', 'apply'])
</script>