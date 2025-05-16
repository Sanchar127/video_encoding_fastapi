<template>
  <DefaultLayout>
    <div class="max-w-4xl mx-auto p-4 sm:p-6">
      <!-- Header Section -->
      <div class="mb-8 flex flex-col sm:flex-row items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">System Configuration</h1>
          <p class="text-gray-500 mt-1 text-sm sm:text-base">Manage your system parameters and operational settings</p>
        </div>
        <div class="bg-blue-50 p-3 rounded-lg w-full sm:w-auto">
          <p class="text-sm text-blue-700 flex items-center">
            <InformationCircleIcon class="h-5 w-5 mr-2 flex-shrink-0" />
            <span>Changes may require system restart to take effect</span>
          </p>
        </div>
      </div>

      <!-- Settings Card -->
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden transition-all duration-200 hover:shadow-md">
        <!-- Card Header -->
        <div class="bg-gradient-to-r from-gray-50 to-gray-100 px-6 py-4 border-b border-gray-200">
          <div class="flex items-center">
            <CogIcon class="h-6 w-6 text-blue-600 mr-3" />
            <div>
              <h2 class="text-lg font-semibold text-gray-800">Core Parameters</h2>
              <p class="text-sm text-gray-500 mt-1">Essential system configuration options</p>
            </div>
          </div>
        </div>

        <!-- Settings Form -->
        <form @submit.prevent="saveSettings" class="divide-y divide-gray-200">
          <!-- Configuration Key -->
          <div class="px-6 py-5 hover:bg-gray-50 transition-colors duration-150">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="md:col-span-1">
                <label class="block text-sm font-medium text-gray-700">Configuration Key</label>
                <p class="text-xs text-gray-500 mt-1">Unique system identifier</p>
              </div>
              <div class="md:col-span-2">
                <div class="relative">
                  <input
                    v-model="form.configkey"
                    type="text"
                    placeholder="e.g. SYSTEM_MAX_RETRIES"
                    class="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm py-2 px-3 transition-all duration-150"
                    :class="{ 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500': errors.configkey }"
                  />
                  <div v-if="errors.configkey" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                  </div>
                </div>
                <p v-if="errors.configkey" class="mt-2 text-sm text-red-600">{{ errors.configkey }}</p>
                <p v-else class="mt-2 text-xs text-gray-500">Use uppercase letters, numbers and underscores only</p>
              </div>
            </div>
          </div>

          <!-- Max Retry -->
          <div class="px-6 py-5 bg-gray-50 hover:bg-gray-100 transition-colors duration-150">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="md:col-span-1">
                <label class="block text-sm font-medium text-gray-700">Max Retry Attempts</label>
                <p class="text-xs text-gray-500 mt-1">Between 0 (disabled) and 10</p>
              </div>
              <div class="md:col-span-2">
                <div class="flex items-center gap-4">
                  <div class="relative flex-1 max-w-[8rem]">
                    <input
                      v-model.number="form.Maxretry"
                      type="number"
                      min="0"
                      max="10"
                      class="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm py-2 px-3"
                      :class="{ 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500': errors.Maxretry }"
                    />
                    <div v-if="errors.Maxretry" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                      <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                    </div>
                  </div>
                  <div class="flex-1">
                    <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                      <div 
                        class="h-full bg-blue-500 transition-all duration-300" 
                        :style="{ width: `${form.Maxretry * 10}%` }"
                      ></div>
                    </div>
                  </div>
                </div>
                <p v-if="errors.Maxretry" class="mt-2 text-sm text-red-600">{{ errors.Maxretry }}</p>
              </div>
            </div>
          </div>

          <!-- Description -->
          <div class="px-6 py-5 hover:bg-gray-50 transition-colors duration-150">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="md:col-span-1">
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <p class="text-xs text-gray-500 mt-1">Detailed explanation of this setting</p>
              </div>
              <div class="md:col-span-2">
                <div class="relative">
                  <textarea
                    v-model="form.Description"
                    rows="4"
                    class="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm py-2 px-3 transition-all duration-150"
                    :class="{ 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500': errors.Description }"
                  ></textarea>
                  <div v-if="errors.Description" class="absolute top-3 right-3">
                    <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                  </div>
                </div>
                <p v-if="errors.Description" class="mt-2 text-sm text-red-600">{{ errors.Description }}</p>
                <p v-else class="mt-2 text-xs text-gray-500 flex justify-between">
                  <span>{{ form.Description.length }}/500 characters</span>
                  <span v-if="form.Description.length < 10" class="text-orange-500">Minimum 10 characters required</span>
                </p>
              </div>
            </div>
          </div>

          <!-- Form Actions -->
          <div class="px-6 py-4 bg-gray-50 text-right border-t border-gray-200">
            <button
              type="button"
              @click="resetForm"
              class="mr-3 inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-150"
            >
              <ArrowPathIcon class="h-4 w-4 mr-2" />
              Reset
            </button>
            <button
              type="submit"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-150"
              :disabled="loading"
              :class="{ 'opacity-75 cursor-not-allowed': loading }"
            >
              <svg
                v-if="loading"
                class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <CheckIcon v-else class="-ml-1 mr-2 h-4 w-4" />
              {{ loading ? 'Saving...' : 'Save Changes' }}
            </button>
          </div>
        </form>
      </div>

      <!-- Success Notification -->
      <Transition name="fade">
        <div v-if="showSuccess" class="fixed bottom-4 right-4">
          <div class="bg-green-50 border border-green-200 rounded-lg shadow-lg p-4 max-w-sm">
            <div class="flex items-start">
              <div class="flex-shrink-0">
                <CheckCircleIcon class="h-5 w-5 text-green-500" />
              </div>
              <div class="ml-3">
                <h3 class="text-sm font-medium text-green-800">Settings saved successfully</h3>
                <p class="text-sm text-green-600 mt-1">Your configuration changes have been applied.</p>
              </div>
              <div class="ml-auto pl-3">
                <button @click="showSuccess = false" class="text-green-500 hover:text-green-600">
                  <XMarkIcon class="h-5 w-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </div>
  </DefaultLayout>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import DefaultLayout from '../layout/DefaultLayout.vue'
