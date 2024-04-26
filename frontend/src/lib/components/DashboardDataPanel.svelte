<script lang="ts">
    import { reportCategories, municipios, dashboardStore } from "$lib/stores";
    import { createEventDispatcher } from "svelte";
    
    // Report Category Filter Logic
    let catUnselected: boolean = true;
    let muniUnselected: boolean = true;
    let cat: string = '';
    let muni: string = '';
    const municipalities = $municipios.municipiosArray;
    const categoryArray = $reportCategories.categoryArray;
    function updateChart (data: any) {
        $dashboardStore.chartData = data;
        console.log($dashboardStore.chartData);
  }

</script>
<div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 py-8 rounded-2xl">
    <div class="flex flex-col w-full h-1/5 text-center">
        <h1>Variables Requeridas</h1>
        <div class="divider divider-neutral"></div>
        <h2>Variable 1 (Eje Vertical)</h2>
        <select class="select text-lg font-medium select-secondary w-full">
            <option selected ># de Reportes</option>
            <option>% de Reportes</option>  
        </select>
        <h2>Variable 2 (Eje Horizontal)</h2>
        <select class="select text-lg font-medium select-secondary w-full">
            <option selected>Municipios</option>
            <option>Categorías</option> 
        </select>
        
        <div class="divider divider-neutral"></div>
        <h1>Variables Opcionales</h1>
            
    </div>
</div>

<style lang="postcss">
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    .stat-title {
        @apply text-lg font-semibold;
    }
    .stat-value {
        @apply text-2xl font-bold;
    }
    option {
        @apply font-medium;
    }
    select {
        @apply text-lg font-medium;
    }
</style>
