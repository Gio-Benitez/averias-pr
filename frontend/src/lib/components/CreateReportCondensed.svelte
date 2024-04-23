<script lang="ts">
  import target_icon from '$lib/images/target_icon.png';
  import check_mark from '$lib/images/green_checkmark.png';
  import { getUserLocation } from "$lib/geolocation";
  import { fade } from 'svelte/transition';
  import { municipalities } from '$lib/stores';
  import { onMount } from 'svelte';
  import CategoryIconCloud from './CategoryIconCloud.svelte';

  let municipalityNames: string[] = [];
  let next = false;
  let selectedMunicipality = '¿En qué municipio se encuentra?';
  let userLocation: GeoJSONPoint | null = null;
  let errorMessage: string | null = null;  
  let steps_counter = 0;

  // Define type for GeoJSON Point
  interface GeoJSONPoint {
    type: string;
    coordinates: [number, number];
  }

  function reset() {
    steps_counter = 0;
    next = false;
    userLocation = null;
  }

  // Handler for when you press next button
  function forward() {
    steps_counter += 1;
    next = false;
  }

  // Handler for when you press back button
  function backward() {
    steps_counter -= 1;
    next = true;
  }

  onMount(() => {
    municipalities.subscribe((value: string[]) => {
      municipalityNames = value;
    });
  });

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
  // $: console.log("selectedMunicipality:", selectedMunicipality);
  $: if (selectedMunicipality != '¿En qué municipio se encuentra?') {
    next = true;
  }
</script>

<div class="pt-6 ml-12">
  <!-- If steps_counter > 0, display steps -->
  {#if steps_counter>0}
    <!-- <div class="flex flex-col mt-5"> -->
      {#if steps_counter===1}
        <div class="flex justify-center align-middle w-full">
          <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detectar Ubicación</li>
            <li class="step text-sm">Seleccionar Categoría</li>
            <li class="step text-sm">Subir Imágen</li>
            <li class="step text-sm">Crear Reporte</li>
          </ul>
        </div>
        <div class="flex flex-row justify-center pt-10 pb-20">
          <div class="w-1/2">
            <button class="btn btn-lg btn-square btn-primary m-1 mt-20" on:click={fetchUserLocation}>
              <div class="w-20 h-20 overflow-hidden">
                <img alt="Theme Icon" src="{target_icon}" />              
              </div>
              {#if !userLocation}
                Presione para detectar su ubicación
              {:else}
                <img class="transition-opacity duration-1000 ease-in-out" alt="Check Mark Icon" src="{check_mark}" transition:fade /> 
              {/if}
            </button>
          </div>
          {#if userLocation}
            <div class="w-1/2 flex flex-col">
              <select class="select select-bordered w-full max-w-xs mt-auto transition-opacity duration-1000 ease-in-out" bind:value={selectedMunicipality} transition:fade>
                <option disabled selected>¿En qué municipio se encuentra?</option>
                {#each municipalityNames as muni}
                  <option value={muni}>{muni}</option>
                {/each}
              </select>
            </div>
          {/if}
          <!-- <pre>{JSON.stringify(userLocation, null, 2)}</pre> -->
        </div>
    {/if}
      
    {#if steps_counter===2}
      <div class="flex justify-center w-full">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
          <li class="step step-primary text-sm">Detectar Ubicación</li>
          <li class="step step-primary text-sm">Seleccionar Categoría</li>
          <li class="step text-sm">Subir Imágen</li>
          <li class="step text-sm">Crear Reporte</li>
        </ul>
      </div>
      <div class="mb-40 mt-20">
        <CategoryIconCloud />
      </div>
    {/if}

    {#if steps_counter===3}
      <div class="flex justify-center w-full">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
          <li class="step step-primary text-sm">Detectar Ubicación</li>
          <li class="step step-primary text-sm">Seleccionar Categoría</li>
          <li class="step step-primary text-sm">Subir Imágen</li>
          <li class="step text-sm">Crear Reporte</li>
        </ul>
      </div>
    {/if}
    {#if steps_counter>=4}
      <div class="flex justify-center w-full">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
          <li class="step step-primary text-sm">Detectar Ubicación</li>
          <li class="step step-primary text-sm">Seleccionar Categoría</li>
          <li class="step step-primary text-sm">Subir Imágen</li>
          <li class="step step-success text-sm text-success">Crear Reporte</li>
        </ul>
      </div>
    {/if}

  {/if}
  <!-- Steps Buttons -->
  <div class="mt-5">
    {#if steps_counter===0}
      <button class="btn btn-success btn-outline" on:click={()=>steps_counter+=1}>Crear Reporte +</button>
    {:else if steps_counter ===1}
      <button class="btn btn-sm" on:click={reset}>Cancel</button>
      <button class="btn btn-sm {next ? '' : 'btn-disabled'}" on:click={forward}>Next</button>
    {:else if steps_counter<4}
      <button class="btn btn-sm" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn btn-sm" on:click={backward}>Back</button>
      <button class="btn btn-sm {next ? '' : 'btn-disabled'}" on:click={forward}>Next</button>
    {:else}
      <button class="btn btn-sm" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn btn-sm" on:click={backward}>Back</button>
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