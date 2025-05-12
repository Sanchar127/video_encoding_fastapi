<template>
  <div class="max-w-sm mx-auto mt-3 mb-3 space-y-4">
    

    <router-link to="/register">
      <div class="shadow-sm w-2/3 hover:shadow-lg transition rounded-lg px-5 py-2 cursor-pointer border border-gray-200 hover:bg-blue-50 mt-2">
        <p class="text-lg font-medium text-gray-800">Create New User</p>
      </div>
    </router-link>

     <router-link to="/editUser">

       <div class="w-2/3 shadow-sm hover:shadow-lg transition rounded-lg px-5 py-2 cursor-pointer border border-gray-200 hover:bg-purple-50 mt-2">
         <p class="text-lg font-medium text-gray-800">Edit Users</p>
       </div>
     </router-link>

  </div>
</template>

<script setup>
</script>
