<template>

    <div class="min-h-screen p-4 md:p-8">
      <DashboardHeader />
      
      <!-- Stats Cards Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatsCard 
          title="Total Users" 
          :value="stats.totalUsers" 
          link="/user/manage"
          icon-bg-color="bg-blue-50"
          icon-color="text-blue-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Active Users" 
          :value="stats.activeUsers" 
          link="/user/manage"
          icon-bg-color="bg-green-50"
          icon-color="text-green-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Blacklisted Users" 
          :value="stats.blacklistedUsers" 
          link="/user/manage"
          icon-bg-color="bg-red-50"
          icon-color="text-red-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M5.636 5.636l3.536 3.536m0 5.656l-3.536 3.536" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Total Jobs" 
          :value="stats.totalJobs" 
          link="/jobList"
          icon-bg-color="bg-purple-50"
          icon-color="text-purple-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Completed Jobs" 
          :value="stats.completedJobs" 
          link="/jobList"
          icon-bg-color="bg-teal-50"
          icon-color="text-teal-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Failed Jobs" 
          :value="stats.failedJobs" 
          link="/jobList"
          icon-bg-color="bg-amber-50"
          icon-color="text-amber-600"
        >
          <template #icon>
            <svg xmlns="http://www/w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Encoding Profiles" 
          :value="stats.totalEncodingProfiles" 
          link="/profile/manage"
          icon-bg-color="bg-indigo-50"
          icon-color="text-indigo-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </template>
        </StatsCard>

        <StatsCard 
          title="Profile Details" 
          :value="stats.totalEncodingProfileDetails" 
          link="/jobList"
          icon-bg-color="bg-yellow-50"
          icon-color="text-yellow-600"
        >
          <template #icon>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
          </template>
        </StatsCard>
      </div>

      <!-- Recent Activity and Quick Actions -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Recent Activities -->
        <!-- <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
          <h2 class="text-xl font-semibold text-gray-800 mb-6">Recent Activities</h2>
          <div class="space-y-3 max-h-96 overflow-y-auto pr-2">
            <ActivityItem 
              v-for="activity in recentActivities" 
              :key="activity.id" 
              :activity="activity"
            />
          </div>
        </div> -->

      <!-- Quick Actions -->
<div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 mt-8 mb-8">
  <h2 class="text-xl font-semibold text-gray-800 mb-6">Quick Actions</h2>
  <div class="space-y-4">
    <QuickActionButton 
      title="Manage User" 
      link="/manage/user"
      bg-color="bg-blue-50"
      text-color="text-blue-700"
      hover-bg-color="hover:bg-blue-100"
      :on-click="addNewUser"
    >
      <template #icon>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
        </svg>
      </template>
    </QuickActionButton>

    <QuickActionButton 
      title="Manage Encoding Profile Details" 
      link="/manage/profile"
      bg-color="bg-green-50"
      text-color="text-green-700"
      hover-bg-color="hover:bg-green-100"
      :on-click="createJob"
    >
      <template #icon>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clip-rule="evenodd" />
          <path d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z" />
        </svg>
      </template>
    </QuickActionButton>

    <QuickActionButton 
      title="Manage Encoding Profile" 
      link="/manage/profileDetails"
      bg-color="bg-purple-50"
      text-color="text-purple-700"
      hover-bg-color="hover:bg-purple-100"
      :on-click="manageProfiles"
    >
      <template #icon>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
        </svg>
      </template>
    </QuickActionButton>

    <QuickActionButton 
      title="Retry Failed Job" 
      link="/jobList"
      bg-color="bg-amber-50"
      text-color="text-amber-700"
      hover-bg-color="hover:bg-amber-100"
      :on-click="viewReports"
    >
      <template #icon>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm2 10a1 1 0 10-2 0v3a1 1 0 102 0v-3zm2-3a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1zm4-1a1 1 0 10-2 0v7a1 1 0 102 0V8z" clip-rule="evenodd" />
        </svg>
      </template>
    </QuickActionButton>
  </div>
</div>
      </div>
    </div>

</template>

<script>

import DashboardHeader from '../DashboardHeader.vue'
import StatsCard from './StatsCard.vue'
import QuickActionButton from './QuickActionButton.vue'
import ActivityItem from '../ActivityItem.vue'

export default {
  components: {
   
    DashboardHeader,
    StatsCard,
    QuickActionButton,
    ActivityItem
  },
  data() {
    return {
      stats: {
        totalUsers: 0,
        activeUsers: 0,
        blacklistedUsers: 0,
        totalJobs: 0,
        completedJobs: 0,
        failedJobs: 0,
        totalEncodingProfiles: 0,
        totalEncodingProfileDetails: 0
      },
      
    }
  },
  methods: {
    addNewUser() {
      console.log('Add new user clicked');
    },
    createJob() {
      console.log('Create job clicked');
    },
    manageProfiles() {
      console.log('Manage profiles clicked');
    },
    viewReports() {
      console.log('View reports clicked');
    }
  },
  async created() {
    try {
      // Fetch all data in parallel
      const [usersResponse, jobsResponse, profilesResponse, profileDetailsResponse] = await Promise.all([
        fetch('http://localhost:8084/users'),
        fetch('http://localhost:8084/job'),
        fetch('http://localhost:8084/encodeprofile'),
        fetch('http://localhost:8084/encodeprofileDetails')
      ]);

      if (!usersResponse.ok || !jobsResponse.ok || !profilesResponse.ok || !profileDetailsResponse.ok) {
        throw new Error('Failed to fetch data from one or more endpoints');
      }

      const users = await usersResponse.json();
      const jobs = await jobsResponse.json();
      const profiles = await profilesResponse.json();
      const profileDetails = await profileDetailsResponse.json();

      // Calculate stats
      this.stats = {
        totalUsers: users.length,
        activeUsers: users.filter(user => user.status === true).length,
        blacklistedUsers: users.filter(user => user.status === false).length,
        totalJobs: jobs.length,
        completedJobs: jobs.filter(job => job.status === 'completed').length,
        failedJobs: jobs.filter(job => job.status === 'failed').length,
        totalEncodingProfiles: profiles.length,
        totalEncodingProfileDetails: profileDetails.length
      };

      this.loading = false;
    } catch (error) {
      this.error = error.message;
      this.loading = false;
      console.error('Error fetching dashboard data:', error);
    }
  }
}
</script>
