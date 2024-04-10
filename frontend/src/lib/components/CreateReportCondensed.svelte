<script>
  import target_icon from '$lib/images/target_icon.png';
  let steps_counter = 0;
</script>
<div>
  <!-- If steps_counter > 0, display steps -->
  {#if steps_counter>0}
    <div class="flex justify-items-center flex-col align-middle mt-5">
      {#if steps_counter===1}
          <ul class="steps sm:steps-vertical lg:steps-horizontal">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
        <div role="button" class="btn btn-xm btn-ghost m-1 btn-circle ">
          <div class="w-5 h-5 rounded-full overflow-hidden">
            <img alt="Theme Icon" src="{target_icon}" />
          </div>
        </div>
      {/if}
      
      {#if steps_counter===2}
          <ul class="steps sm:steps-vertical lg:steps-horizontal">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
      {/if}

      {#if steps_counter===3}
          <ul class="steps sm:steps-vertical lg:steps-horizontal">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step text-sm">Create Report</li>
          </ul>
      {/if}
      {#if steps_counter>=4}
          <ul class="steps sm:steps-vertical lg:steps-horizontal">
            <li class="step step-primary text-sm">Detect Location</li>
            <li class="step step-primary text-sm">Select Category</li>
            <li class="step step-primary text-sm">Upload Photo</li>
            <li class="step step-success text-sm text-success">Create Report</li>
          </ul>
      {/if}
    </div>
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
</style>