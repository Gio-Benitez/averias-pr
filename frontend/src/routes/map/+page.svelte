<script lang="ts">
    import Map from '$components/Map.svelte';
    let name = 'world';
  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>
<!--Interactive Map Segment-->
<main class="flex h-full flex-col gap-8 pb-8 text-center object-center">

    <h1>Interactive Map</h1>
    <div id="map" class="flex  h-2/3 w-3/4 justify-center content-center">
        <Map />
    </div>

</main>

<style>
    
</style>