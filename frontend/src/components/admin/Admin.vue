<template>
  <div class="min-h-screen p-4 md:p-8">
    <HeroHeader title="DashBoard"/>
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
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </template>
      </StatsCard>

      <StatsCard 
        title="Queued Jobs" 
        :value="stats.queuedJobs" 
        link="/jobList"
        icon-bg-color="bg-orange-50"
        icon-color="text-orange-600"
      >
        <template #icon>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </template>
      </StatsCard>

      <StatsCard 
        title="Processing Jobs" 
        :value="stats.processingJobs" 
        link="/jobList"
        icon-bg-color="bg-blue-50"
        icon-color="text-blue-600"
      >
        <template #icon>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
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

     

      <StatsCard 
        title="Success Rate" 
        :value="`${stats.successRate}%`" 
        link="/jobList"
        icon-bg-color="bg-emerald-50"
        icon-color="text-emerald-600"
      >
        <template #icon>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
        </template>
      </StatsCard>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-2 mb-8">
      <div class="bg-white rounded-xl shadow-sm p-6 border ml-5 w-2/3 h-full border-gray-100">
        <h2 class="text-xl font-semibold mb-4">User Statistics</h2>
        <div class="relative h-64">
          <canvas id="userChart"></canvas>
        </div>
        <div v-if="loading" class="text-center">Loading chart...</div>
        <div v-if="error" class="text-center text-red-600">Error loading chart: {{ error }}</div>
      </div>

      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 w-2/3 h-full">
        <h2 class="text-xl font-semibold mb-4">Job Statistics</h2>
        <div class="relative h-64">
          <canvas id="jobChart"></canvas>
        </div>
        <div v-if="loading" class="text-center">Loading chart...</div>
        <div v-if="error" class="text-center text-red-600">Error loading chart: {{ error }}</div>
      </div>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100 mt-8 mb-8">
        <h2 class="text-xl font-semibold text-gray-800 mb-6">Quick Actions</h2>
        <div class="space-y-4">
          <QuickActionButton 
            title="Manage User" 
            link="/user/manage"
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
            title="Manage Encode Profile" 
            link="/ProfileDetails/manage"
            bg-color="bg-green-50"
            text-color="text-green-700"
            hover-bg-color="hover:bg-green-100"
            :on-click="createJob"
          >
            <template #icon>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
              </svg>
            </template>
          </QuickActionButton>

          <QuickActionButton 
            title="Manage Encoding Profiles Details" 
            link="/ProfileDetails/manage"
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
            title="View Job Reports" 
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

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import Cookies from 'js-cookie'
import Chart from 'chart.js/auto'


import DashboardHeader from '../HeroHeader.vue'
import StatsCard from './StatsCard.vue'
import QuickActionButton from './QuickActionButton.vue'
import HeroHeader from '../HeroHeader.vue'


interface Job {
  status: string
  endTime?: string
  startTime?: string
}

interface User {
  status: boolean
}

interface Stats {
  totalUsers: number
  activeUsers: number
  blacklistedUsers: number
  totalJobs: number
  completedJobs: number
  failedJobs: number
  queuedJobs: number
  processingJobs: number
  averageJobDuration: string
  successRate: number
  totalEncodingProfiles: number
  totalEncodingProfileDetails: number
  totalTokens: number
}

// Constants
const apiUrl = 'http://localhost:8084'
const toast = useToast()
const router = useRouter()

// State
const stats = ref<Stats>({
  totalUsers: 0,
  activeUsers: 0,
  blacklistedUsers: 0,
  totalJobs: 0,
  completedJobs: 0,
  failedJobs: 0,
  queuedJobs: 0,
  processingJobs: 0,
  averageJobDuration: '0',
  successRate: 0,
  totalEncodingProfiles: 0,
  totalEncodingProfileDetails: 0,
  totalTokens: 0
})

const loading = ref(false)
const error = ref<string | null>(null)
const userChart = ref<Chart | null>(null)
const jobChart = ref<Chart | null>(null)
const isRenderingUserChart = ref(false)
const isRenderingJobChart = ref(false)
const renderTimeout = ref<NodeJS.Timeout | null>(null)


const getAuthHeaders = () => {
  const accessToken = Cookies.get('access_token')
  if (!accessToken) {
    toast.error('No access token found. Please login again.')
    router.push('/login')
    throw new Error('No access token')
  }
  return {
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json'
    }
  }
}

const fetchData = async <T>(endpoint: string): Promise<T> => {
  try {
    const response = await axios.get<T>(`${apiUrl}/${endpoint}`, getAuthHeaders())
    return response.data
  } catch (err: any) {
    toast.error(`Failed to fetch ${endpoint}: ${err.response?.data?.detail || err.message}`)
    throw err
  }
}

