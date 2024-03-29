<script lang="ts">
  import { Fa } from '$lib';
  import SvelteKitLogo from '$svg/svelte-kit.svg?component';
  import { faPlus } from '@fortawesome/free-solid-svg-icons';
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4 mt-8">
    Welcome to AveriasPR
    <!-- <div class="relative mt-4 w-min lg:ml-0 lg:mt-0">
      <SvelteKitLogo class="h-12 text-primary lg:h-14" />
    </div> -->
  </div>

  <CreateReportCondensed/>
  
</main>

<style lang="postcss">
  aside {
    @apply my-auto grid grid-cols-1 content-start items-center gap-8 text-center text-2xl;
    @screen lg {
      @apply flex w-full items-center justify-center;
    }
  }
</style>
