<script>
  let steps_counter = 1;
</script>
<div>
  <!-- If steps_counter > 0, display steps -->
  {#if steps_counter>0}
    <ul class="steps sm:steps-vertical lg:steps-horizontal">
      {#if steps_counter===1}
        <li class="step step-primary text-sm">Detect Location</li>
        <li class="step text-sm">Select Category</li>
        <li class="step text-sm">Upload Photo</li>
        <li class="step text-sm">Create Report</li>
      {/if}
      
      {#if steps_counter===2}
        <li class="step step-primary text-sm">Detect Location</li>
        <li class="step step-primary text-sm">Select Category</li>
        <li class="step text-sm">Upload Photo</li>
        <li class="step text-sm">Create Report</li>
      {/if}

      {#if steps_counter===3}
        <li class="step step-primary text-sm">Detect Location</li>
        <li class="step step-primary text-sm">Select Category</li>
        <li class="step step-primary text-sm">Upload Photo</li>
        <li class="step text-sm">Create Report</li>
      {/if}
      {#if steps_counter>=4}
        <li class="step step-primary text-sm">Detect Location</li>
        <li class="step step-primary text-sm">Select Category</li>
        <li class="step step-primary text-sm">Upload Photo</li>
        <li class="step step-success text-sm text-success">Create Report</li>
      {/if}
    </ul>
  {/if}
  <!-- Steps Buttons -->
  <div>
    {#if steps_counter===0}
      <button class="btn" on:click={()=>steps_counter+=1}>Create Report</button>
    {:else if steps_counter ===1}
      <button class="btn" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn" on:click={()=>steps_counter += 1}>Next</button>
    {:else if steps_counter<4}
      <button class="btn" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn" on:click={()=>steps_counter -= 1}>Back</button>
      <button class="btn" on:click={()=>steps_counter += 1}>Next</button>
    {:else}
      <button class="btn" on:click={()=>steps_counter = 0}>Cancel</button>
      <button class="btn" on:click={()=>steps_counter -= 1}>Back</button>
      <button class="btn">Submit</button>
    {/if}
  </div>
</div>


  