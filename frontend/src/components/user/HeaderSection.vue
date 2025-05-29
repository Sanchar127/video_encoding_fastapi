<template>
  <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between mb-6 px-4 sm:px-0">
  <HeroHeader title="User Management"/>

    <div class="flex flex-col gap-3 md:flex-row md:flex-wrap md:items-center md:gap-4 w-full md:w-auto">
      <div class="relative w-full sm:w-64 md:w-72 lg:w-80">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center">
          <SearchIcons class="h-5 w-5 text-gray-500 cursor-pointer hover:text-gray-700" />
        </div>
        <input
          :value="modelValue"
          type="text"
          placeholder="Search users..."
          @input="handleInput"
          class="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg text-sm md:text-base bg-white placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all duration-200"
        />
      </div>

      <div class="grid grid-cols-2 gap-3 sm:flex sm:gap-2 md:gap-3 w-full sm:w-auto">
        <router-link to="/user/new" class="flex items-center justify-center">
          <button class="w-full sm:w-auto flex items-center justify-center px-4 py-2.5 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200 whitespace-nowrap">
            <PlusIcon class="h-5 w-5 mr-2 -ml-1" />
            <span>Add User</span>
          </button>
        </router-link>

        <router-link to="/blacklistuser" class="flex items-center justify-center">
          <button class="w-full sm:w-auto flex items-center justify-center px-4 py-2.5 text-sm font-medium text-white bg-red-600 hover:bg-red-700 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors duration-200 whitespace-nowrap">
            <PlusIcon class="h-5 w-5 mr-2 -ml-1" />
            <span>Blacklist</span>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import SearchIcons from '../icons/SearchIcons.vue'
import PlusIcon from '../icons/PlusIcon.vue'
import HeroHeader from '../HeroHeader.vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:modelValue'])

const handleInput = (event: Event) => {
  emit('update:modelValue', (event.target as HTMLInputElement).value)
}
</script>