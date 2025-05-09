<template>
  <div class="flex flex-col gap-5 w-1/2 max-w-sm justify-center items-left">
    
   
    <div>
      <div
        class="bg-sky-100 shadow-sm rounded-lg p-2 hover:shadow-md transition w-1/2 cursor-pointer flex justify-center items-center"
        @click="toggle('users')"
      >
        <h2 class="text-xl font-medium mb-0.5">Manage Users</h2>
        <CevronDownIcon v-if="!show.users" class="w-10 ml-2" />
        <CevronUpIcons v-else class="w-10 ml-2" />
      </div>
      <div v-if="show.users">
        <ManageUser />
      </div>
    </div>

    <div>
      <div
        class="bg-fuchsia-100 shadow-sm rounded-lg p-2 hover:shadow-md transition w-1/2 cursor-pointer flex justify-center items-center"
        @click="toggle('eprofiles')"
      >
        <h2 class="text-xl font-medium mb-0.5">Manage Encode Profiles</h2>
        <CevronDownIcon v-if="!show.eprofiles" class="w-10 ml-2" />
        <CevronUpIcons v-else class="w-10 ml-2" />
      </div>
      <div v-if="show.eprofiles">
        <ManageEprofile />
      </div>
    </div>

    <div>
      <div
        class="bg-violet-100 shadow-sm rounded-lg p-2 hover:shadow-md transition w-1/2 cursor-pointer flex justify-center items-center"
        @click="toggle('eprofileDetails')"
      >
        <h2 class="text-xl font-medium mb-0.5">Manage Encode Profile Details</h2>
        <CevronDownIcon v-if="!show.eprofileDetails" class="w-10 ml-2" />
        <CevronUpIcons v-else class="w-10 ml-2" />
      </div>
      <div v-if="show.eprofileDetails">
        <ManageEprofileDetails />
      </div>
    </div>

    <!-- Manage Jobs -->
    <div>
      <div
        class="bg-rose-50 shadow-sm rounded-lg p-2 hover:shadow-md transition w-1/2 cursor-pointer flex justify-center items-center"
        @click="toggle('jobs')"
      >
        <h2 class="text-xl font-medium mb-0.5">Manage Jobs</h2>
        <CevronDownIcon v-if="!show.jobs" class="w-10 ml-2" />
        <CevronUpIcons v-else class="w-10 ml-2" />
      </div>
      <div v-if="show.jobs">
        <ManageJob />
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">
import ManageEprofile from './ManageEprofile.vue';
import ManageEprofileDetails from './ManageEprofileDetails.vue';
import ManageJob from './ManageJob.vue';
import ManageUser from './ManageUser.vue';
import CevronDownIcon from './icons/CevronDownIcon.vue';
import { reactive } from 'vue';
import CevronUpIcons from './icons/CevronUpIcons.vue';

const show = reactive({
  users: false,
  eprofiles: false,
  eprofileDetails: false,
  jobs: false,
});

function toggle(section: keyof typeof show) {
  show[section] = !show[section];
}
</script>