<template>
  <div class="flex flex-col gap-3 w-full mt-2">
    <!-- Create Encode Profile -->
    <router-link to="/encodeProfiles" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-blue-50"
      >
        <p class="text-base font-medium text-gray-800">
          Create Encode Profile
        </p>
      </div>
    </router-link>

    <!-- Edit Encode Profiles -->
    <router-link to="/edit/profile" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-purple-50"
      >
        <p class="text-base font-medium text-gray-800">
          Edit Encode Profiles
        </p>
      </div>
    </router-link>
  </div>
</template>

<script setup>

</script>
