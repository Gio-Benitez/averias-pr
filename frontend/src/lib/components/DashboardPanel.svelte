<script lang="ts">
    import { dashboardStore } from "$lib/stores";
    import { Bar } from 'svelte-chartjs';
    import { data } from '$lib/data/test_data_chart'
    import { Chart } from 'chart.js/auto';

    /*
    Chart.register(
        Title,
        Tooltip,
        Legend,
        BarElement,
        CategoryScale,
        LinearScale
    );
    */
    
</script>

<div class="rounded-2xl aspect-auto w-full h-full bg-primary shadow-lg">
    <canvas id="testChart"></canvas>
</div>


<style lang="postcss">

</style>
