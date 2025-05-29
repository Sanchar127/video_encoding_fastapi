<template>
  <div v-if="open" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-3xl shadow-2xl w-full max-w-6xl p-10 overflow-y-auto max-h-[90vh]">
      <h2 class="text-3xl font-bold text-gray-800 text-center mb-10">
        {{ isEditing ? 'Edit Encode Profile' : 'Create Encode Profile' }}
      </h2>

      <form @submit.prevent="submitForm" class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Profile Section -->
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Profile Name</label>
          <input v-model="form.profile" type="text" required
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Width</label>
          <input v-model.number="form.width" type="number" required min="1"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Height</label>
          <input v-model.number="form.height" type="number" required min="1"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Video Bitrate (kbps)</label>
          <input v-model.number="form.video_bitrate" type="number" required min="100"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Max Bitrate (kbps)</label>
          <input v-model.number="form.max_bitrate" type="number" min="0"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Video Codec</label>
          <select v-model="form.vcodec" required
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200">
            <option value="libx264">H.264 (libx264)</option>

          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Pixel Format</label>
          <select v-model="form.pix_fmt" required
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200">
            <option value="yuv420p">yuv420p</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Audio Bitrate (kbps)</label>
          <input v-model.number="form.audio_bitrate" type="number" required min="32"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Audio Channels</label>
          <input v-model.number="form.audio_channel" type="number" required min="1" max="8"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Audio Frequency (Hz)</label>
          <input v-model.number="form.audio_frequency" type="number" required min="8000" max="192000"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Audio Codec</label>
          <select v-model="form.acodec" required
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200">
            <option value="aac">AAC</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Force Format</label>
          <select v-model="form.force_format" required
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200">
            <option value="mp4">MP4</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">MOV Flags</label>
          <input v-model="form.movflags" type="text" placeholder="e.g., faststart"
            class="w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-200" />
        </div>

        <!-- Buttons -->
        <div class="md:col-span-2 flex justify-end gap-4 mt-8">
          <button type="button" @click="$emit('close')"
            class="px-6 py-2 rounded-xl border border-gray-300 bg-white text-gray-700 hover:bg-gray-100 transition duration-200 shadow">
            Cancel
          </button>
          <button type="submit"
            class="px-6 py-2 rounded-xl bg-purple-600 text-white font-semibold hover:bg-purple-700 transition duration-200 shadow">
            {{ isEditing ? 'Update Profile' : 'Create Profile' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>



<script setup lang="ts">
import { ref, watch } from 'vue'

// Props
const props = defineProps<{
  open: boolean
  isEditing: boolean
  profileData: {
    id?: string
    profile?: string
    width?: number
    height?: number
    video_bitrate?: number
    max_bitrate?: number
    audio_bitrate?: number
    audio_channel?: number
    audio_frequency?: number
    sc_threshold?: number
    level?: number
    bufsize?: number
    movflags?: string
    pix_fmt?: string
    force_format?: string
    acodec?: string
    vcodec?: string
  }
}>()

const emit = defineEmits<{
  (e: 'submit', value: typeof form.value): void
  (e: 'close'): void
}>()

// Form state
const form = ref({
  profile_id: 0,
  profile: '',
  width: 0,
  height: 0,
  video_bitrate: 0,
  max_bitrate: 0,
  audio_bitrate: 0,
  audio_channel: 0,
  audio_frequency: 0,
  sc_threshold: 0,
  level: 3.0,
  bufsize: 0,
  movflags: '',
  pix_fmt: 'yuv420p',
  force_format: 'mp4',
  acodec: 'aac',
  vcodec: 'libx264'
})


const inputTypes: Record<string, string> = {
  width: 'number',
  height: 'number',
  video_bitrate: 'number',
  max_bitrate: 'number',
  audio_bitrate: 'number',
  audio_channel: 'number',
  audio_frequency: 'number',
  sc_threshold: 'number',
  level: 'number',
  bufsize: 'number',
  movflags: 'text'
}

const fields: Record<string, string> = {
  width: 'Width',
  height: 'Height',
  video_bitrate: 'Video Bitrate (kbps)',
  max_bitrate: 'Max Bitrate (kbps)',
  audio_bitrate: 'Audio Bitrate (kbps)',
  audio_channel: 'Audio Channels',
  audio_frequency: 'Audio Frequency (Hz)',
  sc_threshold: 'Scene Cut Threshold',
  level: 'Encoding Level',
  bufsize: 'Buffer Size',
  movflags: 'MOV Flags'
}

// Sync prop updates into form
watch(() => props.profileData, (newVal) => {
  if (newVal) {
    form.value = {
      ...form.value,
      ...newVal,
      profile_id: newVal.id ? parseInt(newVal.id) : 0,
      width: newVal.width || 0,
      height: newVal.height || 0,
      video_bitrate: newVal.video_bitrate || 0,
      max_bitrate: newVal.max_bitrate || 0,
      audio_bitrate: newVal.audio_bitrate || 0,
      audio_channel: newVal.audio_channel || 0,
      audio_frequency: newVal.audio_frequency || 0,
      sc_threshold: newVal.sc_threshold || 0,
      level: newVal.level || 3.0,
      bufsize: newVal.bufsize || 0,
      movflags: newVal.movflags || '',
      pix_fmt: newVal.pix_fmt || 'yuv420p',
      force_format: newVal.force_format || 'mp4',
      acodec: newVal.acodec || 'aac',
      vcodec: newVal.vcodec || 'libx264'
    }
  }
}, { immediate: true, deep: true })

// Form submission with validation
const submitForm = () => {
  const validProfiles = ['high', 'main', 'baseline'];
  const {
    profile, width, height, video_bitrate, audio_bitrate, audio_channel,
    audio_frequency, level, pix_fmt, acodec, vcodec, force_format
  } = form.value;

  if (!validProfiles.includes(profile)) {
    alert('Profile must be "high", "main", or "baseline"');
    return;
  }

  if (width <= 0 || height <= 0) {
    alert('Width and height must be positive integers');
    return;
  }

  if (video_bitrate < 100) {
    alert('Video bitrate must be at least 100 kbps');
    return;
  }

  if (audio_bitrate < 32) {
    alert('Audio bitrate must be at least 32 kbps');
    return;
  }

  if (audio_channel < 1 || audio_channel > 8) {
    alert('Audio channels must be between 1 and 8');
    return;
  }

  const freq = parseInt(audio_frequency as unknown as string, 10);
  if (isNaN(freq) || freq < 8000 || freq > 192000) {
    alert('Audio frequency must be between 8000 and 192000 Hz');
    return;
  }

  if (level < 3.0 || level > 4.1) {
    alert('Level must be between 3.0 and 4.1');
    return;
  }

  if (pix_fmt !== 'yuv420p') {
    alert('Only "yuv420p" pixel format is supported');
    return;
  }

  if (acodec !== 'aac') {
    alert('Only "aac" audio codec is supported');
    return;
  }

  if (vcodec !== 'libx264') {
    alert('Only "libx264" video codec is supported');
    return;
  }

  if (force_format !== 'mp4') {
    alert('Only "mp4" container format is supported');
    return;
  }

  emit('submit', form.value);
}
</script>
