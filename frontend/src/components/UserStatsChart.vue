<template>
  <div class="w-full">
    <Bar 
      v-if="chartData" 
      :chart-data="chartData" 
      :chart-options="chartOptions" 
    />
    <div v-else class="text-center text-gray-500">
      No chart data available
    </div>
  </div>
</template>

<script setup lang="ts">
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
  chartData: {
    labels: string[],
    datasets: {
      label: string,
      backgroundColor: string[],
      data: number[]
    }[]
  } | null
}

const props = defineProps<Props>()

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: { beginAtZero: true },
  },
}
</script>