const calculateJobMetrics = (jobs: Job[]) => {
  const queuedJobs = jobs.filter(job => job.status === 'queued').length
  const processingJobs = jobs.filter(job => job.status === 'processing').length
  const completedJobs = jobs.filter(job => job.status === 'completed')
  const failedJobs = jobs.filter(job => job.status === 'failed').length
  const totalJobs = jobs.length
  
  const totalDuration = completedJobs.reduce((sum, job) => {
    const duration = job.endTime && job.startTime 
      ? new Date(job.endTime).getTime() - new Date(job.startTime).getTime()
      : 0
    return sum + duration
  }, 0)

  const averageDuration = completedJobs.length > 0 
    ? totalDuration / completedJobs.length / 1000 
    : 0
    
  const successRate = totalJobs > 0
    ? Math.round((completedJobs.length / totalJobs) * 100)
    : 0

  return {
    queuedJobs,
    processingJobs,
    failedJobs,
    averageJobDuration: averageDuration.toFixed(2),
    successRate
  }
}

const destroyChart = (chart: Chart | null, canvasId: string) => {
  console.log(`Destroying chart for ${canvasId}`)
  if (chart) {
    try {
      chart.destroy()
      console.log(`Chart for ${canvasId} destroyed successfully`)
    } catch (err) {
      console.warn(`Error destroying chart for ${canvasId}:`, err)
    }
  }
  
  const canvas = document.getElementById(canvasId) as HTMLCanvasElement | null
  if (canvas) {
    const context = canvas.getContext('2d')
    if (context) {
      context.clearRect(0, 0, canvas.width, canvas.height)
    }
    // Reset canvas attributes and dimensions
    canvas.width = canvas.width
    canvas.height = canvas.height
    canvas.removeAttribute('data-chart')
    // Remove Chart.js internal references
    if ((canvas as any).__chartjs) {
      delete (canvas as any).__chartjs
    }
 
    canvas.style.display = 'none'
    canvas.offsetHeight
    canvas.style.display = ''
   
    if ((Chart as any).instances) {
      Object.keys((Chart as any).instances).forEach((id) => {
        const instance = (Chart as any).instances[id]
        if (instance.canvas && instance.canvas.id === canvasId) {
          try {
            instance.destroy()
            delete (Chart as any).instances[id]
            console.log(`Removed Chart.js instance ${id} for ${canvasId} from registry`)
          } catch (err) {
            console.warn(`Error removing Chart.js instance ${id} for ${canvasId}:`, err)
          }
        }
      })
    }
  }
  return null
}

const renderUserChart = async () => {
  if (isRenderingUserChart.value) {
    console.warn('User chart rendering skipped: already in progress')
    return
  }
  isRenderingUserChart.value = true
  console.log('Starting user chart render')

  try {
    // Destroy existing chart
    userChart.value = destroyChart(userChart.value, 'userChart')

    await nextTick() // Ensure DOM is ready

    const canvas = document.getElementById('userChart') as HTMLCanvasElement | null
    if (!canvas) {
      console.error('User chart canvas not found')
      error.value = 'User chart canvas not found'
      return
    }

    const context = canvas.getContext('2d')
    if (!context) {
      console.error('Failed to get 2D context for user chart')
      error.value = 'Failed to get 2D context for user chart'
      return
    }

    // Check if canvas is already in use
    if ((Chart as any).instances) {
      const existingInstance = Object.values((Chart as any).instances).find(
        (instance: any) => instance.canvas && instance.canvas.id === 'userChart'
      )
      if (existingInstance) {
        console.warn('Existing Chart.js instance found for userChart, destroying it')
        try {
          existingInstance.destroy()
        } catch (err) {
          console.warn('Error destroying existing userChart instance:', err)
        }
      }
    }

    userChart.value = new Chart(context, {
      type: 'bar',
      data: {
        labels: ['Total Users', 'Active Users', 'Blacklisted Users'],
        datasets: [{
          label: 'User Count',
          data: [
            stats.value.totalUsers,
            stats.value.activeUsers,
            stats.value.blacklistedUsers
          ],
          backgroundColor: [
            'rgba(59, 130, 246, 0.7)',
            'rgba(16, 185, 129, 0.7)',
            'rgba(239, 68, 68, 0.7)'
          ],
          borderColor: [
            'rgba(59, 130, 246, 1)',
            'rgba(16, 185, 129, 1)',
            'rgba(239, 68, 68, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              precision: 0
            }
          }
        },
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            callbacks: {
              label: (context) => `${context.dataset.label}: ${context.raw}`
            }
          }
        }
      }
    })
    console.log('User chart rendered successfully')
  } catch (err) {
    console.error('Error creating user chart:', err)
    error.value = 'Failed to render user chart'
  } finally {
    isRenderingUserChart.value = false
    console.log('User chart rendering completed')
  }
}

