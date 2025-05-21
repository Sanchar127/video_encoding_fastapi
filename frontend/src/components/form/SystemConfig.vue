<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50"
  >
    <div class="bg-white rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200 transition-all">
      <h3 class="text-2xl font-bold text-gray-800 mb-6">{{ title }}</h3>
      <form @submit.prevent="handleSubmit" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-600 mb-1">Key</label>
          <input
            v-model="form.config_key"
            type="text"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
            required
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-600 mb-1">Value</label>
          <input
            v-model="form.value"
            readonly
            type="text"
            class="w-full px-4 py-2 border border-gray-200 bg-gray-100 rounded-lg text-gray-700 cursor-not-allowed"
            required
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-600 mb-1">Updated By</label>
          <input
            v-model="form.updated_by"
            type="text"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
            required
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-600 mb-1">Description</label>
          <input
            v-model="form.description"
            type="text"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
            required
          />
        </div>

        <div class="pt-4 flex justify-end space-x-3">
          <button
            type="button"
            @click="$emit('close')"
            class="px-4 py-2 text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-lg border"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="px-4 py-2 text-white bg-blue-600 hover:bg-blue-700 rounded-lg shadow-md"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, watch, defineProps, defineEmits, computed } from 'vue'

const props = defineProps<{
  visible: boolean
  title?: string
  initialData?: {
    config_key: string
    value: string
    updated_by: string
    description: string
  }
}>()

const emit = defineEmits(['submit', 'close'])

const form = reactive({
  config_key: '',
  value: '',
  updated_by: '',
  description: '',
})

const isEditMode = computed(() => !!props.initialData)

watch(
  () => props.initialData,
  (newVal) => {
    if (newVal) {
      form.config_key = newVal.config_key
      form.value = newVal.value
      form.updated_by = newVal.updated_by
      form.description = newVal.description
    }
  },
  { immediate: true }
)

const handleSubmit = () => {
  emit('submit', { ...form })
}
</script>
