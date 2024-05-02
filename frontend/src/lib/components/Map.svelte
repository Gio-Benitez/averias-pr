<script lang="ts">
  import { MapLibre, GeoJSON, FillLayer, LineLayer, hoverStateFilter, MarkerLayer, Popup, FillExtrusionLayer } from 'svelte-maplibre';
  import type { Feature } from 'geojson';
  import municipios from '$lib/data/municipios.json';
  import { contrastingColor } from '$lib/site/colors';
  import { mapDataStore } from '$lib/stores';
  import { lab, type LabColor } from 'd3-color';
  
  
  let showBorder = true;
  let showFill = true;
  let fillColor = '#006600';
  let borderColor = '#003300';
  let alternateFillColor = '#002604';
  let mapCenter: [number, number] = [-66.41, 18.24];
  let zoomLevel = 4;
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
  
  // Values for populating Map Data Panel
  // 
  let clickedFeature: Record<string, any> | null = null;
  let municipioClicked: Boolean = true;
  
  map?.on('click', function(e) {
	    // When the map is clicked, get the geographic coordinate.
	    let coordinate = map?.unproject(e.point);
	    console.log(coordinate);
      map?.flyTo({center: coordinate, zoom: 11});
  });
  function regionHandler (data: any) {
    clickedFeature = data.detail.features?.[0];
    let clickedName = clickedFeature?.properties.NAME;
    $mapDataStore.dataRegion = clickedFeature?.properties.NAME;
    municipioClicked = true;
    console.log(clickedName);
  }
  $: map?.on('click', function(e) {
      
	    // When the map is clicked, get the geographic coordinate.
	    let coordinate = map?.unproject(e.point);
      if (municipioClicked == true) {
        map?.flyTo({center: coordinate, zoom: 11});
        municipioClicked = false;
      }
  });

  // Changing Basemap color
  let selected: 'light' | 'dark' = 'light';
  $: style =
    selected === 'light'
      ? 'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json'
      : 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json';
  
  $: filter = filterMunicipio ? ['==', clickedFeature?.NAME, ['Arecibo']] : undefined;

</script>

<MapLibre
  bind:map
  bind:loaded
  {style}
  class= {mapClasses}
  standardControls
  center={mapCenter}
  zoom={zoomLevel}
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
        
        on:click={ (data, map) => regionHandler(data, map) }
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
<div class="controls">
  <select class="select" bind:value={selected}>
    <option value="light">Light</option>
    <option value="dark">dark</option>
  </select>
</div>

<style lang="postcss">

</style>




