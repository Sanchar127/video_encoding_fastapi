<template>
  <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6 rounded-b-xl">
    <div class="flex-1 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="text-sm text-gray-700">
        Showing <span class="font-medium">{{ pagination.start }}</span> to 
        <span class="font-medium">{{ pagination.end }}</span> of 
        <span class="font-medium">{{ pagination.totalItems }}</span> results
      </div>
      <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px">
        <button
          @click="goToPage(pagination.currentPage - 1)"
          :disabled="pagination.currentPage === 1"
          class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
        >
          <span class="sr-only">Previous</span>
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
          </svg>
        </button>
        <button
          v-for="page in visiblePages"
          :key="page"
          @click="goToPage(page)"
          :class="[
            page === pagination.currentPage 
              ? 'bg-blue-50 border-blue-500 text-blue-600 z-10' 
              : 'bg-white border-gray-300 text-gray-500 hover:bg-gray-50',
            'relative inline-flex items-center px-4 py-2 border text-sm font-medium'
          ]"
        >
          {{ page }}
        </button>
        <button
          @click="goToPage(pagination.currentPage + 1)"
          :disabled="pagination.currentPage === pagination.totalPages"
          class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
        >
          <span class="sr-only">Next</span>
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
          </svg>
        </button>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  pagination: {
    type: Object as () => {
      currentPage: number
      totalPages: number
      start: number
      end: number
      totalItems: number
    },
    required: true
  },
  visiblePages: {
    type: Array as () => number[],
    required: true
  }
})

const emit = defineEmits(['page-change'])

const goToPage = (page: number) => {
  emit('page-change', page)
}
</script>