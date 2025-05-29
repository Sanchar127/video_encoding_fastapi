<template>
  <DefaultLayout>
    <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div class="w-full max-w-2xl p-8 bg-white rounded-lg shadow-md">
        <h2 class="text-3xl font-semibold text-gray-800 mb-6 text-center">Create New User</h2>

        <form @submit.prevent="onSubmit" class="space-y-5">
  
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name</label>
              <div class="relative">
                <UserIcon class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                <Field
                  id="name"
                  name="name"
                  type="text"
                  class="w-full pl-10 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <ErrorMessage name="name" class="text-red-500 text-sm mt-1" />
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <div class="relative">
                <EmailIcon class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                <Field
                  id="email"
                  name="email"
                  type="email"
                  class="w-full pl-10 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <ErrorMessage name="email" class="text-red-500 text-sm mt-1" />
            </div>
          </div>

         
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
              <Field
                id="password"
                name="password"
                type="password"
                class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <ErrorMessage name="password" class="text-red-500 text-sm mt-1" />
            </div>

            <div>
              <label for="mobile" class="block text-sm font-medium text-gray-700 mb-1">Mobile</label>
              <div class="relative">
                <MobileIcon class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                <Field
                  id="mobile"
                  name="mobile"
                  type="text"
                  class="w-full pl-10 pr-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <ErrorMessage name="mobile" class="text-red-500 text-sm mt-1" />
            </div>
          </div>

          <!-- Remaining fields -->
          <div v-for="field in fields.slice(4)" :key="field.name">
            <label :for="field.name" class="block text-sm font-medium text-gray-700 mb-1">
              {{ field.label }}
            </label>
            <Field
              v-if="field.type !== 'select'"
              :id="field.name"
              :name="field.name"
              :type="field.type"
              class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <Field
              v-else
              as="select"
              :name="field.name"
              :id="field.name"
              class="w-full px-4 py-2 border rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="" disabled>Select role</option>
              <option value="super_admin">Super Admin</option>
              <option value="admin">Admin</option>
              <option value="user">User</option>
            </Field>
            <ErrorMessage :name="field.name" class="text-red-500 text-sm mt-1" />
          </div>

          <button
            type="submit"
            :disabled="isSubmitting"
            class="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition duration-200 disabled:opacity-50"
          >
            {{ isSubmitting ? 'Submitting...' : 'Submit' }}
          </button>
        </form>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { Field, ErrorMessage, useForm } from 'vee-validate'
import DefaultLayout from '@/layout/DefaultLayout.vue'
import axios from 'axios';
import UserIcon from '@/components/icons/UserIcon.vue'
import EmailIcon from '@/components/icons/EmailIcon.vue'
import MobileIcon from '@/components/icons/MobileIcon.vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import Cookies from 'js-cookie';
import { userSchema } from '../../validation/userFormSchema';


const accessToken = Cookies.get('access_token');

const router = useRouter(); 
const toast = useToast();  

const apiUrl = 'http://localhost:8084/users/create';




const fields = [
  { name: 'name', label: 'Name', type: 'text' },
  { name: 'email', label: 'Email', type: 'email' },
  { name: 'password', label: 'Password', type: 'password' },
  { name: 'mobile', label: 'Mobile', type: 'text' },
  { name: 'address', label: 'Address', type: 'text' },
  { name: 'callback_key', label: 'Callback Key', type: 'text' },
  { name: 'callback_url', label: 'Callback URL', type: 'text' },
  { name: 'callback_secret_key', label: 'Callback Secret Key', type: 'text' },
  { name: 'role', label: 'Role', type: 'select' },
  
]

const { handleSubmit } = useForm({
  validationSchema: userSchema
})

const onSubmit = handleSubmit(async (values) => {
  try {
    const accessToken = Cookies.get('access_token'); 
    console.log(accessToken)
    const response = await axios.post(apiUrl, values, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.status === 200) {
      toast.success('User created successfully!');
      router.push('/user/manage')
    }
  } catch (error: any) {
    const errorMsg = error.response?.data?.detail || error.message;
    toast.error(`Creation failed: ${errorMsg}`);

    if (error.response?.status === 401) {
      router.push('/login');
    }
  }
});



</script>