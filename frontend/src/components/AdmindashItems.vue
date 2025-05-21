<template>
  <div class="flex flex-col gap-4 w-full max-w-4xl mx-auto px-4 py-6">
    <SidebarSection
    title="Dashboard"
    :icon="HomeIcon"
    :to="dashboardRoute"
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
import { ref, reactive, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Cookies from 'js-cookie';
import * as jwtDecode from 'jwt-decode';

import ManageUser from './ManageUser.vue';
import ManageEprofile from './ManageEprofile.vue';
import ManageEprofileDetails from './ManageEprofileDetails.vue';
import SidebarSection from './SidebarSection.vue';
import { HomeIcon } from '@heroicons/vue/24/solid';
interface DecodedToken {
  sub: string;
  role: string;
  exp: number;
}

const route = useRoute();
const router = useRouter();

const show = reactive({
  users: false,
  eprofiles: false,
  eprofileDetails: false,
});

const activeSection = ref('');

const dashboardRoute = computed(() => {
  const token = Cookies.get('access_token');
  if (!token) return '/'; // fallback to login

  try {
    const decoded: DecodedToken = jwtDecode.default(token);
    if (decoded.role === 'super_admin') return '/superadmin/dashboard';
    if (decoded.role === 'admin') return '/admin/dashboard';
    return '/jobList';
  } catch {
    return '/';
  }
});

onMounted(() => {
  const path = route.path.toLowerCase();
  if (path.includes('/user')) activeSection.value = 'users';
  else if (path.includes('/profile') && !path.includes('/profiledetails')) activeSection.value = 'eprofiles';
  else if (path.includes('/profiledetails')) activeSection.value = 'eprofileDetails';
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

  if (section === 'dashboard') {
    const token = Cookies.get('access_token');
    if (token) {
      try {
        const decoded: DecodedToken = jwtDecode.default(token);
        const role = decoded.role;
        console.log('Decoded role from token:', role);

        if (role === 'super_admin') {
          router.push('/superadmin/dashboard');
        } else if (role === 'admin') {
          router.push('/admin/dashboard');
        } else {
          router.push('/jobList'); // fallback for other roles
        }
      } catch (error) {
        console.error('Failed to decode token:', error);
        router.push('/'); // redirect to login if token is invalid
      }
    } else {
      router.push('/'); // redirect to login if no token
    }
  }
}
</script>
