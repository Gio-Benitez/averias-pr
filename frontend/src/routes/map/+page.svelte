<script lang="ts">
    import { enhance } from '$app/forms';
	import type { PageData, ActionData } from './$types';
    import Map from '$components/Map.svelte';
    import MapDashNav from '$components/MapDashNav.svelte';
    import { mapDataStore, filterCategoriesStore, municipios } from '$lib/stores';
    
    export let data: PageData;
    export let form: ActionData;
    //$mapDataStore.populationData = data.item[1][1];
    let selectedTab = 'map';
    function changeTab(event: MouseEvent) {
        if (selectedTab === 'map') {
            selectedTab = 'dashboard';
        } else if (selectedTab === 'dashboard'){
            selectedTab = 'map';
        }
    }
    // Selectg Category function for map data pane
    let selection = {   
                        region: data.props.mapData.dataRegion, 
                        category: 'Seleccione Categoría'
                    };
    
    let category:string;
    function selectCat (event: any) {
        category = event.target.value;
        console.log(category);
    }
    function updateWithForm (event: any) {
        $mapDataStore.dataRegion = form?.props.mapData.dataRegion as string;
    } 
    // Dashboard Data Panel Logic
    const municipalities = $municipios.municipiosList;
  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>


<main class="grid grid-rows-10 grid-cols-10 h-full w-full gap-8 pb-8">
<!--Tab Implementation to switch between Map and Dashboard Segments-->
    <!--Map and Dashboard Nav Buttons-->
    <MapDashNav />
    <!--Map Component Segment-->
    <div id="map" class="min-h-[697px] col-start-2 col-end-8 row-start-2 row-end-10 mt-3">
        <Map />
    </div>
    <!--Map Data Panel Segment-->
    <div id="dataPane" class="min-w-72 min-h-[697px] col-start-8 col-end-10 row-start-2 row-end-10">
        <div class="flex flex-col flex-wrap gap-4  w-full h-full bg-primary px-8 py-2 rounded-2xl">
            <div class="flex flex-col w-full text-center">
                
                <h1>{$mapDataStore.dataRegion}</h1>
                
                <div class="divider divider-neutral"></div>
                <form action="?/mapCategorySelection" method="POST" class="flex flex-col" use:enhance>
                    <!-- Region input -->
                    <input type="hidden" name="region" value={$mapDataStore.dataRegion}>
                    <!-- Category Select -->
                    <select name="category" class="select text-lg font-medium select-secondary w-full">
                        <option disabled selected >Seleccione Categoría</option>
                        {#each $filterCategoriesStore as category}
                        <option value={category}>{category}</option>
                        {/each}    
                    </select>
                    <!-- Submit Button -->
                    <button type="submit" class="btn">Filtrar</button>
                </form>
            </div>
            <div class="flex flex-col w-full text-center">
                <h1>Statistics</h1>
                <div class="divider divider-neutral"></div>
            </div>
            {#if !form && data}
            <div class="flex flex-col flex-wrap w-full text-center gap-0">
                <div class="stats stats-vertical shadow">
                    <div class="stat shadow-lg">
                        <div class="stat-title">Población</div>
                        <div class="stat-value">{data.props.mapData.population}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Averías Reportadas</div>
                        <div class="stat-value">{data.props.mapData.numOfReports}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Categoría más Común</div>
                        <div class="stat-value">{data.props.mapData.reportCategory}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Averías Resueltas</div>
                        <div class="stat-value">{data.props.mapData.resolved}</div>
                    </div>
                </div>
            </div>
            {:else if form}
            <div class="flex flex-col flex-wrap w-full text-center gap-2">
                <div class="stats stats-vertical shadow">
                    <div class="stat shadow-lg">
                        <div class="stat-title">Población</div>
                        <div class="stat-value">{form.props.mapData.population}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Averías Reportadas</div>
                        <div class="stat-value">{form.props.mapData.numOfReports}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Categoría más Común</div>
                        <div class="stat-value">{form.props.mapData.reportCategory}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title">Averías Resueltas</div>
                        <div class="stat-value">{form.props.mapData.resolved}</div>
                    </div>
                </div>
            </div>
            {/if}
        </div>
    </div>
</main>

<style lang="postcss">
    button {
        @apply  btn-md text-primary font-medium text-lg;
    }
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    h2 {
        @apply text-primary-content text-lg font-medium;
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
        @apply select select-secondary w-full text-lg font-medium;
    }
    
</style>