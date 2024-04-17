<script lang="ts">
    import { onMount, onDestroy } from 'svelte'
    import maplibregl from 'maplibre-gl';
    import 'maplibre-gl/dist/maplibre-gl.css';

    let map: maplibregl.Map | undefined;
    let mapContainer: HTMLElement | null;

    const apiKey = "N6k7AWVqyqCyOnsm59er";

    onMount(() => {
        const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

        map = new maplibregl.Map({
            container: mapContainer instanceof HTMLElement ? mapContainer : '',
            style: `https://api.maptiler.com/maps/streets-v2/style.json?key=N6k7AWVqyqCyOnsm59er`,
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom
        });

    });
    

    onDestroy(() => {
        map?.remove();
    });
</script>

<div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"><img
      src="https://api.maptiler.com/resources/logo.svg" alt="MapTiler logo"/></a>
    <div bind:this={mapContainer} class="map">
        {#if mapContainer !== null}
            <div id="map" style="width: 100%; height: 100%;"></div>
        {/if}
    </div>
  </div>

  <style>
    .map-wrap {
      position: relative;
      width: 100%;
    }
  
    .map {
      position: absolute;
      width: 100%;
      height: 100%;
    }
  
    .watermark {
      position: absolute;
      left: 10px;
      bottom: 10px;
      z-index: 999;
    }
  </style>



