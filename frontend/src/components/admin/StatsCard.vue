<template>
  <div class="bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow duration-300 p-6 border border-gray-100">
    <div class="flex items-center">
      <div class="p-3 rounded-full" :class="[iconBgColor, iconColor] + ' shadow-inner'">
        <slot name="icon"></slot>
      </div>
      <router-link :to="link">
        <div class="ml-4">
          <p class="text-sm font-medium text-gray-500">{{ title }}</p>
          <p class="text-2xl font-semibold text-gray-800 mt-1">{{ value }}</p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    value: {
      type: [String, Number],
      required: true
    },
    link: {
      type: String,
      required: true
    },
    iconBgColor: {
      type: String,
      default: 'bg-blue-50'
    },
    iconColor: {
      type: String,
      default: 'text-blue-600'
    }
  }
}
</script>