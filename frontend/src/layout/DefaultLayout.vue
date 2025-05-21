<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />

    <!-- Desktop layout -->
    <div class="hidden md:flex flex-1 overflow-hidden">
      <aside class="w-64 p-4 bg-gray-50 overflow-y-auto border-r border-gray-200">
        <AdmindashItems />
        <SuperAdashitem v-if="isSuperAdmin" />
      </aside>
      <main class="flex-1 overflow-y-auto p-4">
        <slot />
      </main>
    </div>

    <!-- Mobile layout -->
    <div class="md:hidden flex-1 relative">
      <!-- Hamburger Button -->
      <button
        @click="toggleSidebar"
        class="fixed top-10 left-4 z-50 p-3 rounded-full bg-white shadow-md text-gray-800 hover:bg-gray-100 hover:shadow-lg transition duration-300 focus:outline-none"
        aria-label="Toggle Sidebar"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      <!-- Sidebar Drawer -->
      <div v-if="showSidebar" class="fixed inset-0 z-40 flex">
        <div class="w-64 bg-gray-50 border-r border-gray-200 p-4 h-full">
          <button
            @click="toggleSidebar"
            class="mb-4 text-gray-600 hover:text-black"
          >
            ✕ Close
          </button>
          <AdmindashItems />
          <SuperAdashitem v-if="isSuperAdmin" />
        </div>
        <!-- Backdrop -->
        <div class="flex-1 bg-black bg-opacity-40" @click="toggleSidebar"></div>
      </div>

      <!-- Main Content -->
      <main class="p-4">
        <slot />
      </main>
    </div>

    <Footer />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';

import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import AdmindashItems from '@/components/AdmindashItems.vue';
import SuperAdashitem from '@/components/SuperAdashitem.vue';

interface DecodedToken {
  role: string;
  exp: number;
  sub: string;
}

export default defineComponent({
  components: {
    Navbar,
    Footer,
    AdmindashItems,
    SuperAdashitem,
  },
  setup() {
    const isSuperAdmin = ref(false);
    const showSidebar = ref(false);

    const toggleSidebar = () => {
      showSidebar.value = !showSidebar.value;
    };

    onMounted(() => {
      const token = Cookies.get('access_token');
      if (token) {
        try {
          const decoded = jwtDecode<DecodedToken>(token);
          isSuperAdmin.value = decoded.role === 'super_admin';
        } catch (error) {
          console.error('Failed to decode token:', error);
          isSuperAdmin.value = false;
        }
      }
    });

    return {
      isSuperAdmin,
      showSidebar,
      toggleSidebar,
    };
  },
});
</script>
