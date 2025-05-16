<template>
  <router-link :to="link">
    <button @click="onClick" class="w-full flex items-center justify-between px-5 py-3 rounded-lg transition-all duration-200 transform hover:-translate-y-0.5 shadow-sm hover:shadow-md" :class="buttonClasses">
      <span class="font-medium">{{ title }}</span>
      <slot name="icon"></slot>
    </button>
  </router-link>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    link: {
      type: String,
      required: true
    },
    bgColor: {
      type: String,
      default: 'bg-blue-50'
    },
    textColor: {
      type: String,
      default: 'text-blue-700'
    },
    hoverBgColor: {
      type: String,
      default: 'hover:bg-blue-100'
    },
    onClick: {
      type: Function,
      default: () => {}
    }
  },
  computed: {
    buttonClasses() {
      return `${this.bgColor} ${this.textColor} ${this.hoverBgColor}`;
    }
  }
}
</script>