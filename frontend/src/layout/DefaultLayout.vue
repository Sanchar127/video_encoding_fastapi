<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <div class="flex flex-1 overflow-hidden">
      <!-- Admin Sidebar -->
      <aside class="w-64 p-4 bg-gray-50 overflow-y-auto border-r border-gray-200">
      <AdmindashItems/>
      <SuperAdashitem/>
      </aside>

      <main class="flex-1 overflow-y-auto p-4">
        <slot />
      </main>
    </div>
    <Footer />
  </div>
</template>

<script lang="ts">
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import AdmindashItems from '../components/AdmindashItems.vue';
import SuperAdashitem from '../components/SuperAdashitem.vue';



export default {
  components: {
    Navbar,
    Footer,
    AdmindashItems,
    SuperAdashitem,
  },
};
</script>
