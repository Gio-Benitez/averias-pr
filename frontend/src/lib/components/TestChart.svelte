<script>
import { Bar } from 'svelte-chartjs';
import { data } from '$lib/data/test_data_chart'

import {
    Chart,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
  } from 'chart.js';

  Chart.register(
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
  );
</script>

<div class="h-full w-full">
    <Bar {data} options={{ responsive: true }} />
</div>

