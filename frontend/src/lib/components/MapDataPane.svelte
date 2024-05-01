<script lang="ts">
    import { mapDataStore, filterCategoriesStore, municipios, municipalities } from "$lib/stores";
    import { createEventDispatcher } from "svelte";
    import { enhance } from "$app/forms";
    import { page } from "$app/stores";
    
    
    // Report Category Filter Logic
    let catUnselected: boolean = true;
    let muniUnselected: boolean = true;
    let muni: string = '';
    function selectCat (event: any) {
        $mapDataStore.reportCategory = event.target.value;
        catUnselected = false;
        console.log($mapDataStore.reportCategory);
        console.log($page.form);
        
    }
    function updateRegion (data: any) {
        $mapDataStore.dataRegion = data;
        console.log($mapDataStore.dataRegion);
  }

</script>
<div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 py-8 rounded-2xl">
    <div class="flex flex-col w-full h-1/5 text-center">
        <h1>{$mapDataStore.dataRegion}</h1>
        <div class="divider divider-neutral"></div>
        <form action="?/mapCategorySelection" name="category" method="POST">
            <select 
                name="category"
                class="select text-lg font-medium select-secondary w-full"
                value={$mapDataStore.reportCategory} 
                on:change= {selectCat}
                >
                <option disabled selected >Seleccione Categoría</option>
                {#each $filterCategoriesStore as category}
                <option value={category}>{category}</option>
                {/each}    
            </select>
        </form>
    </div>
    <div class="flex flex-col w-full text-center">
        <h1>Statistics</h1>
        <div class="divider divider-neutral"></div>
    </div>
    <div class="flex flex-col flex-wrap w-full text-center gap-2">
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
