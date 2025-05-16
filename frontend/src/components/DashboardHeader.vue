<template>
  <div class="mb-8 flex justify-between items-center">
    <div>
      <h1 class="text-3xl md:text-4xl font-bold text-gray-800">{{ title }}</h1>
      <p class="text-gray-500 mt-1">{{ subtitle }}</p>
    </div>
    <div v-if="showLiveBadge" class="hidden md:block">
      <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
        <span class="w-2 h-2 mr-2 rounded-full bg-blue-500 animate-pulse"></span>
        Live Data
      </span>
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