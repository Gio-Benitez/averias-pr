<script lang>
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
  import { signedIn, isModalOpen } from '$lib/signinGlobalVars';
  export let form;
</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4 mt-8 mb-10">
    Welcome to AveriasPR
  </div>
  
  {#if form?.success}
    {signedIn.set(true)}
  {:else}
    {#if form?.message}
          {isModalOpen.set(true)}
          <p class="text-red-500 font-semibold">{form.message}</p>
    {/if}
  {/if}
  <CreateReportCondensed/>
  
</main>

