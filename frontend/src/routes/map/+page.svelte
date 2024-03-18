<script lang="ts">
    import { Fa } from '$lib';
    import SvelteKitLogo from '$svg/svelte-kit.svg?component';
    import { faPlus } from '@fortawesome/free-solid-svg-icons';
    import Map from '$components/Map.svelte';
  </script>
<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4">
    Welcome to
    <div class="relative mt-4 w-min lg:ml-0 lg:mt-0">
      <SvelteKitLogo class="h-12 text-primary lg:h-14" />
      <a
        href="https://daisyui.com"
        class="link-hover link absolute -right-1 bottom-0 flex w-max translate-y-[120%] items-center justify-center text-sm">
        <Fa icon={faPlus} class="mr-2 h-3" /> daisyUI!🌻
      </a>
    </div>
  </div>

    Interactive Map
    <div>
        <Map />
    </div>

</main>
    