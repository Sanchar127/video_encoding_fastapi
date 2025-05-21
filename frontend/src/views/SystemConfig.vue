<template>
  <DefaultLayout>
    <div class="px-6 py-10 max-w-7xl mx-auto">
      <!-- Header with Add Button -->
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-3xl font-bold text-gray-800">System Configuration</h2>
        <button
          @click="openCreateModal"
          class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-lg transition"
        >
          + Add Config
        </button>
      </div>

      
      <div class="bg-white rounded-2xl shadow-md overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-100 text-sm text-gray-700 uppercase tracking-wider">
            <tr>
              <th class="px-6 py-4 text-left">Key</th>
              <th class="px-6 py-4 text-left">Value</th>
              <th class="px-6 py-4 text-left">Description</th>
              <th class="px-6 py-4 text-left">Updated By</th>
              <th class="px-6 py-4 text-left">Updated At</th>
              <th class="px-6 py-4 text-left">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 text-gray-700 text-sm">
            <tr
              v-for="config in configs"
              :key="config.id"
              class="hover:bg-gray-50 transition"
            >
              <td class="px-6 py-4 font-medium text-gray-900">
                {{ config.config_key }}
              </td>
              <td class="px-6 py-4">{{ config.value }}</td>
              <td class="px-6 py-4">{{ config.description }}</td>
              <td class="px-6 py-4">{{ config.updated_by }}</td>
              <td class="px-6 py-4">
                {{ formatDate(config.updated_at) }}
              </td>
              <td class="px-6 py-4">
                <button
                  @click="openEditModal(config)"
                  class="inline-flex items-center text-sm font-semibold text-blue-600 hover:text-blue-800 transition"
                >
                  <svg
                    class="w-5 h-5 mr-1"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M16.862 3.487a2.119 2.119 0 0 1 3 3l-11.05 11.05a4.242 4.242 0 0 1-1.773 1.06l-3.366.961.961-3.366a4.242 4.242 0 0 1 1.06-1.773l11.05-11.05Z"
                    />
                  </svg>
                  Edit
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Form Modal -->
      <SystemConfig
        :visible="showModal"
        :title="modalTitle"
        :initialData="formData"
        @submit="handleSubmit"
        @close="showModal = false"
      />
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import DefaultLayout from '../layout/DefaultLayout.vue'
import SystemConfig from '../components/form/SystemConfig.vue'

interface SystemConfigItem {
  id: number
  config_key: string
  value: string
  description: string
  updated_by: number | string
  created_at: string
  updated_at: string
}

const configs = ref<SystemConfigItem[]>([])

const showModal = ref(false)
const isEditMode = ref(false)
const currentEditId = ref<number | null>(null)
const modalTitle = ref('Add Configuration')

const defaultForm = () => ({
  config_key: '',
  value: '',
  updated_by: '',
  description: '',
})

const formData = ref(defaultForm())

const fetchConfigs = async () => {
  try {
    const response = await axios.get('/api/system-config')
    configs.value = response.data
  } catch (err) {
    console.error('Failed to fetch configs:', err)
  }
}

const openCreateModal = () => {
  isEditMode.value = false
  currentEditId.value = null
  modalTitle.value = 'Add Configuration'
  formData.value = defaultForm()
  showModal.value = true
}

const openEditModal = (config: SystemConfigItem) => {
  isEditMode.value = true
  currentEditId.value = config.id
  modalTitle.value = 'Edit Configuration'
  formData.value = {
    config_key: config.config_key,
    value: config.value,
    updated_by: String(config.updated_by),
    description: config.description,
  }
  showModal.value = true
}

const handleSubmit = async (data: {
  config_key: string
  value: string
  updated_by: string
  description: string
}) => {
  try {
    if (isEditMode.value && currentEditId.value !== null) {
      await axios.put(`/api/system-config/${currentEditId.value}`, data)
    } else {
      await axios.post('/api/system-config', data)
    }
    showModal.value = false
    fetchConfigs()
  } catch (err) {
    console.error('Failed to save config:', err)
  }
}

const formatDate = (iso: string) => {
  const date = new Date(iso)
  return date.toLocaleString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

onMounted(fetchConfigs)
</script>
