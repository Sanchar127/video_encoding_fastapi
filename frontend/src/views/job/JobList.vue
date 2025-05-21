<template>
  <DefaultLayout>
    <div class="max-w-full mx-5 my-12 px-4">
      <JobsMetrics
        :metrics="metrics"
        :completion-rate="completionRate"
        :failure-rate="failureRate"
        :queued-rate="queuedRate"
        :processing-rate="processingRate"
      />
      
      <Filters 
        :filters="filters"
        @reset="resetFilters"
        @apply="applyFilters"
      />
      
      <JobTable
        :loading="loading"
        :filtered-jobs="filteredJobs"
        :details="Details"
        @refresh="refreshData"
        @retry="retryJob"
        @reset="resetFilters"
      />
    </div>
  </DefaultLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted} from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import DefaultLayout from '../../layout/DefaultLayout.vue'

import Cookies from 'js-cookie'


import ArrowPathIcons from '../../components/icons/ArrowPathIcons.vue'
import Filters from '../../components/job/Filters.vue'
import JobTable from '../../components/job/JobTable.vue'
import JobsMetrics from '../../components/job/JobsMetrics.vue'

const apiUrl = 'http://localhost:8084'
interface JobItem {
  id: number
  video_filename: string
  job_by: string
  encoding_profile: number
  encoding_profileDetails: number
  started_at: string
  ended_at: string
  status: string
}

const Job = ref<JobItem[]>([])
const Details = ref<any[]>([])


const loading = ref(true)
const toast = useToast()

console.log('adasdasd')
// Metrics data
const metrics = ref({
  total_jobs: 0,
  completed_jobs: 0,
  failed_jobs: 0,
  queued_jobs: 0,        // Add this
  processing_jobs: 0,    // Add this
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
  const totalFailedJobs = metrics.value.failed_jobs
  const totalProcessedJobs = metrics.value.completed_jobs + metrics.value.failed_jobs
  
  // Only calculate rate if we have processed jobs
  if (totalProcessedJobs === 0) return 0
  return ((totalFailedJobs / totalProcessedJobs) * 100).toFixed(1)
})

const queuedRate = computed(() => {
  const totalqueuedJob = metrics.value.queued_jobs
  const totalProcessedJobs = metrics.value.completed_jobs + metrics.value.queued_jobs
  
  // Only calculate rate if we have processed jobs
  if (totalProcessedJobs === 0) return 0
  return (( totalqueuedJob / totalProcessedJobs) * 100).toFixed(1)
})

const processingRate = computed(() => {
  if (metrics.value.total_jobs === 0) return '0%'
  return `${((metrics.value.processing_jobs / metrics.value.total_jobs) * 100).toFixed(1)}%`
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
  console.log(`This is Start date ${startTime}`)
  console.log(`This is End date endTime`)
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
const fetchProfileDetails = async () => {
  try {
    const res = await axios.get(`${apiUrl}/encodeprofileDetails`, {
      headers: {
        Authorization: `Bearer ${Cookies.get('access_token')}`,
      }
    })
    Details.value = res.data  // Make sure this is an array of objects with `id` and `name`
    console.log(res.data)
  } catch (err) {
    toast.error('Failed to fetch profile details')
  }
}


const retryJob = async (jobId: number) => {
  try {
    
    console.log(`job id = ${jobId}`)
    const accessToken = Cookies.get('access_token');
    console.log(accessToken);

    const response = await axios.put(
      `${apiUrl}/retry-job/${jobId}`,
      {},  // Empty body
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json'
        }
      }
    );

    if (response.status === 200 || response.status === 202) {
      toast.success('Retry job request sent successfully!');
      refreshData();
    }
  } catch (error: any) {
    const errorMsg = error.response?.data?.detail || error.message;
    toast.error(`Retry failed: ${errorMsg}`);

    if (error.response?.status === 401) {
      console.log("Authentication error:", error.response);
    }
  }
}





const calculateMetrics = () => {
  const total = Job.value.length
  const completed = Job.value.filter(job => job.status === 'completed').length
  const failed = Job.value.filter(job => job.status === 'failed').length
  const queued = Job.value.filter(job => job.status === 'queued').length
  const processing = Job.value.filter(job => job.status === 'processing').length
  
  // Calculate processing times
  let totalCompletedTime = 0
  let completedCount = 0
  let totalActiveTime = 0
  let activeCount = 0
  
  Job.value.forEach(job => {
    if (job.started_at) {
      const start = new Date(job.started_at)
      const now = new Date()
      
      if (job.status === 'completed' && job.ended_at) {
        // For completed jobs with end date
        const end = new Date(job.ended_at)
        totalCompletedTime += end.getTime() - start.getTime()
        completedCount++
      } else if (['processing', 'queued'].includes(job.status)) {
        // For ongoing jobs, use current time as end time
        totalActiveTime += now.getTime() - start.getTime()
        activeCount++
      }
    }
  })
  
  // Calculate averages
  const avgCompletedTime = completedCount > 0 ? totalCompletedTime / completedCount : 0
  const avgActiveTime = activeCount > 0 ? totalActiveTime / activeCount : 0
  
  // Combine averages (weighted or simple)
  const avgTime = completedCount > 0 ? avgCompletedTime : avgActiveTime
  const avgSeconds = Math.floor(avgTime / 1000)
  
  // Format average time
  let avgTimeFormatted = 'N/A'
  if (avgSeconds > 0) {
    if (avgSeconds < 60) {
      avgTimeFormatted = `${avgSeconds}s`
    } else if (avgSeconds < 3600) {
      avgTimeFormatted = `${Math.floor(avgSeconds / 60)}m ${avgSeconds % 60}s`
    } else {
      avgTimeFormatted = `${Math.floor(avgSeconds / 3600)}h ${Math.floor((avgSeconds % 3600) / 60)}m`
    }
    
    // Add indicator if using active jobs in calculation
    if (completedCount === 0 && activeCount > 0) {
      avgTimeFormatted += ' (estimated)'
    }
  }
  
  metrics.value = {
    total_jobs: total,
    completed_jobs: completed,
    failed_jobs: failed,
    queued_jobs: queued,
    processing_jobs: processing,
    avg_processing_time: avgTimeFormatted,
    status_distribution: {
      completed,
      failed,
      queued,
      processing
    }
  }
}





const refreshData = () => {
  fetchJob()
  fetchProfileDetails()
}

onMounted(() => {
  fetchJob()
  fetchProfileDetails()
})
</script>


