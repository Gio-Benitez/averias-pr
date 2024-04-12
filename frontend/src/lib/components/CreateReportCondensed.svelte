<script lang="ts">
  import target_icon from '$lib/images/target_icon.png';
  import { getUserLocation } from "$lib/geolocation";
  import { DefaultMarker, MapLibre, Popup} from 'svelte-maplibre'
  // import { LngLat } from 'maplibre-gl';

  // Define type for GeoJSON Point
  interface GeoJSONPoint {
    type: string;
    coordinates: [number, number];
  }

  let userLocation: GeoJSONPoint | null = null;

  let errorMessage: string | null = null;

  async function fetchUserLocation() {
    try {
      userLocation = await getUserLocation();
      errorMessage = null; // Reset error message on success
      // let ll = new LngLat(userLocation?.coordinates[0],userLocation?.coordinates[1]);
    } catch (error) {
      if (error instanceof Error) {
        errorMessage = error.message;
      } else {
        errorMessage = "An unknown error occurred.";
      }
      console.error(errorMessage);
    }
  }
  
  
  let steps_counter = 1;
    

</script>
<div>
  <!-- If steps_counter > 0, display steps -->
  {#if steps_counter>0}
    <!-- <div class="flex flex-col mt-5"> -->
      {#if steps_counter===1}
        <div class="flex justify-center w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
        </div>
        <button class="btn btn-lg btn-square btn-primary m-1 mt-20" on:click={fetchUserLocation}>
          <div class="w-20 h-20 overflow-hidden">
            <img alt="Theme Icon" src="{target_icon}" />              
          </div>
        </button>
        <span>Press to detect location</span>
        {#if userLocation}
          <div>
            <MapLibre
              center={[userLocation ? userLocation.coordinates[0] : 0, userLocation ? userLocation.coordinates[1] : 0]}
              zoom={14}
              class="map"
              style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
              maxBounds={[-67.5, 17.8, -65.1, 18.6]}
            >
              <!-- <DefaultMarker {ll} draggable>
                <Popup offset={[0, -10]}>
                  <div class="text-lg font-bold">{"You are here"}</div>
                </Popup>
              </DefaultMarker> -->
            </MapLibre>
          </div>
          <pre>{JSON.stringify(userLocation, null, 2)}</pre>
        {:else}
          <p>No location available</p>
        {/if}
      {/if}
      
      {#if steps_counter===2}
          <ul class="steps sm:steps-vertical lg:steps-horizontal" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
      {/if}

      {#if steps_counter===3}
          <ul class="steps sm:steps-vertical lg:steps-horizontal" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
      {/if}
      {#if steps_counter>=4}
          <ul class="steps sm:steps-vertical lg:steps-horizontal" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step step-success text-sm text-success">Create Report</li>
          </ul>
      {/if}
    <!-- </div> -->
  {/if}
  <!-- Steps Buttons -->
  <div class="mt-5">
    {#if steps_counter===0}
      <button class="btn btn-success btn-outline" on:click={()=>steps_counter+=1}>Create Report +</button>
    {:else if steps_counter ===1}
      <button class="btn btn-sm" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn btn-sm" on:click={()=>steps_counter += 1}>Next</button>
    {:else if steps_counter<4}
      <button class="btn btn-sm" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn btn-sm" on:click={()=>steps_counter -= 1}>Back</button>
      <button class="btn btn-sm" on:click={()=>steps_counter += 1}>Next</button>
    {:else}
      <button class="btn btn-sm" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn btn-sm" on:click={()=>steps_counter -= 1}>Back</button>
      <button class="btn btn-success">Submit</button>
    {/if}
  </div>
</div>


<style>
  .container {
    display: flex;
    flex-direction: column; /* Stack items vertically */
    /* justify-content: center; /* Align items vertically in the center */
    /*align-items: center; Align items horizontally in the center */
  }
  :global(.map) {
    height: 200px;
    width: 35%;
  }
</style>