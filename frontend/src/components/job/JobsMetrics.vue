<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    <!-- Total Jobs -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-blue-500">
      <h3 class="text-gray-500 text-sm font-medium">Total Jobs</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.total_jobs }}</p>
    </div>

    <!-- Completed Jobs -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-green-500">
      <h3 class="text-gray-500 text-sm font-medium">Completed Jobs</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.completed_jobs }}</p>
      <p v-if="completionRate" class="text-green-600 text-sm mt-1">
        {{ completionRate }} completion rate
      </p>
    </div>

    <!-- Failed Jobs -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-red-500">
      <h3 class="text-gray-500 text-sm font-medium">Failed Jobs</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.failed_jobs }}</p>
      <p v-if="failureRate" class="text-red-600 text-sm mt-1">
        {{ failureRate }} failure rate
      </p>
    </div>

    <!-- Queued Jobs -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-yellow-500">
      <h3 class="text-gray-500 text-sm font-medium">Queued Jobs</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.queued_jobs }}</p>
      <p v-if="queuedRate" class="text-yellow-600 text-sm mt-1">
        {{ queuedRate }} queued rate
      </p>
    </div>

    <!-- Processing Jobs -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-indigo-500">
      <h3 class="text-gray-500 text-sm font-medium">Processing Jobs</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.processing_jobs }}</p>
      <p v-if="processingRate" class="text-indigo-600 text-sm mt-1">
        {{ processingRate }} processing rate
      </p>
    </div>

    <!-- Avg Processing Time -->
    <div class="bg-white shadow rounded-xl p-6 border-l-4 border-purple-500">
      <h3 class="text-gray-500 text-sm font-medium">Avg Processing Time</h3>
      <p class="text-3xl font-bold text-gray-800">{{ metrics.avg_processing_time || 'N/A' }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  metrics: {
    type: Object,
    required: true
  },
  completionRate: String,
  failureRate: String,
  queuedRate: String,
  processingRate: String
})
</script>
