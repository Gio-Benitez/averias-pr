<script lang="ts">
  import {buttonNext, steps_counter, forward, backward, reset } from '$lib/stores';
  import ReportForm from './ReportForm.svelte';
  import ReportProgressBar from './ReportProgressBar.svelte';
</script>

<div class="pt-6">
  <!-- Report Steps Progress Bar -->
  <ReportProgressBar />
  <!-- Report Form-->
  <ReportForm />
  <!-- Next, Back, and Cancel Buttons -->
  <div class="mt-5">
    {#if $steps_counter===0}
      <button class="btn btn-success btn-outline" on:click={()=>$steps_counter+=1}>Crear Reporte +</button>
    {:else if $steps_counter ===1}
      <button class="btn btn-sm" on:click={reset}>Cancel</button>
      <button class="btn btn-sm {$buttonNext ? '' : 'btn-disabled'}" on:click={forward}>Next</button>
    {:else if $steps_counter<4}
      <button class="btn btn-sm" on:click={reset}>Cancel</button>
      <button class="btn btn-sm" on:click={backward}>Back</button>
      <button class="btn btn-sm {$buttonNext ? '' : 'btn-disabled'}" on:click={forward}>Next</button>
    {:else if $steps_counter===4}
      <button class="btn btn-sm" on:click={reset}>Cancel</button>
      <button class="btn btn-sm" on:click={backward}>Back</button>
      <button class="btn btn-sm btn-disabled" on:click={forward}>Next</button>
    {/if}
  </div>
</div>


<style>
</style>