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
      default: ' Dashboard'
    },
    subtitle: {
      type: String,
      default: ''
    },
    showLiveBadge: {
      type: Boolean,
      default: true
    }
  }
}
</script>