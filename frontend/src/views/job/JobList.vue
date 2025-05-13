<template>
  <DefaultLayout>
    <div class="max-w-6xl mx-auto my-12 px-4">
    

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white shadow rounded-xl p-6 border-l-4 border-blue-500">
          <h3 class="text-gray-500 text-sm font-medium">Total Jobs</h3>
          <p class="text-3xl font-bold text-gray-800">{{ metrics.total_jobs || 0 }}</p>
        </div>
        
        <div class="bg-white shadow rounded-xl p-6 border-l-4 border-green-500">
          <h3 class="text-gray-500 text-sm font-medium">Completed Jobs</h3>
          <p class="text-3xl font-bold text-gray-800">{{ metrics.completed_jobs || 0 }}</p>
          <p class="text-sm text-gray-500 mt-1">{{ completionRate }}% completion rate</p>
        </div>
        
        <div class="bg-white shadow rounded-xl p-6 border-l-4 border-red-500">
          <h3 class="text-gray-500 text-sm font-medium">Failed Jobs</h3>
          <p class="text-3xl font-bold text-gray-800">{{ metrics.failed_jobs || 0 }}</p>
          <p class="text-sm text-gray-500 mt-1">{{ failureRate }}% failure rate</p>
        </div>
        
        <div class="bg-white shadow rounded-xl p-6 border-l-4 border-purple-500">
          <h3 class="text-gray-500 text-sm font-medium">Avg Processing Time</h3>
          <p class="text-3xl font-bold text-gray-800">{{ metrics.avg_processing_time || 'N/A' }}</p>
        </div>
      </div>

      <!-- Filters -->
      <div class="bg-white shadow rounded-xl p-6 mb-8">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Filters</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
            <select v-model="filters.status" class="w-full px-3 py-2 border rounded-md">
              <option value="">All Statuses</option>
              <option value="queued">queued</option>
              <option value="processing">Processing</option>
              <option value="completed">Completed</option>
              <option value="failed">Failed</option>
            </select>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Date Range</label>
            <select v-model="filters.date_range" class="w-full px-3 py-2 border rounded-md">
              <option value="all">All Time</option>
              <option value="today">Today</option>
              <option value="week">This Week</option>
              <option value="month">This Month</option>
              <option value="custom">Custom</option>
            </select>
          </div>
          
          <div v-if="filters.date_range === 'custom'">
            <label class="block text-sm font-medium text-gray-700 mb-1">From</label>
            <input v-model="filters.start_date" type="date" class="w-full px-3 py-2 border rounded-md">
          </div>
          
          <div v-if="filters.date_range === 'custom'">
            <label class="block text-sm font-medium text-gray-700 mb-1">To</label>
            <input v-model="filters.end_date" type="date" class="w-full px-3 py-2 border rounded-md">
          </div>
        </div>
        
        <div class="mt-4 flex justify-end gap-2">
          <button 
            @click="resetFilters" 
            class="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200"
          >
            Reset
          </button>
          <button 
            @click="applyFilters" 
            class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500"
          >
            Apply
          </button>
        </div>
      </div>

   

      <!-- Job List Table -->
      <div class="bg-white shadow rounded-xl overflow-x-auto">
        <div class="p-4 border-b flex justify-between items-center">
          <h3 class="text-lg font-semibold text-gray-800">Recent Jobs</h3>
          <button 
            @click="refreshData" 
            class="flex items-center gap-2 px-3 py-1 bg-gray-100 rounded-md hover:bg-gray-200"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Refresh
          </button>
        </div>
        
        <div v-if="loading" class="p-6">
          <div class="animate-pulse space-y-6">
            <div v-for="i in 5" :key="i" class="flex items-center gap-4">
              <div class="w-16 h-16 bg-gray-200 rounded-full"></div>
              <div class="flex-1 space-y-3">
                <div class="h-4 bg-gray-200 rounded w-3/4"></div>
                <div class="h-4 bg-gray-200 rounded w-1/2"></div>
              </div>
            </div>
          </div>
        </div>

        <table v-else class="min-w-full table-auto">
          <thead class="bg-gray-700 text-white">
            <tr>
              <th class="px-6 py-3 text-left text-sm font-semibold">Filename</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">Job By</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">Profile</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">Start Time</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">End Time</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">Status</th>
              <th class="px-6 py-3 text-left text-sm font-semibold">Duration</th>
            </tr>
          </thead>
          <tbody class="text-gray-800">
            <tr v-for="job in filteredJobs" :key="job.id" class="border-b hover:bg-gray-50">
              <td class="px-6 py-4 text-sm">{{ job.video_filename }}</td>
              <td class="px-6 py-4 text-sm">{{ job.job_by || 'Unknown' }}</td>
              <td class="px-6 py-4 text-sm">{{ job.encoding_profile }}</td>
              <td class="px-6 py-4 text-sm">{{ formatDate(job.started_at) }}</td>
              <td class="px-6 py-4 text-sm">{{ formatDate(job.ended_at) }}</td>
              <td class="px-6 py-4 text-sm">
                <span :class="statusClass(job.status)" class="px-2 py-1 rounded-full text-xs">
                  {{ job.status }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm">{{ calculateDuration(job.started_at, job.ended_at) }}</td>
            </tr>
          </tbody>
        </table>

        <!-- Pagination -->
        <div v-if="filteredJobs.length > 0" class="p-4 border-t flex justify-between items-center">
          <div class="text-sm text-gray-500">
            Showing {{ pagination.start }} to {{ pagination.end }} of {{ pagination.total }} jobs
          </div>
          <div class="flex gap-2">
            <button 
              @click="prevPage" 
              :disabled="pagination.current_page === 1"
              :class="{'opacity-50 cursor-not-allowed': pagination.current_page === 1}"
              class="px-3 py-1 bg-gray-100 rounded-md hover:bg-gray-200"
            >
              Previous
            </button>
            <button 
              @click="nextPage" 
              :disabled="pagination.current_page === pagination.total_pages"
              :class="{'opacity-50 cursor-not-allowed': pagination.current_page === pagination.total_pages}"
              class="px-3 py-1 bg-gray-100 rounded-md hover:bg-gray-200"
            >
              Next
            </button>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="!loading && filteredJobs.length === 0" class="p-10 text-center">
          <div class="text-gray-300 mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-16 h-16 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">No jobs found</h3>
          <p class="text-gray-500 mb-6">No jobs match your current filters.</p>
          <button
            @click="resetFilters"
            class="px-6 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition"
          >
            Reset Filters
          </button>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted} from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'
