<template>
  <div class="mb-8 flex justify-between items-center">
    <div>
      <h1 class="text-3xl md:text-4xl font-bold text-gray-800">{{ title }}</h1>
      <p class="text-gray-500 mt-1">{{ subtitle }}</p>
    </div>
 
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'Admin Dashboard'
    },
    subtitle: {
      type: String,
      default: 'Welcome back! Here\'s what\'s happening today.'
    },
    showLiveBadge: {
      type: Boolean,
      default: true
    }
  }
}
</script>