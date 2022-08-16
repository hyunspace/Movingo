<template>
  <Pie v-if="genreTimes && genreNames"
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>

<script>
import { Pie } from 'vue-chartjs/legacy';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale
} from 'chart.js'



ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, ChartDataLabels)
export default {
  name: 'PieChart',
  components: {
    Pie,
  },
  props: {
    genreNames:Array,
    genreTimes:Array,

    chartId: {
      type: String,
      default: 'pie-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 100
    },
    height: {
      type: Number,
      default: 100
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      chartData: {
        labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
        datasets: [
          {
            backgroundColor: ['#8ecae6', '#58b4d1', '#219ebc', '#126782','#023047', '#ffb703','#fd9e02', '#fb8500'],
            data: [40, 20, 80, 10]
          }
        ]
      },
      
      chartOptions: {
        plugins: {
          datalabels: {            
            color: '#ffffff',
            display: true,
            align: 'end',
            
            formatter: function(value, ctx) {
              return ctx.chart.data.labels[ctx.dataIndex];
            }
          },
          legend: {
            display: false,
            labels: {
            }
          }
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  created() {
    console.log(this.genreNames)
    this.chartData.labels = this.genreNames
    this.chartData.datasets[0].data = this.genreTimes
  }

}
</script>
