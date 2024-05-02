<script lang="ts">
    import { dashboardStore } from "$lib/stores";
    import { Bar, Line } from 'svelte-chartjs';
    import { data } from '$lib/data/test_data_chart';
    import { Chart,
             Title,
             Tooltip,
             Legend,
             BarElement,
             CategoryScale,
             LinearScale } from "chart.js";
    import autocolors from 'chartjs-plugin-autocolors';

    Chart.register(
        Title,
        Tooltip,
        Legend,
        BarElement,
        CategoryScale,
        LinearScale,
        autocolors
    );

    
</script>

<div class="rounded-2xl py-8 px-12 aspect-auto w-full h-full bg-white shadow-lg">
    <Bar 
        {data} 
        options={
            {   responsive: true, 
                scales: {
                    x: {
                        stacked: true,
                        ticks: {
                            color: 'black'
                        }
                    },
                    y: {
                        stacked: true,
                        ticks: {
                            color: 'black',
                            
                        }
                    }
                },
                plugins: {
                    autocolors: {
                        mode: 'data',
                        enabled: true
                    }
                }
            }
        }
        />

</div>
<style lang="postcss">
    
</style>
