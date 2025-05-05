<template>
  <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Create Your Account
      </h2>
      <p class="mt-2 text-center text-sm text-gray-600">
        Join our platform to access powerful features
      </p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form @submit.prevent="register" class="space-y-6" novalidate>
          <!-- Personal Information Section -->
          <div class="space-y-4 border-b border-gray-200 pb-6">
            <h3 class="text-lg font-medium text-gray-900">Personal Information</h3>
            
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700">Full Name</label>
              <div class="mt-1 relative">
                <input
                  id="name"
                  v-model="name"
                  type="text"
                  placeholder="John Doe"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.name ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.name" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.name" class="mt-2 text-sm text-red-600">{{ errors.name }}</p>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email Address</label>
              <div class="mt-1 relative">
                <input
                  id="email"
                  v-model="email"
                  type="email"
                  placeholder="john@example.com"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.email ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.email" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.email" class="mt-2 text-sm text-red-600">{{ errors.email }}</p>
            </div>

            <div>
              <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
              <div class="mt-1 relative">
                <input
                  id="password"
                  v-model="password"
                  type="password"
                  placeholder="••••••••"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.password ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.password" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.password" class="mt-2 text-sm text-red-600">{{ errors.password }}</p>
              <p class="mt-2 text-xs text-gray-500">At least 8 characters with a mix of letters and numbers</p>
            </div>

            <div>
              <label for="mobile" class="block text-sm font-medium text-gray-700">Mobile Number</label>
              <div class="mt-1 relative">
                <input
                  id="mobile"
                  v-model="mobile"
                  type="tel"
                  placeholder="+1 (555) 123-4567"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.mobile ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.mobile" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.mobile" class="mt-2 text-sm text-red-600">{{ errors.mobile }}</p>
            </div>

            <div>
              <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
              <div class="mt-1 relative">
                <input
                  id="address"
                  v-model="address"
                  type="text"
                  placeholder="123 Main St, City, Country"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.address ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.address" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.address" class="mt-2 text-sm text-red-600">{{ errors.address }}</p>
            </div>
          </div>

          <!-- Integration Settings Section -->
          <div class="space-y-4 border-b border-gray-200 pb-6">
            <h3 class="text-lg font-medium text-gray-900">Integration Settings</h3>
            
            <div>
              <label for="callback_key" class="block text-sm font-medium text-gray-700">Callback Key</label>
              <div class="mt-1 relative">
                <input
                  id="callback_key"
                  v-model="callback_key"
                  type="text"
                  placeholder="your_callback_key"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.callback_key ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.callback_key" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.callback_key" class="mt-2 text-sm text-red-600">{{ errors.callback_key }}</p>
            </div>

            <div>
              <label for="callback_url" class="block text-sm font-medium text-gray-700">Callback URL</label>
              <div class="mt-1 relative">
                <input
                  id="callback_url"
                  v-model="callback_url"
                  type="url"
                  placeholder="https://your-callback-url.com"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.callback_url ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.callback_url" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.callback_url" class="mt-2 text-sm text-red-600">{{ errors.callback_url }}</p>
            </div>

            <div>
              <label for="callback_secret_key" class="block text-sm font-medium text-gray-700">Callback Secret Key</label>
              <div class="mt-1 relative">
                <input
                  id="callback_secret_key"
                  v-model="callback_secret_key"
                  type="password"
                  placeholder="••••••••"
                  :class="['block w-full px-4 py-3 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 border', 
                          errors.callback_secret_key ? 'border-red-300' : 'border-gray-300']"
                />
                <div v-if="errors.callback_secret_key" class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  <ExclamationCircleIcon class="h-5 w-5 text-red-500" />
                </div>
              </div>
              <p v-if="errors.callback_secret_key" class="mt-2 text-sm text-red-600">{{ errors.callback_secret_key }}</p>
            </div>
          </div>

          <!-- Role Selection -->
          <div>
            <label for="role" class="block text-sm font-medium text-gray-700">Account Type</label>
            <select
              id="role"
              v-model="role"
              class="mt-1 block w-full pl-3 pr-10 py-3 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 rounded-md shadow-sm"
            >
              <option v-for="roleOption in roleOptions" :key="roleOption.value" :value="roleOption.value">
                {{ roleOption.label }}
              </option>
            </select>
            <p class="mt-2 text-xs text-gray-500">
              {{ roleOptions.find(r => r.value === role)?.description }}
            </p>
          </div>

          <!-- Form Status -->
          <div>
            <div v-if="isSubmitting" class="rounded-md bg-blue-50 p-4">
              <div class="flex">
                <div class="flex-shrink-0">
                  <ArrowPathIcon class="h-5 w-5 text-blue-400 animate-spin" />
                </div>
                <div class="ml-3">
                  <h3 class="text-sm font-medium text-blue-800">Creating your account...</h3>
                </div>
              </div>
            </div>

            <div v-if="success" class="rounded-md bg-green-50 p-4">
              <div class="flex">
                <div class="flex-shrink-0">
                  <CheckCircleIcon class="h-5 w-5 text-green-400" />
                </div>
                <div class="ml-3">
                  <h3 class="text-sm font-medium text-green-800">{{ success }}</h3>
                </div>
              </div>
            </div>

            <div v-if="error" class="rounded-md bg-red-50 p-4">
              <div class="flex">
                <div class="flex-shrink-0">
                  <XCircleIcon class="h-5 w-5 text-red-400" />
                </div>
                <div class="ml-3">
                  <h3 class="text-sm font-medium text-red-800">{{ error }}</h3>
                </div>
              </div>
            </div>
          </div>

          <!-- Submit Button -->
          <div>
            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!isSubmitting">Create Account</span>
              <span v-else class="flex items-center">
                <ArrowPathIcon class="animate-spin -ml-1 mr-2 h-4 w-4" />
                Processing...
              </span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useForm, useField } from 'vee-validate';