import Chart from 'chart.js/auto'

const apiUrl = 'http://localhost:8084'
const Job = ref<any[]>([])
const loading = ref(true)
const toast = useToast()
const statusChart = ref<HTMLCanvasElement | null>(null)
const timeTrendChart = ref<HTMLCanvasElement | null>(null)
console.log('adasdasd')
// Metrics data
const metrics = ref({
  total_jobs: 0,
  completed_jobs: 0,
  failed_jobs: 0,
  avg_processing_time: '0s',
  status_distribution: {}
})

// Filters
const filters = ref({
  status: '',
  date_range: 'all',
  start_date: '',
  end_date: '',
  search: ''
})

// Pagination
const pagination = ref({
  current_page: 1,
  per_page: 10,
  total: 0,
  total_pages: 1
})

// Computed properties
const completionRate = computed(() => {
  if (metrics.value.total_jobs === 0) return 0
  return ((metrics.value.completed_jobs / metrics.value.total_jobs) * 100).toFixed(1)
})

const failureRate = computed(() => {
  if (metrics.value.total_jobs === 0) return 0
  return ((metrics.value.failed_jobs / metrics.value.total_jobs) * 100).toFixed(1)
})

const filteredJobs = computed(() => {
  let result = [...Job.value]
  
  // Apply status filter
  if (filters.value.status) {
    result = result.filter(job => job.status === filters.value.status)
  }
  
  // Apply date range filter
  if (filters.value.date_range !== 'all') {
    const now = new Date()
    let startDate = new Date()
    
    switch (filters.value.date_range) {
      case 'today':
        startDate.setHours(0, 0, 0, 0)
        break
      case 'week':
        startDate.setDate(now.getDate() - 7)
        break
      case 'month':
        startDate.setMonth(now.getMonth() - 1)
        break
      case 'custom':
        if (filters.value.start_date) {
          startDate = new Date(filters.value.start_date)
        }
        break
    }
    
    result = result.filter(job => {
      const jobDate = new Date(job.started_at)
      console.log('jobdate',jobDate)
      return jobDate >= startDate && 
        (!filters.value.end_date || jobDate <= new Date(filters.value.end_date))
    })
  }
  
  // Update pagination totals
  pagination.value.total = result.length
  pagination.value.total_pages = Math.ceil(result.length / pagination.value.per_page)
  
  // Apply pagination
  const start = (pagination.value.current_page - 1) * pagination.value.per_page
  const end = start + pagination.value.per_page
  pagination.value.start = start + 1
  pagination.value.end = Math.min(end, result.length)
  
  return result.slice(start, end)
})

