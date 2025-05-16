<template>
  <div class="flex flex-col gap-4 w-full max-w-3xl mx-auto p-4">
    <!-- Dashboard -->
    <router-link 
      to="/admin/dashboard" 
      v-slot="{ navigate, isActive }"
      custom
    >
      <div
        @click="navigate"
        class="rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer flex items-center justify-between"
        :class="isActive ? 'bg-red-100' : 'bg-white'"
      >
        <h2 class="text-lg font-medium" :class="isActive ? 'text-gray-600' : 'text-gray-800'">Dashboard</h2>
        <HomeIcon class="w-5 h-5" :class="isActive ? 'text-red-500' : 'text-blue-700'" />
      </div>
    </router-link>

    <!-- Manage Users -->
    <div>
      <router-link 
        to="/user/manage"
        v-slot="{ navigate, isActive }"
        custom
      >
        <div
          @click="(e) => { navigate(e); toggle('users'); setActive('users'); }"
          class="rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer flex items-center justify-between"
          :class="isActive || activeSection === 'users' ? 'bg-red-100' : 'bg-white'"
        >
          <h2 class="text-lg font-medium" :class="isActive || activeSection === 'users' ? 'text-gray-600' : 'text-gray-800'">Manage Users</h2>
          <component
            :is="show.users ? ChevronUpIcon : ChevronDownIcon"
            class="w-5 h-5"
            :class="isActive || activeSection === 'users' ? 'text-gray-600' : 'text-blue-500'"
          />
        </div>
      </router-link>
      <transition name="fade">
        <div v-if="show.users" class="pl-4 mt-2">
          <ManageUser />
        </div>
      </transition>
    </div>

    <!-- Manage Encode Profiles -->
    <div>
      <router-link 
        to="/profile/manage"
        v-slot="{ navigate, isActive }"
        custom
      >
        <div
          @click="(e) => { navigate(e); toggle('eprofiles'); setActive('eprofiles'); }"
          class="rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer flex items-center justify-between"
          :class="isActive || activeSection === 'eprofiles' ? 'bg-red-100' : 'bg-white'"
        >
          <h2 class="text-lg font-medium" :class="isActive || activeSection === 'eprofiles' ? 'text-gray-600' : 'text-gray-800'">Manage Encode Profiles</h2>
          <component
            :is="show.eprofiles ? ChevronUpIcon : ChevronDownIcon"
            class="w-5 h-5"
            :class="isActive || activeSection === 'eprofiles' ? 'text-gray-600' : 'text-blue-500'"
          />
        </div>
      </router-link>
      <transition name="fade">
        <div v-if="show.eprofiles" class="pl-4 mt-2">
          <ManageEprofile />
        </div>
      </transition>
    </div>

    <!-- Manage Encode Profile Details -->
    <div>
      <router-link 
        to="/ProfileDetails/manage"
        v-slot="{ navigate, isActive }"
        custom
      >
        <div
          @click="(e) => { navigate(e); toggle('eprofileDetails'); setActive('eprofileDetails'); }"
          class="rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer flex items-center justify-between"
          :class="isActive || activeSection === 'eprofileDetails' ? 'bg-red-100' : 'bg-white'"
        >
          <h2 class="text-lg font-medium" :class="isActive || activeSection === 'eprofileDetails' ? 'text-gray-600' : 'text-gray-800'">Encode Profile Details</h2>
          <component
            :is="show.eprofileDetails ? ChevronUpIcon : ChevronDownIcon"
            class="w-5 h-5"
            :class="isActive || activeSection === 'eprofileDetails' ? 'text-gray-600' : 'text-blue-500'"
          />
        </div>
      </router-link>
      <transition name="fade">
        <div v-if="show.eprofileDetails" class="pl-4 mt-2">
          <ManageEprofileDetails />
        </div>
      </transition>
    </div>

    <!-- Manage Jobs -->
    <div>
      <router-link 
        to="/jobList"
        v-slot="{ navigate, isActive }"
        custom
      >
        <div
          @click="(e) => { navigate(e); setActive('job'); }"
          class="rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer flex items-center justify-between"
          :class="isActive || activeSection === 'job' ? 'bg-red-100' : 'bg-white'"
        >
          <h2 class="text-lg font-medium" :class="isActive || activeSection === 'job' ? 'text-gray-600' : 'text-gray-800'">Manage Jobs</h2>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import ManageEprofile from './ManageEprofile.vue';
import ManageEprofileDetails from './ManageEprofileDetails.vue';
import ManageUser from './ManageUser.vue';
import { HomeIcon, ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/outline';
import { reactive, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const show = reactive({
  users: false,
  eprofiles: false,
  eprofileDetails: false,
});

const activeSection = ref('');

// Set initial active section based on current route
onMounted(() => {
  const pathParts = route.path.split('/').filter(Boolean);
  if (pathParts.length > 0) {
    activeSection.value = pathParts[0];
  }
});

function toggle(section: keyof typeof show) {
  // Close other sections when opening a new one
  Object.keys(show).forEach(key => {
    if (key !== section) {
      show[key as keyof typeof show] = false;
    }
  });
  show[section] = !show[section];
}

function setActive(section: string) {
  activeSection.value = section;
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 640px) {
  .max-w-3xl {
    max-width: 100%;
    padding: 1rem;
  }
  h2 {
    font-size: 1rem;
  }
}
</style>