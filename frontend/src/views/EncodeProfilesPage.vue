<template>
    <DefaultLayout>

        <div class="min-h-screen flex items-center justify-center p-6">
          <div class="bg-white shadow-xl rounded-2xl p-8 w-full max-w-md">
            <h2 class="text-2xl font-bold mb-6 text-center">Create Encode Profile</h2>
            <form @submit.prevent="handleSubmit" class="space-y-4">
              <div>
                <label class="block font-medium mb-1">Encode Profile Name</label>
                <input
                  type="text"
                  v-model="encodeProfileName"
                  class="w-full border border-gray-300 rounded-lg p-2"
                  placeholder="e.g., 720p_H264"
                  required
                />
              </div>
              <div>
      <label class="block font-medium mb-1">Username</label>
      <select
  v-model="username"
  class="w-full border border-gray-300 rounded-lg p-2"
  required
>
  <option disabled value="">Select a username</option>
  <option v-for="user in users" :key="user.id" :value="user.username">
    {{ user.name }}
  </option>
</select>

   
    </div>
    
              <button
                type="submit"
                class="w-full bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700"
              >
                Submit
              </button>
            </form>
          </div>
        </div>
    </DefaultLayout>
  </template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import { useToast } from 'vue-toastification'
import DefaultLayout from '@/layout/DefaultLayout.vue'

const apiUrl = 'http://localhost:8084'
const encodeProfileName = ref('')
const username = ref('')
const users = ref<any[]>([])
const toast = useToast()

// Fetch users on mount
const fetchUsers = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please log in again.')
    return
  }

  try {
    const response = await axios.get(`${apiUrl}/users`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      }
    })
    users.value = response.data
  } catch (error: any) {
    toast.error('Failed to fetch users: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

// Handle encode profile submission
const handleSubmit = async () => {
  const selectedUser = users.value.find(user => user.username === username.value)

  if (!selectedUser) {
    toast.error('No valid user selected.')
    return
  }

  const payload = {
    name: encodeProfileName.value,
    user_id: selectedUser.unique_id,
  }

  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please log in again.')
    return
  }

  try {
    const response = await axios.post(`${apiUrl}/encode-profile`, payload, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      }
    })
    toast.success('Encode Profile Created Successfully')
    console.log('Profile created:', response.data)
  } catch (error: any) {
    toast.error('Failed to create encode profile: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>