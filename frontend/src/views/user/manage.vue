<template>
  <DefaultLayout>
    <div class="min-h-screen py-2 px-2 xs:px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <HeaderSection 
          v-model:search="searchQuery" 
          @add-user="handleAddUser"
        />
        <StatsCards 
          :total-users="totalUsers" 
          :active-users="activeUsers" 
          :blacklisted-users="totalBlacklistedUser" 
        />
        <UsersTable 
          :users="filteredUsers" 
          @edit-user="openEditModal" 
        />
        <Pagination />
        <EditUserModal 
          :show="showEditModal" 
          :user="editingUser" 
          @close="closeEditModal" 
          @save="saveUser" 
        />
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import HeaderSection from '../../components/user/HeaderSection.vue'
import StatsCards from '../../components/user/StatsCards.vue'
import UsersTable from '../../components/user/UsersTable.vue'
import Cookies from 'js-cookie'
import EditUserModal from '../../components/user/EditUserModal.vue'

const apiUrl = 'http://localhost:8084'

const users = ref<any[]>([])
const blacklistedUsers = ref<any[]>([])
const tokens = ref<any[]>([])
const toast = useToast()
const searchQuery = ref('')

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

// Computed properties
const totalUsers = computed(() => users.value.length)
const activeUsers = computed(() => users.value.filter(user => user.is_activated).length)
const totalBlacklistedUser = computed(() => blacklistedUsers.value.length)

const filteredUsers = computed(() => {
  if (!searchQuery.value.trim()) return users.value
  
  const query = searchQuery.value.toLowerCase().trim()
  return users.value.filter(user => {
    return (
      user.name?.toLowerCase().includes(query) ||
      user.email?.toLowerCase().includes(query) ||
      user.role?.toLowerCase().includes(query) ||
      user.mobile?.includes(query) ||
      user.callback_url?.toLowerCase().includes(query)
    )
  })
})

// Data fetching
const fetchUsers = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }
  try {
    const res = await axios.get(`${apiUrl}/users`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })
    users.value = res.data
  } catch (error: any) {
    toast.error('Failed to fetch user data: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

const fetchBlacklistedUsers = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }
  try {
    const res = await axios.get(`${apiUrl}/blacklisted-tokens/details`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })
    blacklistedUsers.value = res.data.blacklisted_tokens
  } catch (error: any) {
    toast.error('Failed to fetch blacklisted users: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

const fetchAllTokens = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }
  try {
    const res = await axios.get(`${apiUrl}/tokens/stored`, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })
    tokens.value = res.data
  } catch (error: any) {
    toast.error('Failed to fetch tokens: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}

// User actions
const openEditModal = (user: any) => {
  editingUser.value = JSON.parse(JSON.stringify(user))
  showEditModal.value = true
}

const closeEditModal = () => {
  showEditModal.value = false
}

const saveUser = async () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    return
  }
  try {
    await axios.put(`${apiUrl}/users/update`, {
      ...editingUser.value,
      email_notification_status: editingUser.value.email_notification,
    }, {
      params: { user_id: editingUser.value.unique_id },
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    })
    toast.success('User updated successfully')
    fetchUsers()
    closeEditModal()
  } catch (error: any) {
    toast.error('Failed to update user: ' + (error.response?.data?.detail || error.message))
    console.error(error)
  }
}


// Lifecycle hooks
onMounted(() => {
  fetchUsers()
  fetchBlacklistedUsers()
  fetchAllTokens()
})
</script>