<script lang="ts">
    import { dashboardStore } from "$lib/stores";
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

<div class="rounded-2xl aspect-auto py-12 px-12 w-full h-full bg-neutral shadow-lg">
    <Bar {data} options={{ responsive: true }} />
</div>


<style lang="postcss">

</style>
