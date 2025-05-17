<template>
  <router-link :to="to" custom v-slot="{ navigate, isActive }">
    <div
      @click="handleClick(navigate)"
      class="rounded-xl p-4 flex items-center justify-between shadow-sm cursor-pointer transition-colors"
      :class="[
        isActive || active ? 'bg-red-100 text-gray-800' : 'bg-white text-gray-700',
        'hover:bg-gray-100'
      ]"
    >
      <div class="flex items-center gap-2">
        <component :is="icon" class="w-5 h-5" />
        <span class="text-base font-semibold">{{ title }}</span>
      </div>

      <component
        v-if="collapsible"
        :is="open ? ChevronUpIcon : ChevronDownIcon"
        class="w-5 h-5"
      />
    </div>
  </router-link>

  <transition name="fade">
    <div v-if="collapsible && open">
      <slot />
    </div>
  </transition>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/solid';

const props = defineProps<{
  title: string;
  icon: any;
  to: string;
  active?: boolean;
  collapsible?: boolean;
  open?: boolean;
}>();

const emit = defineEmits(['toggle', 'activate']);

const handleClick = (navigate: Function) => {
  emit('activate');
  if (props.collapsible) emit('toggle');
  navigate();
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