const renderJobChart = async () => {
  if (isRenderingJobChart.value) {
    console.warn('Job chart rendering skipped: already in progress')
    return
  }
  isRenderingJobChart.value = true
  console.log('Starting job chart render')

  try {
    // Destroy existing chart
    jobChart.value = destroyChart(jobChart.value, 'jobChart')

    await nextTick() // Ensure DOM is ready

    const canvas = document.getElementById('jobChart') as HTMLCanvasElement | null
    if (!canvas) {
      console.error('Job chart canvas not found')
      error.value = 'Job chart canvas not found'
      return
    }

    const context = canvas.getContext('2d')
    if (!context) {
      console.error('Failed to get 2D context for job chart')
      error.value = 'Failed to get 2D context for job chart'
      return
    }

    // Check if canvas is already in use
    if ((Chart as any).instances) {
      const existingInstance = Object.values((Chart as any).instances).find(
        (instance: any) => instance.canvas && instance.canvas.id === 'jobChart'
      )
      if (existingInstance) {
        console.warn('Existing Chart.js instance found for jobChart, destroying it')
        try {
          existingInstance.destroy()
        } catch (err) {
          console.warn('Error destroying existing jobChart instance:', err)
        }
      }
    }

    jobChart.value = new Chart(context, {
      type: 'doughnut',
      data: {
        labels: ['Completed', 'Failed', 'Queued', 'Processing'],
        datasets: [{
          data: [
            stats.value.completedJobs,
            stats.value.failedJobs,
            stats.value.queuedJobs,
            stats.value.processingJobs
          ],
          backgroundColor: [
            'rgba(16, 185, 129, 0.7)',
            'rgba(239, 68, 68, 0.7)',
            'rgba(249, 115, 22, 0.7)',
            'rgba(59, 130, 246, 0.7)'
          ],
          borderColor: [
            'rgba(16, 185, 129, 1)',
            'rgba(239, 68, 68, 1)',
            'rgba(249, 115, 22, 1)',
            'rgba(59, 130, 246, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom'
          },
          tooltip: {
            callbacks: {
              label: (context) => {
                const label = context.label || ''
                const value = context.raw as number || 0
                const total = (context.dataset.data as number[]).reduce((a, b) => a + b, 0)
                const percentage = total > 0 ? Math.round((value / total) * 100) : 0
                return `${label}: ${value} (${percentage}%)`
              }
            }
          }
        }
      }
    })
    console.log('Job chart rendered successfully')
  } catch (err) {
    console.error('Error creating job chart:', err)
    error.value = 'Failed to render job chart'
  } finally {
    isRenderingJobChart.value = false
    console.log('Job chart rendering completed')
  }
}

const debounceRenderCharts = async () => {
  if (renderTimeout.value) {
    clearTimeout(renderTimeout.value)
  }
  return new Promise<void>((resolve) => {
    renderTimeout.value = setTimeout(async () => {
      console.log('Starting debounced chart rendering')
      await renderUserChart()
      await renderJobChart()
      console.log('Debounced chart rendering completed')
      resolve()
    }, 100)
  })
}

// Quick Actions
const addNewUser = () => {
  router.push('/user/manage')
}

const createJob = () => {
  router.push('/job/create')
}

const manageProfiles = () => {
  router.push('/profile/manage')
}

const viewReports = () => {
  router.push('/job/reports')
}

// Lifecycle Hooks
onMounted(async () => {
  console.log('Component mounted, fetching data and rendering charts')
  try {
    loading.value = true

    const [users, jobs, profiles, profileDetails, blacklistedUsers, tokens] = await Promise.all([
      fetchData<User[]>('users'),
      fetchData<Job[]>('job'),
      fetchData<any[]>('encodeprofile'),
      fetchData<any[]>('encodeprofileDetails'),
      fetchData<{ blacklisted_tokens: any[] }>('blacklisted-tokens/details'),
      fetchData<any[]>('tokens/stored')
    ])

    const jobMetrics = calculateJobMetrics(jobs)

    stats.value = {
      totalUsers: users.length,
      activeUsers: users.filter(user => user.status).length,
      blacklistedUsers: blacklistedUsers.blacklisted_tokens?.length || 0,
      totalJobs: jobs.length,
      completedJobs: jobs.filter(job => job.status === 'completed').length,
      ...jobMetrics,
      totalEncodingProfiles: profiles.length,
      totalEncodingProfileDetails: profileDetails.length,
      totalTokens: tokens.length
    }

    await nextTick() // Ensure DOM is ready
    await debounceRenderCharts()

  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Unknown error occurred'
    console.error('Error fetching dashboard data:', err)
  } finally {
    loading.value = false
    console.log('Component mount completed')
  }
})

onBeforeUnmount(() => {
  console.log('Component unmounting, destroying charts')
  if (renderTimeout.value) {
    clearTimeout(renderTimeout.value)
  }
  userChart.value = destroyChart(userChart.value, 'userChart')
  jobChart.value = destroyChart(jobChart.value, 'jobChart')
})
</script>