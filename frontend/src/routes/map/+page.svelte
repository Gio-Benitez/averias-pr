<script lang="ts">
	import { page } from '$app/stores';
    import { enhance } from '$app/forms';
	import type { PageData, ActionData } from './$types';
    import Map from '$components/Map.svelte';
    import MapDashNav from '$components/MapDashNav.svelte';
    import { mapDataStore, filterCategoriesStore, municipios } from '$lib/stores';
    
    export let data: PageData;
    export let form: ActionData; 

    // Select Category function for map data pane
    const mapStats = data.props.mapStatistics;
    console.log(mapStats);
    let category:string;
    let catSelected = false;
    let panelValues:string;

    function selectCat (event: any) {
        category = event.target.value;
        catSelected = true;
        panelValues = mapStats[$mapDataStore.dataRegion].categories[category];
        console.log(category);
        console.log(mapStats[$mapDataStore.dataRegion].categories[category]);
    }

    function updateWithForm (event: any) {
        $mapDataStore.dataRegion = form?.props.mapData.dataRegion as string;
    } 
    function panelReset () {
        $mapDataStore.dataRegion = "Puerto Rico";
        catSelected = false;
        category = "";
    }
    // Dashboard Data Panel Logic
    const municipalities = $municipios.municipiosList;
  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>


<main class="grid grid-cols-10 h-full w-full gap-8 pb-8">
<!--Tab Implementation to switch between Map and Dashboard Segments-->
    <!--Map and Dashboard Nav Buttons-->
    <!--Map Component Segment-->
    <div id="map" class="flex flex-col min-h-[697px] col-start-2 col-end-8 ">
        <MapDashNav />
        <Map />
    </div>
    <!--Map Data Panel Segment-->
    <div id="dataPane" class="min-w-72 my-12 min-h-[697px] col-start-8 col-end-10">
        <div class="flex flex-row flex-wrap gap-4 min-w-[320px] w-full h-full bg-primary px-8 py-2 rounded-2xl">
            <div class="flex flex-col w-full text-center">
                
                <h1>{$mapDataStore.dataRegion}</h1>
                
                <div class="divider divider-neutral"></div>
                    <div class="flex items-center flex-col gap-2">
                        <select name="category" on:change={selectCat} class="select text-lg font-medium select-secondary w-full">
                            <option disabled selected >Seleccione Categoría</option>
                            {#each $filterCategoriesStore as category}
                            <option value={category}>{category}</option>
                            {/each}    
                        </select>
                        <button name="reset" on:click={panelReset}>Restaurar</button>
                        
                    </div>
            </div>
            <div class="flex flex-col w-full text-center">
                <h1>Statistics</h1>
                <div class="divider divider-neutral"></div>
            </div>
            {#if !catSelected}
            <div class="flex flex-col w-full text-center gap-0">
                <div class="stats stats-vertical shadow">
                    <div class="stat shadow-lg">
                        <div class="stat-title   lg:text-lg">Población</div>
                        <div class="stat-value   lg:text-xl">{mapStats[$mapDataStore.dataRegion].population}</div>
                    </div>  
                    <div class="stat shadow-lg">
                        <div class="stat-title  lg:text-lg">Categoría más Común</div>
                        <div class="stat-value  lg:text-xl">{mapStats[$mapDataStore.dataRegion].most_common_category}</div>
                    </div>  
                    <div class="stat shadow-lg">
                        <div class="stat-title  lg:text-lg">Averías Reportadas</div>
                        <div class="stat-value  lg:text-xl">{mapStats[$mapDataStore.dataRegion].num_reports}</div>
                    </div>  
                    <div class="stat shadow-lg">
                        <div class="stat-title  lg:text-lg">Averías Resueltas</div>
                        <div class="stat-value  lg:text-xl">{mapStats[$mapDataStore.dataRegion].resolved_reports}</div>
                    </div>
                </div>
            </div>
            {:else if catSelected}
            <div class="flex flex-col w-full text-center gap-0">
                <div class="stats stats-vertical shadow">
                    <div class="stat shadow-lg">
                        <div class="stat-title lg:text-lg">Población</div>
                        <div class="stat-value lg:text-xl">{mapStats[$mapDataStore.dataRegion].population}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title lg:text-lg">Categoría Seleccionada</div>
                        <div class="stat-value lg:text-xl">{category}</div>
                    </div>
                    <div class="stat shadow-lg">
                        <div class="stat-title lg:text-lg">Averías Reportadas</div>
                        <div class="stat-value lg:text-xl">{mapStats[$mapDataStore.dataRegion].categories[category].total}</div>
                    </div>
                    <div class="stat shadow-lg ">
                        <div class="stat-title lg:text-lg">Averías Resueltas</div>
                        <div class="stat-value lg:text-xl">{mapStats[$mapDataStore.dataRegion].categories[category].resolved}</div>
                    </div>
                </div>
            </div>
            {/if}
        </div>
    </div>
</main>

<style lang="postcss">
    main {
        min-height: 100vh;
        overflow: scroll;
    }
    button {
        @apply  btn-md bg-primary-content rounded-lg w-1/2 text-primary  font-medium text-lg;
    }
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    h2 {
        @apply text-primary-content text-lg font-medium;
    }
    .stat-title {
        @apply font-semibold text-base;
    }
    .stat-value {
        @apply font-bold text-lg;
    }
    option {
        @apply font-medium;
    }
    select {
        @apply select select-secondary w-full text-lg font-medium;
    }
    .stats {
        @apply w-min;
    }
    
</style>