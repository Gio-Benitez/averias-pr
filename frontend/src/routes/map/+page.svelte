<script lang="ts">
	import type { PageData } from './$types';
	import MapDataPane from '$components/MapDataPane.svelte';
    import Map from '$components/Map.svelte';
    import mapDataStore from '$lib/stores';

    export let data: PageData;
    $mapDataStore.populationData = data.item[1][1];

  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>
<!--Interactive Map Segment-->
<main class="grid grid-rows-9 grid-cols-10 grid-flow-auto h-full gap-8 pb-8">

    <h1 class="col-span-1 row-span-1 col-start-5 col-end-6 row-start-1">Interactive Map</h1>
    <div id="map" class="col-start-2 col-end-8 row-start-2 row-end-9">
        <Map />
    </div>
    <div id="dataPane" class="flex aspect-auto col-span-2 col-start-8 row-start-2 row-end-9">
        <MapDataPane />
    </div>

</main>

<style>
    
</style>