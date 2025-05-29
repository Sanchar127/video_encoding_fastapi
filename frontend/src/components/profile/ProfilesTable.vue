<template>
  <div class="bg-white shadow rounded-xl overflow-hidden">
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th scope="col" class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Profile Name</th>
            <th scope="col" class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
            <th scope="col" class="px-4 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="profile in profiles" :key="profile.id" class="hover:bg-gray-50 transition">
            <td class="px-4 py-4">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10 bg-blue-100 rounded-full flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
                  </svg>
                </div>
                <div class="ml-4">
                  <div class="text-sm font-medium text-gray-900">{{ profile.name }}</div>
                  <div class="text-sm text-gray-500">ID: {{ profile.id }}</div>
                </div>
              </div>
            </td>
            <td class="px-4 py-4">
              <div class="text-sm text-gray-900">{{ profile.user?.name || 'Unknown' }}</div>
              <div class="text-sm text-gray-500">{{ profile.user?.email || 'No email' }}</div>
            </td>
            <td class="px-4 py-4 text-right text-sm font-medium">
              <button
                @click="$emit('edit-profile', profile)"
                class="text-blue-600 hover:text-blue-900 mr-3 inline-flex items-center"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                <span class="hidden sm:inline">Edit</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  profiles: {
    type: Array as () => Array<{
      id: string
      name: string
      user?: {
        name?: string
        email?: string
      }
    }>,
    required: true
  }
})

defineEmits(['edit-profile'])
</script>