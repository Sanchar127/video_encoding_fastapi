
<template>
  <DefaultLayout>
    <div class="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
      <h1 class="text-3xl font-bold mb-6 text-center">Login</h1>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <div class="relative">
            <EmailIcon class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
            <input
              v-model="email"
              type="email"
              id="email"
              class="mt-1 block w-full pl-10 pr-4 py-2 border border-gray-300 rounded focus:ring focus:ring-blue-300"
              placeholder="you@example.com"
              required
            />
          </div>
          <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
        </div>

        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded focus:ring focus:ring-blue-300"
            placeholder="••••••••"
            required
          />
          <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition duration-300"
        >
          Login
        </button>
      </form>
    </div>
  </DefaultLayout>
</template>
<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import Cookies from 'js-cookie';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    const toast = useToast();

    const handleSubmit = async () => {
      try {
        const formData = new URLSearchParams();
        formData.append('username', email.value);
        formData.append('password', password.value);

        const response = await axios.post('http://localhost:8084/token', formData, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        });
        console.log('Login token:', response.data.access_token); 
        console.log('User role :',response.data.role)
        // Save token in cookie (not HttpOnly so JS can read it)
        Cookies.set('access_token', response.data.access_token);


        toast.success('Login successful!');
        router.push('/user/manage');
      } catch (error: any) {
        toast.error('Login failed: ' + (error.response?.data?.detail || error.message));
      }
    };

    return { email, password, handleSubmit };
  },
};
</script>

