<template>
  <nav class="bg-gradient-to-r from-blue-900 to-purple-900 text-white shadow-lg sticky top-0 z-50 ">
    <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center">
        <span class="text-2xl font-bold">VideoEncoder</span>
      </div>
      <div class="flex space-x-6 items-center">
        <router-link to="/login" class="bg-blue-600 px-4 py-2 rounded-full hover:bg-blue-700 transition">
          Sign In
        </router-link>
        <router-link to="/register" class="bg-purple-600 px-4 py-2 rounded-full hover:bg-purple-700 transition">
          Register
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>
