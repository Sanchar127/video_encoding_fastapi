<template>
  <div class="flex flex-col gap-3 w-full mt-2">
    <!-- Retry Failed Job -->
    <router-link to="/job/jobList" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-green-50"
      >
        <p class="text-base font-medium text-gray-800">View All Jobs</p>
      </div>
    </router-link>

    <!-- View All Jobs -->
    <!-- <router-link to="/job/all" class="w-full">
      <div
        class="shadow-sm hover:shadow-md transition rounded-lg px-4 py-2 cursor-pointer border border-gray-200 hover:bg-purple-50"
      >
        <p class="text-base font-medium text-gray-800"</p>
      </div>
    </router-link> -->
  </div>
</template>

<script setup>
// No script logic needed
</script>
