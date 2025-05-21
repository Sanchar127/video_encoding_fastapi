<template>
  <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between mb-4">
    <!-- Heading -->
    <h1 class="text-xl sm:text-2xl md:text-3xl font-bold text-gray-900">User Management</h1>

    <!-- Right Side: Search + Buttons -->
    <div class="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
      
      <!-- Search Input -->
      <div class="relative w-full sm:w-60 md:w-64">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
        </div>
        <input
          v-model="localSearchQuery"
          type="text"
          placeholder="Search users..."
          @input="emitSearchQuery"
          class="w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md text-sm bg-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-gray-200"
        />
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
        <!-- Add User Button -->
        <router-link to="/user/new" class="w-full sm:w-auto">
          <button class="w-full sm:w-auto inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <PlusIcon class="h-5 w-5 mr-2" />
            <span>Add User</span>
          </button>
        </router-link>

        <!-- Blacklist Button -->
        <router-link to="/blacklistuser" class="w-full sm:w-auto">
          <button class="w-full sm:w-auto inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-red-500 hover:bg-red-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-400">
            <PlusIcon class="h-5 w-5 mr-2" />
            <span>Blacklist</span>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'
import { MagnifyingGlassIcon, PlusIcon } from '@heroicons/vue/24/outline'

const localSearchQuery = ref('')

const emitSearchQuery = () => {
  emit('update:search', localSearchQuery.value)
}

defineEmits(['update:search'])
</script>