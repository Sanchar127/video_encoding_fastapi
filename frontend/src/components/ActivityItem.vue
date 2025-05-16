<template>
  <div class="flex items-start py-3 border-b border-gray-100 last:border-0">
    <div class="flex-shrink-0 w-2.5 h-2.5 rounded-full mt-1.5" :class="dotColor"></div>
    <div class="ml-3">
      <p class="text-sm text-gray-800">{{ activity.description }}</p>
      <p class="text-xs text-gray-500 mt-1">{{ activity.time }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    activity: {
      type: Object,
      required: true
    },
    dotColor: {
      type: String,
      default: 'bg-blue-500'
    }
  }
}
</script>