import { 
  ExclamationCircleIcon, 
  InformationCircleIcon,
  CogIcon,
  ArrowPathIcon,
  CheckIcon,
  CheckCircleIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

interface SettingsForm {
  configkey: string
  Maxretry: number
  Description: string
}

const defaultForm: SettingsForm = {
  configkey: 'SYSTEM_MAX_RETRIES',
  Maxretry: 3,
  Description: 'Maximum number of retry attempts for failed operations before giving up.'
}

const form = reactive<SettingsForm>({ ...defaultForm })

const errors = reactive<{
  configkey?: string
  Maxretry?: string
  Description?: string
}>({})

const loading = ref(false)
const showSuccess = ref(false)

function resetForm() {
  Object.assign(form, defaultForm)
  errors.configkey = ''
  errors.Maxretry = ''
  errors.Description = ''
}

function validateForm(): boolean {
  let isValid = true
  errors.configkey = ''
  errors.Maxretry = ''
  errors.Description = ''

  if (!form.configkey.trim()) {
    errors.configkey = 'Configuration key is required'
    isValid = false
  } else if (!/^[A-Z0-9_]+$/.test(form.configkey)) {
    errors.configkey = 'Only uppercase letters, numbers and underscores allowed'
    isValid = false
  }

  if (form.Maxretry < 0 || form.Maxretry > 10 || isNaN(form.Maxretry)) {
    errors.Maxretry = 'Enter a value between 0 and 10'
    isValid = false
  }

  if (!form.Description.trim()) {
    errors.Description = 'Description is required'
    isValid = false
  } else if (form.Description.length < 10) {
    errors.Description = 'Description must be at least 10 characters'
    isValid = false
  } else if (form.Description.length > 500) {
    errors.Description = 'Description must be less than 500 characters'
    isValid = false
  }

  return isValid
}

async function saveSettings() {
  if (!validateForm()) return

  loading.value = true

  try {
    // Replace this with your actual API call
    await new Promise((resolve) => setTimeout(resolve, 1500))
    showSuccess.value = true
    setTimeout(() => showSuccess.value = false, 5000)
  } catch (err) {
    console.error('Save failed:', err)
    alert('Failed to save settings. Please try again.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>