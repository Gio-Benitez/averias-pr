<script lang="ts">
    import { Fa } from '$lib';
    import SvelteKitLogo from '$svg/svelte-kit.svg?component';
    import { faPlus } from '@fortawesome/free-solid-svg-icons';
    import Map from '$components/Map.svelte';
    let name = 'world';
  </script>
<main class="flex h-full flex-col gap-8 pb-8 text-center">

    Interactive Map
    <div class="flex items-center justify-center">
        <Map />
    </div>

</main>
    