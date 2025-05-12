<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <main class="flex-1 overflow-y-auto p-4">
      <slot></slot> 
    </main>
    <Footer />
  </div>
</template>

<script lang="ts">
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>
