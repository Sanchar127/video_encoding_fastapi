<template>
  <div class="bg-white shadow overflow-hidden rounded-lg">
    <div class="overflow-x-auto">
      <!-- Mobile view - stacked cards -->
      <div class="block sm:hidden">
        <div class="space-y-3 xs:space-y-4 p-3 xs:p-4">
          <div v-for="user in users" :key="user.id" class="border rounded-lg p-3 xs:p-4 hover:bg-gray-50">
            <div class="flex items-center mb-2 xs:mb-3">
              <div class="h-7 w-7 xs:h-8 xs:w-8 rounded-full bg-indigo-100 flex items-center justify-center">
                <UserIcon class="h-4 w-4 xs:h-5 xs:w-5 text-indigo-600" />
              </div>
              <div class="ml-2 xs:ml-3">
                <div class="font-medium text-sm xs:text-base text-gray-900">{{ user.name }}</div>
                <div class="text-xs text-gray-500">{{ user.role }}</div>
              </div>
            </div>
            
            <div class="text-sm mb-2">
              <a :href="`mailto:${user.email}`" class="text-indigo-600 hover:text-indigo-900 flex items-center">
                <EnvelopeIcon class="h-3 w-3 xs:h-4 xs:w-4 mr-1" />
                {{ user.email }}
              </a>
            </div>
            
            <div class="flex justify-between items-center mb-2">
              <span :class="user.is_activated ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" 
                    class="px-2 py-1 text-xs rounded-full">
                {{ user.is_activated ? 'Active' : 'Inactive' }}
              </span>
              <button @click="emitEditUser(user)" class="text-indigo-600 hover:text-indigo-900">
                <PencilSquareIcon class="h-4 w-4 xs:h-5 xs:w-5" />
              </button>
            </div>
            
            <div class="text-xs text-gray-500 space-y-1">
              <div v-if="user.mobile" class="flex items-center">
                <PhoneIcon class="h-3 w-3 mr-1" />
                {{ user.mobile }}
              </div>
              <div class="flex items-center">
                <BellIcon :class="user.email_notification ? 'text-green-500' : 'text-gray-400'" class="h-3 w-3 mr-1" />
                {{ user.email_notification ? 'Notifications On' : 'Notifications Off' }}
              </div>
              <div v-if="user.callback_url" class="truncate">
                <LinkIcon class="h-3 w-3 mr-1 inline" />
                {{ truncateUrl(user.callback_url) }}
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Desktop view - full table -->
      <table class="hidden sm:table min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/6">User</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/5">Contact</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/12">Role</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/12">Status</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/12">Notifications</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/6">API Key</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/6">Callback URL</th>
            <th scope="col" class="px-3 xs:px-4 py-2 xs:py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/12">Action</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-7 w-7 xs:h-8 xs:w-8">
                  <div class="h-7 w-7 xs:h-8 xs:w-8 rounded-full bg-indigo-100 flex items-center justify-center">
                    <UserIcon class="h-4 w-4 xs:h-5 xs:w-5 text-indigo-600" />
                  </div>
                </div>
                <div class="ml-2 xs:ml-3">
                  <div class="text-xs xs:text-sm font-medium text-gray-900">{{ user.name }}</div>
                </div>
              </div>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <div class="text-xs xs:text-sm text-gray-900">
                <a :href="`mailto:${user.email}`" class="flex items-center text-indigo-600 hover:text-indigo-900">
                  <EnvelopeIcon class="flex-shrink-0 mr-1 h-3 w-3 xs:h-4 xs:w-4" />
                  {{ user.email }}
                </a>
              </div>
              <div v-if="user.mobile" class="text-xs text-gray-500 mt-1 flex items-center">
                <PhoneIcon class="flex-shrink-0 mr-1 h-3 w-3" />
                {{ user.mobile }}
              </div>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <span :class="{
                'bg-purple-100 text-purple-800': user.role === 'admin',
                'bg-green-100 text-green-800': user.role === 'user',
                'bg-blue-100 text-blue-800': user.role === 'manager'
              }" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full capitalize">
                {{ user.role }}
              </span>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <span :class="user.is_activated ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" 
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ user.is_activated ? 'Active' : 'Inactive' }}
              </span>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <div class="flex items-center">
                <span :class="user.email_notification ? 'text-green-500' : 'text-gray-400'">
                  <BellIcon class="h-3 w-3 xs:h-4 xs:w-4" />
                </span>
                <span class="ml-1 text-xs text-gray-500">
                  {{ user.email_notification ? 'On' : 'Off' }}
                </span>
              </div>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap">
              <div class="text-xs font-mono text-gray-500 truncate max-w-[80px] xs:max-w-[100px]">
                {{ user.callback_key || '—' }}
              </div>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4">
              <div class="text-xs text-gray-900 truncate max-w-[100px] xs:max-w-[120px]" :title="user.callback_url || 'Not configured'">
                <span v-if="user.callback_url" class="flex items-center text-indigo-600">
                  <LinkIcon class="flex-shrink-0 mr-1 h-3 w-3" />
                  {{ truncateUrl(user.callback_url) }}
                </span>
                <span v-else class="text-gray-400">—</span>
              </div>
            </td>
            <td class="px-3 xs:px-4 py-3 xs:py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="emitEditUser(user)" class="text-indigo-600 hover:text-indigo-900">
                <PencilSquareIcon class="h-4 w-4 xs:h-5 xs:w-5" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { UserIcon, EnvelopeIcon, PhoneIcon, LinkIcon, BellIcon, PencilSquareIcon } from '@heroicons/vue/24/outline'

defineProps<{
  users: any[]
}>()

const emit = defineEmits(['edit-user'])

const truncateUrl = (url: string) => {
  if (!url) return ''
  return url.length > 30 ? url.substring(0, 30) + '...' : url
}

const emitEditUser = (user: any) => {
  emit('edit-user', user)
}
</script>