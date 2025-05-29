
<template>
  <DefaultLayout>
   <div class="max-w-md mx-auto mt-20 p-8 bg-white rounded-xl shadow-lg backdrop-blur-sm bg-opacity-90">
  <div class="text-center mb-8">
    
    <p class="text-gray-500 mt-2 font-bold">Sign in to your account to continue</p>
  </div>

  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div class="space-y-2">
      <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
      <div class="relative">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        </div>
        <input
          v-model="email"
          type="email"
          id="email"
          class="block w-full pl-10 pr-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-100 focus:border-blue-500 transition duration-200"
          placeholder="you@example.com"
          required
          @focus="emailError = ''"
        />
      </div>
      <p v-if="emailError" class="text-red-500 text-sm mt-1 animate-fade-in">{{ emailError }}</p>
    </div>

    <div class="space-y-2">
      <div class="flex justify-between items-center">
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
     
      </div>
      <div class="relative">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <input
          v-model="password"
          type="password"
          id="password"
          class="block w-full pl-10 pr-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-100 focus:border-blue-500 transition duration-200"
          placeholder="••••••••"
          required
          @focus="passwordError = ''"
        />
      </div>
      <p v-if="passwordError" class="text-red-500 text-sm mt-1 animate-fade-in">{{ passwordError }}</p>
    </div>

  

    <button
      type="submit"
      class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white py-3 px-4 rounded-lg font-medium hover:from-blue-600 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition duration-200 transform hover:-translate-y-0.5 shadow-md"
    >
      Sign in
    </button>
    <button
    @click="handleGoogleLogin"
    class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
  >
    Continue with Google
  </button>
  </form>

  
</div>
  </DefaultLayout>
</template>
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';

const email = ref('');
const password = ref('');
const emailError = ref('');
const passwordError = ref('');
const router = useRouter();
const toast = useToast();

interface DecodedToken {
  sub: string;
  role: string;
  exp: number;
}

onMounted(() => {
  const token = Cookies.get('access_token');
  if (token) {
    router.push('/admin/dashboard');
  }
});

const handleSubmit = async () => {
  try {
    const formData = new URLSearchParams();
    formData.append('username', email.value);
    formData.append('password', password.value);

    const response = await axios.post('http://localhost:8084/token', formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });

    const token = response.data.access_token;
    Cookies.set('access_token', token, { path: '/' });

    const decoded: DecodedToken = jwtDecode(token);
    const role = decoded.role;

    toast.success('Login successful!');

    if (role === 'super_admin') {
      router.push('/superadmin/dashboard');
    } else if (role === 'admin') {
      router.push('/admin/dashboard');
    } else {
      router.push('/jobList');
    }
  } catch (error: any) {
    toast.error('Login failed: ' + (error.response?.data?.detail || error.message));
  }
};

const handleGoogleLogin = () => {
  window.location.href = 'http://localhost:8084/login/google';
};
</script>
