<script lang="ts">
    import { enhance } from '$app/forms';
	import type { PageData, ActionData } from './$types';
	import MapDataPane from '$components/MapDataPane.svelte';
    import Map from '$components/Map.svelte';
    import DashboardPanel from '$components/DashboardPanel.svelte';
    import DashboardDataPanel from '$components/DashboardDataPanel.svelte';
    import { mapDataStore, filterCategoriesStore } from '$lib/stores';
    import TestChart from '$components/TestChart.svelte';
    
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

    function selectCat (event: any) {
        selection.category = event.target.value;
    }
  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>


<main class="grid grid-rows-10 grid-cols-10 h-full w-full gap-8 pb-8">
<!--Tab Implementation to switch between Map and Dashboard Segments-->
    {#if selectedTab === 'map'}
        <!--Map and Dashboard Nav Buttons-->
        <div class="flex pt-12 pl-0 space-x-2 col-span-3 row-span-1 col-start-2 row-start-1 ">
            <div class="flex shrink-0 h-full">
                <div class="tabs-lifted tabs-lg w-full h-full" >
                    <button on:click={changeTab} class="tab tab-active">Interactive Map</button>
                    <button on:click={changeTab} class="tab">Dashboard</button>
                </div>
            </div>
        </div>
        <!--Map Component Segment-->
        <div id="map" class="min-h-[697px] col-start-2 col-end-8 row-start-2 row-end-10">
            <Map />
        </div>
        <!--Map Data Panel Segment-->
        <div id="dataPane" class="min-w-72 min-h-[697px] col-start-8 col-end-10 row-start-2 row-end-10">
            <div class="flex flex-col flex-wrap gap-4  w-full h-full bg-primary px-8 py-2 rounded-2xl">
                <div class="flex flex-col w-full text-center">
                    <h1>{$mapDataStore.dataRegion}</h1>
                    <div class="divider divider-neutral"></div>
                    <form action="?/mapCategorySelection" name="selection" method="POST" class="flex flex-col" use:enhance>
                        <select
                            name="category" 
                            class="select text-lg font-medium select-secondary w-full"
                            value={selection.category} 
                            on:change= {selectCat}
                            >
                            <option disabled selected >Seleccione Categoría</option>
                            {#each $filterCategoriesStore as category}
                            <option value={category}>{category}</option>
                            {/each}    
                        </select>
                        <input type="hidden" id="region" name="region" value={$mapDataStore.dataRegion}>
                        <button type="submit"  class="btn">Filtrar</button>
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
    {:else if selectedTab === 'dashboard'}
        <!--Map and Dashboard Nav Buttons-->
        <div class="flex pt-12 pl-0 space-x-2 col-span-3 row-span-1 col-start-2 row-start-1 ">
            <div class="flex shrink-0 h-full">
                <div class="tabs-lifted tabs-lg w-full h-full ">
                    <button on:click={changeTab} class="tab">Interactive Map</button>
                    <button on:click={changeTab} class="tab tab-active">Dashboard</button>
                </div>
            </div>
        </div>
        <!--Dashboard Component Segment-->
        <div id="dashboard" class="min-h-[697px] col-start-2 col-end-8 row-start-2 row-end-10">
            <DashboardPanel />
        </div>
        <!--Dashboard Data Panel Segement-->
        <div id="dataPanelSlot" class="min-w-72 min-h-[697px] col-start-8 col-end-10 row-start-2 row-end-10">
            <DashboardDataPanel />
        </div>
    {/if}
</main>

<style lang="postcss">
    button {
        @apply  btn-md  text-primary font-medium text-lg;
    }
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