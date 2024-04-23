<script lang="ts">
  import { MapLibre, GeoJSON, FillLayer, LineLayer, hoverStateFilter, MarkerLayer, Popup } from 'svelte-maplibre';
  import type { Feature } from 'geojson';
  import municipios from '$lib/data/municipios.json';
  import { contrastingColor } from '$lib/site/colors';
  import { mapDataStore } from '$lib/stores';
  

  let showBorder = true;
  let showFill = true;
  let fillColor = '#006600';
  let borderColor = '#003300';
  const mapClasses = 'rounded-lg aspect-auto w-full h-full';

  let map: maplibregl.Map | undefined;
  let loaded: boolean;
  let textLayers: maplibregl.LayerSpecification[] = [];
  $: if (map && loaded) {
    textLayers = map.getStyle().layers.filter((layer: maplibregl.LayerSpecification) => layer['source-layer'] === 'place');
  }

  $: colors = contrastingColor(fillColor);
  $: if (map && loaded) {
    for (let layer of textLayers) {
      map.setPaintProperty(layer.id, 'text-color', colors.textColor);
      map.setPaintProperty(layer.id, 'text-halo-color', colors.textOutlineColor);
    }
  }

  let filterStates = false;
  
  $: filter = filterStates ? ['==', 'T', ['slice', ['get', 'NAME'], 0, 1]] : undefined;

  
  // Values for populating Map Data Panel
  export let clickedFeature: Record<string, any> | null = null;
  function updateDataPanel(clickedFeature) {
    $mapDataStore.dataRegion = clickedFeature?.NAME;
  }
</script>


<MapLibre
  bind:map
  bind:loaded
  style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
  class= {mapClasses}
  standardControls
  center={[-66.41, 18.24]}
  zoom={4}
  maxBounds={[-67.5, 17.8, -65.1, 18.6]}
>
  <GeoJSON id="municipios" data= { municipios } promoteId="NAME">
    {#if showFill}
      <FillLayer
        type="background"
        hoverCursor="pointer"
        paint={{
          'fill-color': hoverStateFilter(fillColor, colors.hoverBgColor),
          'fill-opacity': 0.5
        }}
        {filter}
        beforeLayerType="symbol"
        manageHoverState
        on:click={ (data) => (clickedFeature = data.detail.features?.[0]?.properties) }
    />
    {/if}
    {#if showBorder}
      <LineLayer
        layout={{ 'line-cap': 'round', 'line-join': 'round' }}
        paint={{ 'line-color': borderColor, 'line-width': 3 }}
        beforeLayerType="symbol"
      />
    {/if}

  </GeoJSON>
</MapLibre>

{#if clickedFeature}
  {updateDataPanel(clickedFeature)}
{/if}

<style lang="postcss">

</style>




