<template>
    <div>
      <Navbar />
      <main>
        <slot></slot> <!-- Content will be injected here -->
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
  
  <style scoped>
  /* Add any layout-specific styles here */
  </style>
  