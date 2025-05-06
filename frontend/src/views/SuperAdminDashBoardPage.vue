<template>
    <div class="min-h-screen bg-gray-100 p-6">
      <h1 class="text-3xl font-bold mb-6 text-center text-gray-800">
        Super Admin Dashboard
      </h1>
  
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <DashboardCard title="Create User" icon="👤" />
        <DashboardCard title="Update User" icon="🔄" />
        <DashboardCard title="Create Encode Profile" icon="🛠️" />
        <DashboardCard title="Update Encode Profile" icon="⚙️" />
        <DashboardCard title="Create Encode Profile Details" icon="➕" />
        <DashboardCard title="Update Encode Profile Details" icon="✏️" />
        <DashboardCard title="Manage Jobs" icon="📂" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    components: {
      DashboardCard: {
        props: ['title', 'icon'],
        template: `
          <div class="bg-white shadow rounded-xl p-6 hover:shadow-md transition cursor-pointer text-center">
            <div class="text-4xl mb-2">{{ icon }}</div>
            <h2 class="text-xl font-semibold text-gray-700">{{ title }}</h2>
          </div>
        `
      }
    }
  }
  </script>
  
  <style scoped>
  /* Optional custom styles */
  </style>
  