import { object, string } from 'yup';
import {
  ExclamationCircleIcon,
  CheckCircleIcon,
  XCircleIcon,
  ArrowPathIcon
} from '@heroicons/vue/24/outline';

// Role options with descriptions
const roleOptions = [
  { 
    value: 'user', 
    label: 'Standard User', 
    description: 'Access to basic encoding features and personal dashboard' 
  },
  { 
    value: 'admin', 
    label: 'Administrator', 
    description: 'Manage users, view analytics, and configure system settings' 
  },
  { 
    value: 'super_admin', 
    label: 'Super Admin', 
    description: 'Full platform control including security settings and API management' 
  }
];

// Form validation schema
const { handleSubmit, errors } = useForm({
  validationSchema: object({
    name: string()
      .required('Full name is required')
      .min(2, 'Name must be at least 2 characters')
      .max(50, 'Name must be less than 50 characters'),
    email: string()
      .email('Please enter a valid email address')
      .required('Email is required'),
    password: string()
      .required('Password is required')
      .min(8, 'Password must be at least 8 characters')
      .matches(
        /^(?=.*[a-zA-Z])(?=.*[0-9])/,
        'Password must contain letters and numbers'
      ),
    mobile: string()
      .required('Mobile number is required')
      .matches(
        /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/,
        'Please enter a valid phone number'
      ),
    address: string()
      .required('Address is required')
      .min(5, 'Address must be at least 5 characters'),
    callback_key: string()
      .required('Callback key is required')
      .min(4, 'Key must be at least 4 characters'),
    callback_url: string()
      .required('Callback URL is required')
      .url('Please enter a valid URL')
      .matches(
        /^https?:\/\//,
        'URL must start with http:// or https://'
      ),
    callback_secret_key: string()
      .required('Secret key is required')
      .min(8, 'Secret key must be at least 8 characters')
  }),
  initialValues: {
    role: 'user'
  }
});

// Form fields
const { value: name } = useField('name');
const { value: email } = useField('email');
const { value: password } = useField('password');
const { value: mobile } = useField('mobile');
const { value: address } = useField('address');
const { value: callback_key } = useField('callback_key');
const { value: callback_url } = useField('callback_url');
const { value: callback_secret_key } = useField('callback_secret_key');
const { value: role } = useField('role');

// Form state
const isSubmitting = ref(false);
const error = ref('');
const success = ref('');

// Submit handler
const register = handleSubmit(async (values) => {
  isSubmitting.value = true;
  error.value = '';
  success.value = '';

  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // In a real app, you would call your API here
    // const response = await api.post('/register', values);
    
    success.value = 'Account created successfully! Redirecting to dashboard...';
    
    // Simulate redirect
    setTimeout(() => {
      // In a real app, you would navigate to the next page
      // router.push('/dashboard');
      isSubmitting.value = false;
    }, 2000);
  } catch (err) {
    error.value = 'Registration failed. Please try again.';
    isSubmitting.value = false;
  }
});
</script>

<style scoped>
/* Custom animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.animate-fade-in {
  animation: fadeIn 0.3s ease-out;
}

/* Smooth transitions for form sections */
.form-section {
  transition: all 0.3s ease;
}
</style>