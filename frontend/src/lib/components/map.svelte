<script lang="ts">
    import { MapLibre, GeoJSON, FillLayer, LineLayer, hoverStateFilter } from 'svelte-maplibre';
    import type { Feature } from 'geojson';
    import municipios from '$lib/data/municipios.json';
    import { contrastingColor } from '$lib/site/colors';
    import { mapClasses } from '$lib/styles';

    let showBorder = true;
    let showFill = true;
    let fillColor = '#006600';
    let borderColor = '#003300';

    // START EXTRACT
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
  // END EXTRACT
</script>


<MapLibre
  bind:map
  bind:loaded
  style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
  class={mapClasses}
  standardControls
  center={[-98.137, 40.137]}
  zoom={4}
>
  <GeoJSON id="municipios" data= { municipios } promoteId="STATEFP">
    {#if showFill}
      <FillLayer
        paint={{
          'fill-color': hoverStateFilter(fillColor, colors.hoverBgColor),
          'fill-opacity': 0.5,
        }}
        {filter}
        beforeLayerType="symbol"
        manageHoverState
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

<style>
  :global(.map) {
    height: 600px;
    width: 90%;
  }
</style>




