<template>
  <div class="flex flex-col gap-3 w-full mt-2">
    <!-- Create New User -->
    <router-link to="/user/new" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-blue-50"
      >
        <p class="text-base font-medium text-gray-800">Create New User</p>
      </div>
    </router-link>

    <!-- Edit Users -->
    <router-link to="/editUser" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-purple-50"
      >
        <p class="text-base font-medium text-gray-800">Edit Users</p>
      </div>
    </router-link>
  </div>
</template>

<script setup>
// No script logic needed for basic navigation
</script>
