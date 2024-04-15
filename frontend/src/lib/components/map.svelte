<script lang="ts">
    import { MapLibre, GeoJSON, FillExtrusionLayer } from 'svelte-maplibre';
    import type { Feature } from 'geojson';
    import municipios from '$lib/data/municipios.json';

</script>


<MapLibre 
  center={[-66.41, 18.24]}
  zoom={6.5}
  class="relative aspect-[9/16] max-h-[70vh] w-[80vw]"
  standardControls
  style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json" 
  maxBounds={[-67.5, 17.8, -65.1, 18.6]}
  
  />

<style>
  :global(.map) {
    height: 600px;
    width: 90%;
  }
</style>




