<template>
  <nav class="bg-white text-slate-800 shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 py-3 relative flex justify-between items-center">
      
      <!-- Logo (Left) -->
      <div class="flex items-center space-x-2">
        <span class="text-2xl font-bold">VideoEncoder</span>
      </div>

      <div class="absolute left-1/2 transform -translate-x-1/2">
  <div class="relative">
    <SearchIcons class="absolute left-4 top-1/2 -translate-y-1/2 w-6 h-6 text-gray-400 pointer-events-none" />
    <input
      type="text"
      placeholder="Search..."
      class="pl-12 pr-4 py-3 w-96 rounded-full text-base border border-gray-300 focus:outline-none focus:ring-2 focus:ring-red-100"
    />
  </div>
</div>

      <!-- Auth Buttons (Right) -->
      <div class="flex space-x-6 items-center">
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
            to="/login"
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

export default {
  name: 'Navbar',
  components: {
    SearchIcons,
  },
  data() {
    return {
      isAuthenticated: !!localStorage.getItem('access_token'),
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.isAuthenticated = false;
      this.$router.push('/login');
    },
  },
};
</script>
