<template>
  <DefaultLayout>
    <div class="bg-gray-50 min-h-screen py-12 px-4 sm:px-6">
      <div class="max-w-7xl mx-auto">
        <h1 class="text-3xl font-bold text-gray-800 mb-8">User Management</h1>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="user in users"
            :key="user.id"
            class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden border "
          >
            <!-- Card Header -->
            <div class="bg-rose-200 px-6 py-4 border-b border-indigo-100">
              <div class="flex justify-between items-center">
                <h3 class="text-lg font-semibold text-gray-900">Username : {{ user.name }}</h3>
                <span class="text-sm font-medium py-1 px-1 rounded-full "
                  :class="user.is_activated ? 'bg-white text-green-800' : 'bg-amber-100 text-amber-800'">
                  {{ user.is_activated ? 'Active' : 'Inactive' }}
                </span>
              </div>
              <p class="text-md text-gray-900 mt-1">User Role :{{ user.role }}</p>
            </div>

            <!-- User Details -->
            <div class="px-6 py-4 space-y-3">
              <div class="flex items-start">
                <EnvelopeIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                <a :href="`mailto:${user.email}`" class="text-sm text-gray-600 hover:text-indigo-600 hover:underline">Email:{{ user.email }}</a>
              </div>
              
              <div class="flex items-start">
                <PhoneIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                <a :href="`tel:${user.mobile}`" class="text-sm text-gray-600 hover:text-indigo-600">Mobile :{{ user.mobile }}</a>
              </div>
              
              <div class="flex items-start">
                <MapPinIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                <p class="text-sm text-gray-600">Address :{{ user.address }}</p>
              </div>
              
              <div class="pt-3 border-t border-gray-100 mt-3">
                <h4 class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Integration Settings</h4>
                
                <div class="space-y-2">
                  <div class="flex items-start">
                    <LinkIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                    <p class="text-sm text-gray-600 break-all">callback_url :{{ user.callback_url || 'Not configured' }}</p>
                  </div>
                  
                  <div class="flex items-start">
                    <KeyIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                    <p class="text-sm text-gray-600 font-mono truncate">callback_key :{{ user.callback_key || '••••••••' }}</p>
                  </div>
                  
                  <div class="flex items-start">
                    <LockClosedIcon class="h-4 w-4 text-gray-400 mt-0.5 mr-2 flex-shrink-0" />
                    <p class="text-sm text-gray-600 font-mono truncate">callback_secret_key :{{ user.callback_secret_key ? '••••••••' : 'Not set' }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Footer -->
            <div class="px-6 py-3 border-t border-gray-100 flex justify-between items-center">
              <div class="flex items-center">
                <BellIcon class="h-4 w-4 mr-1.5" :class="user.email_notification ? 'text-blue-500' : 'text-gray-400'" />
                <span class="text-xs font-medium" :class="user.email_notification ? 'text-gray-700' : 'text-gray-500'">
                 Email Notifications {{ user.email_notification ? 'ON' : 'OFF' }}
                </span>
              </div>
              
              <div class="flex space-x-2">
                <button 
                  @click="openEditModal(user)"
                  class="text-xs font-medium px-3 py-1.5 rounded-md bg-white text-indigo-600 hover:bg-indigo-100 transition"
                >
                  Edit
                </button>
                <button class="text-xs font-medium px-3 py-1.5 rounded-md bg-gray-100 text-gray-600 hover:bg-gray-200 transition">
                  More
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit User Modal -->
    <div v-if="showEditModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl max-w-md w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-lg font-semibold text-gray-800">Edit User</h3>
            <button @click="closeEditModal" class="text-gray-400 hover:text-gray-500">
              <XMarkIcon class="h-6 w-6" />
            </button>
          </div>
          
          <form @submit.prevent="saveUser">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                <input 
                  v-model="editingUser.name"
                  type="text" 
                  class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                  required
                >
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                <input 
                  v-model="editingUser.email"
                  type="email" 
                  class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                  required
                >
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Mobile</label>
                <input 
                  v-model="editingUser.mobile"
                  type="tel" 
                  class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                >
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Address</label>
                <textarea 
                  v-model="editingUser.address"
                  rows="3"
                  class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                ></textarea>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Role</label>
                <select 
                  v-model="editingUser.role"
                  class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                >
                  <option value="admin">admin</option>
                  <option value="user">user</option>
                  <option value="manager"></option>
                </select>
              </div>
              
              <div class="flex items-center">
                <input 
                  v-model="editingUser.is_activated"
                  type="checkbox" 
                  id="isActive"
                  class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                >
                <label for="isActive" class="ml-2 block text-sm text-gray-700">Account Active</label>
              </div>
              
              <div class="flex items-center">
                <input 
                  v-model="editingUser.email_notification"
                  type="checkbox" 
                  id="emailNotifications"
                  class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                >
                <label for="emailNotifications" class="ml-2 block text-sm text-gray-700">Email Notifications</label>
              </div>
              
              <div class="pt-4 border-t border-gray-200">
                <h4 class="text-sm font-medium text-gray-700 mb-3">Integration Settings</h4>
                
                <div class="space-y-3">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Callback URL</label>
                    <input 
                      v-model="editingUser.callback_url"
                      type="url" 
                      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    >
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Callback Key</label>
                    <input 
                      v-model="editingUser.callback_key"
                      type="text" 
                      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    >
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Callback Secret Key</label>
                    <input 
                      v-model="editingUser.callback_secret_key"
                      type="password" 
                      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    >
                  </div>
                </div>
              </div>
            </div>
            
            <div class="mt-6 flex justify-end space-x-3">
              <button 
                type="button"
                @click="closeEditModal"
                class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Cancel
              </button>
              <button 
                type="submit"
                class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Save Changes
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import {
  EnvelopeIcon,
  PhoneIcon,
  MapPinIcon,
  LinkIcon,
  KeyIcon,
  LockClosedIcon,
  BellIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

const apiUrl = 'http://localhost:8084'
const users = ref<any[]>([])
const toast = useToast()


const showEditModal = ref(false)
const editingUser = ref<any>({
  id: '',
  name: '',
  email: '',
  mobile: '',
  address: '',
  role: 'user',
  is_activated: false,
  email_notification: false,
  callback_url: '',
  callback_key: '',
  callback_secret_key: ''
})

const fetchUsers = async () => {
  try {
    const res = await axios.get(`${apiUrl}/users`)
    users.value = res.data
  } catch (error: any) {
    toast.error('Failed to fetch user data: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

const openEditModal = (user: any) => {
  editingUser.value = JSON.parse(JSON.stringify(user)) // Deep copy
  showEditModal.value = true
}

const closeEditModal = () => {
  showEditModal.value = false
}

const saveUser = async () => {
  try {
    await axios.put(`${apiUrl}/users/update`, {
  ...editingUser.value,
  email_notification_status: editingUser.value.email_notification, // or set explicitly
}, {
  params: { user_id: editingUser.value.unique_id}
})


    toast.success('User updated successfully')
    fetchUsers() // Refresh the user list
    closeEditModal()
  } catch (error: any) {
    toast.error('Failed to update user: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>