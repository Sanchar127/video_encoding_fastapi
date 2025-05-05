<template>
  <DefaultLayout>
    <div class="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
      <h1 class="text-3xl font-bold mb-6 text-center">Login Page</h1>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="email"
            type="email"
            id="email"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded focus:ring focus:ring-blue-300"
            placeholder="you@example.com"
          />
          <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
        </div>

        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded focus:ring 
            "
            placeholder="••••••••"
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
import DefaultLayout from '@/layout/DefaultLayout.vue';

export default {
  components: {
    DefaultLayout,
  },
  setup() {
    const email = ref('');
    const password = ref('');
    const emailError = ref('');
    const passwordError = ref('');

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

    const handleSubmit = () => {
      if (validate()) {
        console.log('Logging in:', {
          email: email.value,
          password: password.value,
        });
        // Make API call here
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
