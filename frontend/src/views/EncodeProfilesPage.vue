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
  
  <script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import DefaultLayout from '@/layout/DefaultLayout.vue'

const encodeProfileName = ref('')
const username = ref('')
const users = ref([])

const handleSubmit = async () => {
  const selectedUser = users.value.find(user => user.username === username.value)
  if (!selectedUser) {
      console.error('No valid user selected')
      return
    }
  else{
    console.log('found selected user')
}

console.log(selectedUser.unique_id)
  const payload = {
    
    name: encodeProfileName.value,
    user_id: selectedUser.unique_id
  }  
console.log(payload)
  try {
   
    const response = await axios.post('http://localhost:8084/encode-profile', payload, {
  headers: {
    'Content-Type': 'application/json'
  }
})

    console.log('Profile created successfully:', response.data)
  } catch (error) {
    console.error('Failed to create encode profile:', error)
  }
}


const fetchUsers = async () => {
  try {
  
    const response = await axios.get('http://localhost:8084/users', {
      headers: {
        'Content-Type': 'application/json'

      }
    })
    users.value = response.data
  } catch (error) {
    console.error('Failed to fetch users:', error)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>

  
  <style scoped>
  
  </style>
  
