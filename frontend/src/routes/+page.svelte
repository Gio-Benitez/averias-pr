<script lang="ts">
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
  export let form;
</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4 mt-8 mb-10">
    Welcome to AveriasPR
  </div>

  <CreateReportCondensed/>
  
  {#if form?.message}
        <p class="text-red-500 font-semibold">{form.message}</p>
  {/if}
</main>

<style lang="postcss">
  aside {
    @apply my-auto grid grid-cols-1 content-start items-center gap-8 text-center text-2xl;
    @screen lg {
      @apply flex w-full items-center justify-center;
    }
  }
</style>
