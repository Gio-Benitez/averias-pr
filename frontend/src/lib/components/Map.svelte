<script lang="ts">
  import { MapLibre, GeoJSON, FillLayer, LineLayer, hoverStateFilter, MarkerLayer, Popup, FillExtrusionLayer } from 'svelte-maplibre';
  import type { Feature } from 'geojson';
  import municipios from '$lib/data/municipios.json';
  import { contrastingColor } from '$lib/site/colors';
  import { mapDataStore } from '$lib/stores';
  

  let showBorder = true;
  let showFill = true;
  let fillColor = '#006600';
  let borderColor = '#003300';
  const mapClasses = 'rounded-2xl aspect-auto w-full h-full';

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

  let filterMunicipio = false;
  
  $: filter = filterMunicipio ? ['==', clickedFeature?.NAME, ['Arecibo']] : undefined;

  
  // Values for populating Map Data Panel
  let clickedFeature: Record<string, any> | null = null;

  function regionHandler (data: any) {
    clickedFeature = data.detail.features?.[0]?.properties
    $mapDataStore.dataRegion = clickedFeature?.NAME;
    console.log(clickedFeature);
    console.log($mapDataStore.dataRegion);
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
        on:click={ (data) => regionHandler(data) }
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


<style lang="postcss">

</style>




