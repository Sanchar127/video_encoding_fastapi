<template>
  <div>
    <Bar :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script setup lang="ts">
import { computed, watch } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

interface Props {
  total: number
  active: number
  blacklisted: number
  tokens: number
}
const props = defineProps<Props>()

const chartData = computed(() => ({
  labels: ['Total Users', 'Active Users', 'Blacklisted Users', 'Stored Tokens'],
  datasets: [
    {
      label: 'Count',
      data: [props.total, props.active, props.blacklisted, props.tokens],
    
      borderWidth: 1,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  scales: {
    y: { beginAtZero: true },
  },
}


watch(props, () => {
  
})
</script>
