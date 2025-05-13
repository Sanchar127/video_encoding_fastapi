<template>
  <div class="flex flex-col gap-3 w-full mt-2">
    <!-- Create Encode Profile Details -->
    <router-link to="/new/EncodeProfileDetails" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-blue-50"
      >
        <p class="text-base font-medium text-gray-800">
          Create Encode Profile Details
        </p>
      </div>
    </router-link>

    <!-- Edit Encode Profiles Details -->
    <router-link to="/edit/EncodeProfilesDetails" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-purple-50"
      >
        <p class="text-base font-medium text-gray-800">
          Edit Encode Profiles Details
        </p>
      </div>
    </router-link>
  </div>
</template>

<script setup>
// No script logic needed
</script>
