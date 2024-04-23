<script lang="ts">
	import type { PageData } from './$types';
	import MapDataPane from '$components/MapDataPane.svelte';
    import Map from '$components/Map.svelte';
    import DashboardPanel from '$components/DashboardPanel.svelte';
    import DashboardDataPanel from '$components/DashboardDataPanel.svelte';
    import { mapDataStore } from '$lib/stores';

    //export let data: PageData;
    //$mapDataStore.populationData = data.item[1][1];
    let selectedTab = 'map';
    function changeTab(event: MouseEvent) {
        if (selectedTab === 'map') {
            selectedTab = 'dashboard';
        } else if (selectedTab === 'dashboard'){
            selectedTab = 'map';
        }
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
        <div id="map" class="col-start-2 col-end-8 row-start-2 row-end-10">
            <Map />
        </div>
        <!--Map Data Panel Segment-->
        <div id="dataPane" class="min-w-72 col-start-8 col-end-10 row-start-2 row-end-10">
            <MapDataPane />
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
        <div id="dashboard" class="col-start-2 col-end-8 row-start-2 row-end-10">
            <DashboardPanel />
        </div>
        <!--Dashboard Data Panel Segement-->
        <div id="dataPanelSlot" class="min-w-72 min-h-fit col-start-8 col-end-10 row-start-2 row-end-10">
            <DashboardDataPanel />
        </div>
    {/if}
</main>

<style lang="postcss">
    button {
        @apply font-black text-3xl text-left;
    }

</style>