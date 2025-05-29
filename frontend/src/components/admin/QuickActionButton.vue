<template>
  <router-link :to="link" class="block group">
    <button
      @click="onClick"
      class="w-full flex items-center justify-between gap-4 px-6 py-4 rounded-2xl border transition-all duration-200 transform bg-white hover:-translate-y-1 shadow-sm hover:shadow-lg"
      :class="buttonClasses"
      aria-label="Quick action button"
    >
      <div class="flex items-center gap-3">
        <slot name="icon" />
        <span class="text-base font-semibold">{{ title }}</span>
      </div>
      <svg
        class="w-4 h-4 text-gray-400 group-hover:text-current transition-transform duration-200 transform group-hover:translate-x-1"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
      </svg>
    </button>
  </router-link>
</template>

<script lang="ts" setup>
import { defineProps, computed } from 'vue';

const props = defineProps<{
  title: string;
  link: string;
  bgColor?: string;
  textColor?: string;
  hoverBgColor?: string;
  onClick?: () => void;
}>();

const buttonClasses = computed(() => {
  return `${props.bgColor ?? 'bg-blue-50'} ${props.textColor ?? 'text-blue-700'} ${props.hoverBgColor ?? 'hover:bg-blue-100'} border-gray-200`;
});
</script>