<template>
  <nav class="bg-white text-slate-800 shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
     
      <div class="flex items-center space-x-2">
        <span class="text-2xl font-bold">FastEncoder</span>
      </div>

      
      <button
        @click="isOpen = !isOpen"
        class="lg:hidden text-slate-800 focus:outline-none"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          ></path>
        </svg>
      </button>


      <div class="hidden lg:block absolute left-1/2 transform -translate-x-1/2 w-full max-w-md">
        <div class="relative">
          <SearchIcons class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" />
          <input
            type="text"
            placeholder="Search..."
            class="w-full pl-12 pr-4 py-2 rounded-full text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-100"
          />
        </div>
      </div>

      <!-- Auth Buttons (Right) -->
      <div class="hidden lg:flex space-x-4 items-center">
        <template v-if="isAuthenticated">
          <button
            @click="logout"
            class="bg-red-600 text-white px-4 py-2 rounded-full hover:bg-red-700 transition"
          >
            Logout
          </button>
        </template>
        <template v-else>
          <router-link
            to="/"
            class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition"
          >
            Sign In
          </router-link>
        </template>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isOpen" class="lg:hidden px-4 pb-4">
      <div class="mb-3">
        <div class="relative">
          <SearchIcons class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" />
          <input
            type="text"
            placeholder="Search..."
            class="w-full pl-12 pr-4 py-2 rounded-full text-sm border border-gray-300 focus:outline-none focus:ring-2 focus:ring-red-100"
          />
        </div>
      </div>
      <div class="flex flex-col space-y-3">
        <template v-if="isAuthenticated">
          <button
            @click="logout"
            class="bg-red-600 text-white px-4 py-2 rounded-full hover:bg-red-700 transition"
          >
            Logout
          </button>
        </template>
        <template v-else>
          <router-link
            to=""
            class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition"
          >
            Sign In
          </router-link>
        </template>
      </div>
    </div>
  </nav>
</template>



<script>
import SearchIcons from './icons/SearchIcons.vue';
import Cookies from 'js-cookie';
import axios from 'axios';
import { useToast } from 'vue-toastification'
const apiurl='http://localhost:8084'
export default {
  name: 'Navbar',
  components: {
    SearchIcons,
  },
  data() {
    return {
      isAuthenticated: !!Cookies.get('access_token'),
    };
  },

methods: {
  async logout() {
    try {
      const accessToken = Cookies.get('access_token');

      if (!accessToken) {
        console.warn('No access token found in cookies.');
        return;
      }

      await axios.post(
            `${apiurl}/logout`,
        {},
        {
          headers: {
            Authorization: `Bearer ${accessToken}`, 
          },
          withCredentials: true, 
        }
      );

      this.isAuthenticated = false;
      this.$router.push('/');
      toast.success('Logout successful!');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  }
}

};
</script>
