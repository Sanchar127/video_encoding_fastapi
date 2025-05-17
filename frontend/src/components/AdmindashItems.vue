<template>
  <div class="flex flex-col gap-4 w-full max-w-4xl mx-auto px-4 py-6">
    <SidebarSection
      title="Dashboard"
      icon="HomeIcon"
      :to="'/admin/dashboard'"
      :active="activeSection === 'dashboard'"
      @activate="setActive('dashboard')"
    />

    <SidebarSection
      title="Manage Users"
      icon="UserGroupIcon"
      :to="'/user/manage'"
      collapsible
      :open="show.users"
      :active="activeSection === 'users'"
      @toggle="toggle('users')"
      @activate="setActive('users')"
    >
      <ManageUser class="mt-2 ml-4" />
    </SidebarSection>

    <SidebarSection
      title="Manage Encode Profiles"
      icon="AdjustmentsHorizontalIcon"
      :to="'/profile/manage'"
      collapsible
      :open="show.eprofiles"
      :active="activeSection === 'eprofiles'"
      @toggle="toggle('eprofiles')"
      @activate="setActive('eprofiles')"
    >
      <ManageEprofile class="mt-2 ml-4" />
    </SidebarSection>

    <SidebarSection
      title="Encode Profile Details"
      icon="DocumentTextIcon"
      :to="'/ProfileDetails/manage'"
      collapsible
      :open="show.eprofileDetails"
      :active="activeSection === 'eprofileDetails'"
      @toggle="toggle('eprofileDetails')"
      @activate="setActive('eprofileDetails')"
    >
      <ManageEprofileDetails class="mt-2 ml-4" />
    </SidebarSection>

    <SidebarSection
      title="Manage Jobs"
      icon="ClipboardDocumentListIcon"
      :to="'/jobList'"
      :active="activeSection === 'job'"
      @activate="setActive('job')"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import ManageUser from './ManageUser.vue';
import ManageEprofile from './ManageEprofile.vue';
import ManageEprofileDetails from './ManageEprofileDetails.vue';
import SidebarSection from './SidebarSection.vue';

const route = useRoute();
const show = reactive({
  users: false,
  eprofiles: false,
  eprofileDetails: false,
});

const activeSection = ref('');

onMounted(() => {
  const path = route.path;
  if (path.includes('/user')) activeSection.value = 'users';
  else if (path.includes('/profile')) activeSection.value = 'eprofiles';
  else if (path.includes('/ProfileDetails')) activeSection.value = 'eprofileDetails';
  else if (path.includes('/job')) activeSection.value = 'job';
  else activeSection.value = 'dashboard';
});

function toggle(section: keyof typeof show) {
  Object.keys(show).forEach(key => {
    show[key as keyof typeof show] = key === section ? !show[key as keyof typeof show] : false;
  });
}

function setActive(section: string) {
  activeSection.value = section;
}
</script>