// Helper functions
const formatDate = (dateString: string) => {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleString()
}

const calculateDuration = (start: string, end: string) => {
  if (!start) return 'N/A'
  const startTime = new Date(start)
  const endTime = end ? new Date(end) : new Date()
  console.log(startTime)
  console.log(endTime)
  const seconds = Math.floor((endTime.getTime() - startTime.getTime()) / 1000)
  console.log(seconds)
  if (seconds < 60) return `${seconds}s`
  if (seconds < 3600) return `${Math.floor(seconds / 60)}m ${seconds % 60}s`
  return `${Math.floor(seconds / 3600)}h ${Math.floor((seconds % 3600) / 60)}m`
}

const statusClass = (status: string) => {
  switch (status.toLowerCase()) {
    case 'completed': return 'bg-green-100 text-green-800'
    case 'failed': return 'bg-red-100 text-red-800'
    case 'processing': return 'bg-blue-100 text-blue-800'
    default: return 'bg-gray-100 text-gray-800'
  }
}

// Data fetching
const fetchJob = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${apiUrl}/job`)
    Job.value = Array.isArray(res.data) ? res.data : [res.data]
    calculateMetrics()
    renderCharts()
  } catch (error: any) {
    toast.error('Failed to fetch jobs: ' + (error.response?.data?.detail || error.message))
    Job.value = []
  } finally {
    loading.value = false
  }
}

const calculateMetrics = () => {
  const total = Job.value.length
  const completed = Job.value.filter(job => job.status === 'completed').length
  const failed = Job.value.filter(job => job.status === 'failed').length
  
  // Calculate average processing time
  let totalTime = 0
  let count = 0
  
  Job.value.forEach(job => {
    if (job.started_at && job.ended_at) {
      const start = new Date(job.started_at)
      const end = new Date(job.ended_at)
      totalTime += end.getTime() - start.getTime()
      count++
    }
  })
  
  const avgTime = count > 0 ? totalTime / count : 0
  const avgSeconds = Math.floor(avgTime / 1000)
  
  // Format average time
  let avgTimeFormatted = ''
  if (avgSeconds < 60) {
    avgTimeFormatted = `${avgSeconds}s`
  } else if (avgSeconds < 3600) {
    avgTimeFormatted = `${Math.floor(avgSeconds / 60)}m ${avgSeconds % 60}s`
  } else {
    avgTimeFormatted = `${Math.floor(avgSeconds / 3600)}h ${Math.floor((avgSeconds % 3600) / 60)}m`
  }
  
  // Status distribution
  const statusDistribution = Job.value.reduce((acc, job) => {
    acc[job.status] = (acc[job.status] || 0) + 1
    return acc
  }, {})
  
  metrics.value = {
    total_jobs: total,
    completed_jobs: completed,
    failed_jobs: failed,
    avg_processing_time: avgTimeFormatted,
    status_distribution: statusDistribution
  }
}

// Chart rendering
const renderCharts = () => {
  // Status distribution pie chart
  if (statusChart.value) {
    const statusData = metrics.value.status_distribution
    const ctx = statusChart.value.getContext('2d')
    
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: Object.keys(statusData),
        datasets: [{
          data: Object.values(statusData),
          backgroundColor: [
            '#3B82F6', // blue for processing
            '#10B981', // green for completed
            '#EF4444', // red for failed
            '#9CA3AF'  // gray for others
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'right'
          }
        }
      }
    })
  }
  
 
}

// Filter and pagination functions
const applyFilters = () => {
  pagination.value.current_page = 1
}

const resetFilters = () => {
  filters.value = {
    status: '',
    date_range: 'all',
    start_date: '',
    end_date: '',
    search: ''
  }
  pagination.value.current_page = 1
}

const nextPage = () => {
  if (pagination.value.current_page < pagination.value.total_pages) {
    pagination.value.current_page++
  }
}

const prevPage = () => {
  if (pagination.value.current_page > 1) {
    pagination.value.current_page--
  }
}

const refreshData = () => {
  fetchJob()
}

onMounted(() => {
  fetchJob()
})
</script>


