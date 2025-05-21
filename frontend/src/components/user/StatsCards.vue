<template>
  <div class="grid grid-cols-1 gap-3 xs:gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mb-4 xs:mb-6">
    <!-- Total Users Card -->
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-3 py-3 xs:px-4 xs:py-4 sm:p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-indigo-500 rounded-md p-1.5 xs:p-2 sm:p-3">
            <UsersIcon class="h-4 w-4 xs:h-5 xs:w-5 sm:h-6 sm:w-6 text-white" />
          </div>
          <div class="ml-3 xs:ml-4 w-0 flex-1">
            <dl>
              <dt class="text-xs xs:text-sm font-medium text-gray-500 truncate">Total Users</dt>
              <dd class="flex items-baseline">
                <div class="text-lg xs:text-xl sm:text-2xl font-semibold text-gray-900">{{ totalUsers }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Active Users Card -->
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-3 py-3 xs:px-4 xs:py-4 sm:p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-green-500 rounded-md p-1.5 xs:p-2 sm:p-3">
            <CheckCircleIcon class="h-4 w-4 xs:h-5 xs:w-5 sm:h-6 sm:w-6 text-white" />
          </div>
          <div class="ml-3 xs:ml-4 w-0 flex-1">
            <dl>
              <dt class="text-xs xs:text-sm font-medium text-gray-500 truncate">Active Users</dt>
              <dd class="flex items-baseline">
                <div class="text-lg xs:text-xl sm:text-2xl font-semibold text-gray-900">{{ activeUsers }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Blacklisted Users Card -->
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-3 py-3 xs:px-4 xs:py-4 sm:p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-yellow-500 rounded-md p-1.5 xs:p-2 sm:p-3">
            <ExclamationTriangleIcon class="h-4 w-4 xs:h-5 xs:w-5 sm:h-6 sm:w-6 text-white" />
          </div>
          <div class="ml-3 xs:ml-4 w-0 flex-1">
            <dl>
              <dt class="text-xs xs:text-sm font-medium text-gray-500 truncate">Blacklisted</dt>
              <dd class="flex items-baseline">
                <div class="text-lg xs:text-xl sm:text-2xl font-semibold text-gray-900">{{ blacklistedUsers }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { UsersIcon, CheckCircleIcon, ExclamationTriangleIcon } from '@heroicons/vue/24/outline'

defineProps<{
  totalUsers: number
  activeUsers: number
  blacklistedUsers: number
}>()
</script>