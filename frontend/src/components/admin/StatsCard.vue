<template>
  <router-link
    :to="link"
    class="block rounded-xl p-6 cursor-pointer
           bg-gradient-to-tr from-indigo-100 via-purple-100 to-pink-100
           shadow-md hover:shadow-lg
           transform hover:scale-105 transition-transform duration-300 border border-transparent hover:border-purple-300"
  >
    <div class="flex items-center space-x-5">
      <div
        class="flex items-center justify-center w-14 h-14 rounded-full
               bg-gradient-to-br from-yellow-200 via-pink-200 to-red-200
               shadow-inner text-pink-600 text-2xl"
      >
        <slot name="icon" />
      </div>

      <div class="flex flex-col">
        <p
          class="text-sm font-semibold text-purple-700 uppercase tracking-wide"
        >
          {{ title }}
        </p>
        <p
          class="mt-1 text-3xl font-bold text-purple-900"
        >
          {{ value }}
          <span
            class="block h-1 w-12 rounded-full mt-2
                   bg-pink-300 transition-all duration-300"
          ></span>
        </p>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    value: {
      type: [String, Number],
      required: true,
    },
    link: {
      type: String,
      required: true,
    },
  },
};
</script>
