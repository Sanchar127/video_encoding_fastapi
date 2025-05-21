<template>
  <div v-if="show" class="fixed z-50 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="emitClose"></div>
      <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true"></span>
      <div class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full sm:p-6">
        <div class="absolute top-0 right-0 pt-4 pr-4">
          <button type="button" class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" @click="emitClose">
            <span class="sr-only">Close</span>
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>
        <div class="sm:flex sm:items-start">
          <div class="mx-auto flex-shrink-0 flex items-center justify-center h-10 w-10 rounded-full bg-indigo-100 sm:mx-0 sm:h-10 sm:w-10">
            <UserIcon class="h-5 w-5 text-indigo-600" />
          </div>
          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">Edit User</h3>
            <div class="mt-2">
              <p class="text-sm text-gray-500">Update user details and permissions below.</p>
            </div>
          </div>
        </div>
        <div class="mt-5">
          <form @submit.prevent="emitSave">
            <div class="space-y-4">
              <!-- Basic Information Section -->
              <div>
                <h4 class="text-md font-medium text-gray-900 mb-2">Basic Information</h4>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-6">
                  <div class="sm:col-span-3">
                    <label for="name" class="block text-sm font-medium text-gray-700">Full name</label>
                    <input 
                      v-model="localUser.name"
                      type="text" 
                      id="name"
                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      required
                    >
                  </div>
                  <div class="sm:col-span-3">
                    <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
                    <input 
                      v-model="localUser.email"
                      type="email" 
                      id="email"
                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                      required
                    >
                  </div>
                  <div class="sm:col-span-3">
                    <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile number</label>
                    <input 
                      v-model="localUser.mobile"
                      type="tel" 
                      id="mobile"
                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    >
                  </div>
                  <div class="sm:col-span-3">
                    <label for="role" class="block text-sm font-medium text-gray-700">Role</label>
                    <select 
                      v-model="localUser.role"
                      id="role"
                      class="mt-1 block w-full bg-white border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    >
                      <option value="admin">Admin</option>
                      <option value="user">User</option>
                      <option value="super_admin">Super Admin</option>
                    </select>
                  </div>
                  <div class="sm:col-span-6">
                    <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
                    <textarea 
                      v-model="localUser.address"
                      id="address"
                      rows="2"
                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    ></textarea>
                  </div>
                </div>
              </div>

              <!-- Account Status Section -->
              <div>
                <h4 class="text-md font-medium text-gray-900 mb-2">Account Status</h4>
                <div class="space-y-3">
                  <div class="relative flex items-start">
                    <div class="flex items-center h-5">
                      <input 
                        v-model="localUser.is_activated"
                        id="isActive" 
                        type="checkbox" 
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                      >
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="isActive" class="font-medium text-gray-700">Account is active</label>
                      <p class="text-gray-500">User will be able to login if enabled.</p>
                    </div>
                  </div>
                  <div class="relative flex items-start">
                    <div class="flex items-center h-5">
                      <input 
                        v-model="localUser.email_notification"
                        id="emailNotifications" 
                        type="checkbox" 
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                      >
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="emailNotifications" class="font-medium text-gray-700">Email notifications</label>
                      <p class="text-gray-500">User will receive email notifications if enabled.</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Integration Settings Section -->
              <div>
                <h4 class="text-md font-medium text-gray-900 mb-2">Integration Settings</h4>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-6">
                  <div class="sm:col-span-6">
                    <label for="callback_url" class="block text-sm font-medium text-gray-700">Callback URL</label>
                    <div class="mt-1 flex rounded-md shadow-sm">
                      <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 text-sm">
                        <LinkIcon class="h-4 w-4 text-gray-400" />
                      </span>
                      <input 
                        v-model="localUser.callback_url"
                        type="url" 
                        id="callback_url"
                        class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        placeholder="https://example.com/callback"
                      >
                    </div>
                  </div>
                  <div class="sm:col-span-3">
                    <label for="callback_key" class="block text-sm font-medium text-gray-700">API Key</label>
                    <div class="mt-1 flex rounded-md shadow-sm">
                      <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 text-sm">
                        <KeyIcon class="h-4 w-4 text-gray-400" />
                      </span>
                      <input 
                        v-model="localUser.callback_key"
                        type="text" 
                        id="callback_key"
                        class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        placeholder="Your API key"
                      >
                    </div>
                  </div>
                  <div class="sm:col-span-3">
                    <label for="callback_secret_key" class="block text-sm font-medium text-gray-700">Secret Key</label>
                    <div class="mt-1 flex rounded-md shadow-sm">
                      <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 text-sm">
                        <LockClosedIcon class="h-4 w-4 text-gray-400" />
                      </span>
                      <input 
                        v-model="localUser.callback_secret_key"
                        type="password" 
                        id="callback_secret_key"
                        class="flex-1 min-w-0 block w-full px-3 py-2 rounded-none rounded-r-md border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        placeholder="Your secret key"
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="mt-6 flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-3">
              <button 
                type="button"
                @click="emitClose"
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:w-auto sm:text-sm"
              >
                Cancel
              </button>
              <button 
                type="submit"
                class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:w-auto sm:text-sm"
              >
                Save Changes
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { UserIcon, XMarkIcon, LinkIcon, KeyIcon, LockClosedIcon } from '@heroicons/vue/24/outline'

defineProps<{
  show: boolean
  user: any
}>()

const emit = defineEmits(['close', 'save'])

const localUser = defineModel('user', { required: true })

const emitClose = () => {
  emit('close')
}

const emitSave = () => {
  emit('save')
}
</script>