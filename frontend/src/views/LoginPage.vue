<template>

    <div class="max-w-md mx-auto mt-20 p-6 bg-white rounded shadow">
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
              class="mt-1 block w-full pl-10 pr-4 py-2 border border-gray-100 rounded focus:ring focus:ring-gray-50"
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
            class="mt-1 block w-full pl-10 pr-4 py-2 border border-gray-100 rounded focus:ring focus:ring-gray-50"
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

</template>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import DefaultLayout from '@/layout/DefaultLayout.vue';
import EmailIcon from '@/components/icons/EmailIcon.vue';
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'



export default {
  components: {
    DefaultLayout,
    EmailIcon,
  },
  setup() {
  const email = ref('');
  const password = ref('');
  const emailError = ref('');
  const passwordError = ref('');
  const apiUrl = 'http://localhost:8084/token';

  const router = useRouter(); 
  const toast = useToast();  

  const validate = () => {
    emailError.value = '';
    passwordError.value = '';
    let isValid = true;

    if (!email.value) {
      emailError.value = 'Email is required.';
      isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email.value)) {
      emailError.value = 'Invalid email format.';
      isValid = false;
    }

    if (!password.value) {
      passwordError.value = 'Password is required.';
      isValid = false;
    }

    return isValid;
  };

  const handleSubmit = async () => {
    if (!validate()) return;

    try {
      const formData = new URLSearchParams();
      formData.append('username', email.value);
      formData.append('password', password.value);

      const response = await axios.post(apiUrl, formData, {
        headers: {
          
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      console.log('Login successful:', response.data);
      toast.success('Login successfully!');
      // router.push('/');
      localStorage.setItem('access_token', response.data.access_token);

    } catch (error: any) {
      console.error('Login failed:', error.response?.data?.detail || error.message);
      toast.error('Failed to create user: ' + (error.response?.data?.detail || error.message));
    }
  };

  return {
    email,
    password,
    emailError,
    passwordError,
    handleSubmit,
  };


  },
};
</script>