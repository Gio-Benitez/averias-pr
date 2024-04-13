<script lang="ts">
    import { MapLibre} from 'svelte-maplibre'
    import { GeoJSON, FillExtrusionLayer, Popup } from 'svelte-maplibre'
</script>


<MapLibre 
center={[-66.41, 18.24]}
zoom={6.5}
class="map"
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




