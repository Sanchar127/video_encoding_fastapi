<template>
  <div class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50 p-4">
    <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-xl">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-semibold text-gray-800">{{ isEditMode ? 'Edit Profile' : 'Add Profile' }}</h2>
        <button @click="$emit('close')" class="text-gray-400 hover:text-gray-500">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Profile Name</label>
          <input
            v-model="formData.name"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            type="text"
            placeholder="Enter profile name"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">User</label>
          <select
            v-model="formData.user_id"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="">Select User</option>
            <option v-for="user in users" :key="user.id" :value="user.unique_id">
              {{ user.name }} ({{ user.email }})
            </option>
          </select>
        </div>
      </div>
      <div class="mt-6 flex justify-end gap-3">
        <button 
          @click="$emit('close')" 
          class="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition"
        >
          Cancel
        </button>
        <button 
          @click="$emit('submit')" 
          class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
          :disabled="!formData.name"
          :class="{'opacity-50 cursor-not-allowed': !formData.name}"
        >
          {{ isEditMode ? 'Save Changes' : 'Create Profile' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  isEditMode: {
    type: Boolean,
    default: false
  },
  formData: {
    type: Object as () => {
      name: string
      user_id: string
    },
    required: true
  },
  users: {
    type: Array as () => Array<{
      id: string
      name: string
      email: string
      unique_id: string
    }>,
    required: true
  }
})

defineEmits(['close', 'submit'])
</script>