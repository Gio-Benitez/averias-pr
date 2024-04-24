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
<div class="flex flex-col flex-wrap w-full h-full bg-primary px-8 py-12 rounded-2xl">
    <div class="flex flex-col w-full h-2/5 text-center gap-1">
        <h1>{$mapDataStore.dataRegion}</h1>
        <div class="divider divider-neutral"></div>
        <select class="select select-secondary w-full">
            <option selected>{$mapDataStore.dataRegion}</option>
            {#each municipalities as municipio}
            <option>{municipio}</option>
            {/each}    
        </select>
        <select class="select text-lg font-medium select-secondary w-full">
            <option disabled selected >Seleccione Categoría</option>
            {#each categoryArray as category}
            <option value={category}>{category}</option>
            {/each}    
        </select>
    </div>
    <div class="flex flex-col w-full h-1/5 text-center">
        <h1>Statistics</h1>
        <div class="divider divider-neutral"></div>
    </div>
    <div class="flex flex-col flex-wrap w-full h-2/5 text-center gap-2">
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title"># of Reports</div>
            <div class="stat-value">{$mapDataStore.numOfReports}</div>
        </div>
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Population</div>
            <div class="stat-value">{$mapDataStore.population}</div>
        </div>
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Report Category</div>
            <div class="stat-value">{$mapDataStore.reportCategory}</div>
        </div> 
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Stat 2</div>
            <div class="stat-value">{$mapDataStore.stat2}</div>
        </div>
    </div>
    
</div>

<style lang="postcss">
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    .stat-title {
        @apply text-primary-content text-lg;
    }
    .stat-value {
        @apply text-primary-content text-2xl;
    }
    option {
        @apply text-base font-medium;
    }
    select {
        @apply text-lg font-medium;
    }
</style>
