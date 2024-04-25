<script lang="ts">
    import { mapDataStore, reportCategories, municipios } from "$lib/stores";
    import { createEventDispatcher } from "svelte";
    
    // Report Category Filter Logic
    let catUnselected: boolean = true;
    let muniUnselected: boolean = true;
    let cat: string = '';
    let muni: string = '';
    const municipalities = $municipios.municipiosArray;
    const categoryArray = $reportCategories.categoryArray;
    function updateRegion (data: any) {
        $mapDataStore.dataRegion = data;
        console.log($mapDataStore.dataRegion);
  }

</script>
<div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 py-8 rounded-2xl">
    <div class="flex flex-col w-full h-1/5 text-center">
        <h1>{$mapDataStore.dataRegion}</h1>
        <div class="divider divider-neutral"></div>
        
        <select class="select text-lg font-medium select-secondary w-full">
            <option disabled selected >Seleccione Categoría</option>
            {#each categoryArray as category}
            <option value={category}>{category}</option>
            {/each}    
        </select>
    </div>
    <div class="flex flex-col w-full text-center">
        <h1>Statistics</h1>
        <div class="divider divider-neutral"></div>
    </div>
    <div class="flex flex-col flex-wrap w-full h-3/5 text-center gap-2">
        <div class="stats stats-vertical shadow">
            <div class="stat shadow-lg">
                <div class="stat-title">Población</div>
                <div class="stat-value">{$mapDataStore.population}</div>
            </div>
            <div class="stat shadow-lg">
                <div class="stat-title">Averías Reportadas</div>
                <div class="stat-value">{$mapDataStore.numOfReports}</div>
            </div>
            <div class="stat shadow-lg">
                <div class="stat-title">Categoría más Común</div>
                <div class="stat-value">{$mapDataStore.reportCategory}</div>
            </div>
            <div class="stat shadow-lg">
                <div class="stat-title">Averías Resueltas</div>
                <div class="stat-value">{$mapDataStore.resolved}</div>
            </div>
        </div>
    </div>
</div>

<style lang="postcss">
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    .stat-title {
        @apply text-lg;
    }
    .stat-value {
        @apply text-2xl;
    }
    option {
        @apply font-medium;
    }
    select {
        @apply text-lg font-medium;
    }
</style>
