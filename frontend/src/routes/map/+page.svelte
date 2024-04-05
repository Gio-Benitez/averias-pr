<script lang="ts">
    import Map from '$components/Map.svelte';
    let name = 'world';
  </script>
<svelte:head>
    <!--- To-Do -->
</svelte:head>
<!--Interactive Map Segment-->
<main class="flex h-full  flex-col gap-8 pb-8 text-center">

    Interactive Map
    <div class="grid grid-cols-1 place-content-center">
        <div class="flex justify-center">
            <Map />
        </div>
    </div>
    <div>

    </div>

</main>
    