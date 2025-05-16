<template>
  <DefaultLayout>
    <div class="max-w-full mx-5 my-12 px-4">
    

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
              <option value="processing">processing</option>
              <option value="completed">completed</option>
              <option value="failed">failed</option>
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

   

  
      <div class="bg-white shadow-lg rounded-xl overflow-hidden border border-gray-100 transition-all duration-300 hover:shadow-xl">
  <!-- Header -->
  <div class="p-5 border-b border-gray-100 flex justify-between items-center bg-gradient-to-r from-gray-50 to-white">
  
    <button 
      @click="refreshData" 
      class="flex items-center gap-2 px-4 py-2 bg-indigo-50 text-indigo-600 rounded-lg hover:bg-indigo-100 transition-colors duration-200"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
      </svg>
      Refresh
    </button>
  </div>
  
  <!-- Loading State -->
  <div v-if="loading" class="p-6">
    <div class="animate-pulse space-y-6">
      <div v-for="i in 5" :key="i" class="flex items-center gap-4">
        <div class="w-12 h-12 bg-gray-100 rounded-full"></div>
        <div class="flex-1 space-y-3">
          <div class="h-4 bg-gray-100 rounded w-3/4"></div>
          <div class="h-3 bg-gray-100 rounded w-1/2"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Table -->
  <div v-else class="overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Filename</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Job By</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Profile name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Profile Details name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Start Time</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">End Time</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Retry</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Duration</th>
        </tr>
      </thead>
    <tbody class="bg-white divide-y divide-gray-200">
  <tr 
    v-for="job in filteredJobs" 
    :key="job.id" 
    class="hover:bg-gray-50 transition-colors duration-150"
  >
    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ job.video_filename }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ job.job_by || 'Unknown' }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ job.encoding_profile }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ job.encoding_profileDetails }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(job.started_at) }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(job.ended_at) }}</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm">
      <span :class="statusClass(job.status)" class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full">
        {{ job.status }}
      </span>
    </td>

    <!-- Conditional column based on status -->
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500" v-if="job.status === 'completed'">--</td>
    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500" v-else>+</td>

    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ calculateDuration(job.started_at, job.ended_at) }}</td>
  </tr>
</tbody>

    </table>
  </div>

  <!-- Pagination -->
  <div v-if="filteredJobs.length > 0" class="p-4 border-t border-gray-100 bg-gray-50 flex justify-between items-center">
    <div class="text-sm text-gray-500">
      Showing <span class="font-medium">{{ pagination.start }}</span> to <span class="font-medium">{{ pagination.end }}</span> of <span class="font-medium">{{ pagination.total }}</span> jobs
    </div>
    <div class="flex gap-2">
      <button 
        @click="prevPage" 
        :disabled="pagination.current_page === 1"
        :class="{'opacity-50 cursor-not-allowed': pagination.current_page === 1}"
        class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors duration-200"
      >
        Previous
      </button>
      <button 
        @click="nextPage" 
        :disabled="pagination.current_page === pagination.total_pages"
        :class="{'opacity-50 cursor-not-allowed': pagination.current_page === pagination.total_pages}"
        class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-colors duration-200"
      >
        Next
      </button>
    </div>
  </div>

  <!-- Empty State -->
  <div v-if="!loading && filteredJobs.length === 0" class="p-12 text-center">
    <div class="mx-auto flex items-center justify-center h-24 w-24 rounded-full bg-gray-100 mb-6">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">No jobs found</h3>
    <p class="text-gray-500 max-w-md mx-auto mb-6">We couldn't find any jobs matching your current filters. Try adjusting your search or reset the filters.</p>
    <button
      @click="resetFilters"
      class="px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors duration-200 shadow-sm"
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


const apiUrl = 'http://localhost:8084'
const Job = ref<any[]>([])
const loading = ref(true)
const toast = useToast()

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


