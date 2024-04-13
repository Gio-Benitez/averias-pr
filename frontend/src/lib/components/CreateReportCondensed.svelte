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

  function reset() {
    steps_counter = 0;
    userLocation = null;
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
  
  
  let steps_counter = 0;
    

</script>
<div class="pt-6 ml-12">
  <!-- If steps_counter > 0, display steps -->
  {#if steps_counter>0}
    <!-- <div class="flex flex-col mt-5"> -->
      {#if steps_counter===1}
        <div class="flex justify-center align-middle w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
        </div>
        <div class="flex flex-row justify-center pt-10">
          <div class="w-1/2">
          <button class="btn btn-lg btn-square btn-primary m-1 mt-20" on:click={fetchUserLocation}>
            <div class="w-20 h-20 overflow-hidden">
              <img alt="Theme Icon" src="{target_icon}" />              
            </div>
            {#if !userLocation}
              Press to detect location
            {/if}
          </button>
          </div>
          {#if userLocation}
            <div class="map-container flex justify-center align-middle w-1/2">
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
            <!-- <pre>{JSON.stringify(userLocation, null, 2)}</pre> -->
          {/if}
        </div>
        
      {/if}
      
      {#if steps_counter===2}
        <div class="flex justify-center w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
        </div>
      {/if}

      {#if steps_counter===3}
        <div class="flex justify-center w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
        </div>
      {/if}
      {#if steps_counter>=4}
        <div class="flex justify-center w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step step-success text-sm text-success">Create Report</li>
          </ul>
        </div>
      {/if}
    <!-- </div> -->
  {/if}
  <!-- Steps Buttons -->
  <div class="mt-5">
    {#if steps_counter===0}
      <button class="btn btn-success btn-outline" on:click={()=>steps_counter+=1}>Create Report +</button>
    {:else if steps_counter ===1}
      <button class="btn btn-sm" on:click={reset}>Cancel</button>
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
  :global(.map) {
    height: 200px;
    width: 35%;
  }

  .map-container {
    flex-grow: 1;
    min-width: 0;
  }
  .rounded-border {
    border-radius: 10px; /* Adjust the value to change the roundness of the border */
    border: 1px solid #ccc; /* Optionally, you can add a border for visual clarity */
    padding: 10px; /* Optionally, add padding to create space inside the element */
  }
</style>