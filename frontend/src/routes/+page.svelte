<script lang="ts">
  import { Fa } from '$lib';
  import SvelteKitLogo from '$svg/svelte-kit.svg?component';
  import { faPlus } from '@fortawesome/free-solid-svg-icons';
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

  <aside>
    Get started by editing
    <div class="mockup-code mx-auto w-min bg-secondary text-secondary-content lg:mx-0">
      <pre data-prefix="∟" class="whitespace-nowrap">
                <code>src/routes/+page.svelte</code>
      </pre>
    </div>
    <div class="mockup-code mx-auto w-min bg-secondary text-secondary-content lg:mx-0">
      <pre data-prefix="∟" class="whitespace-nowrap">
                <code>src/routes/map/+page.svelte</code>
      </pre>
    </div>
  </aside>
</main>

<style lang="postcss">
  aside {
    @apply my-auto grid grid-cols-1 content-start items-center gap-8 text-center text-2xl;
    @screen lg {
      @apply flex w-full items-center justify-center;
    }
  }
</style>
