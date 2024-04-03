<script>
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
  import { invalidAuth, isModalOpen, signedIn } from '$lib/stores';

  /** @type {import('./$types').PageData} */
	export let data;

  if (data.access) {
    signedIn.set(true)
  }
  else if (data.failedAuth) {
    isModalOpen.set(true);
    invalidAuth.set(true);
  }

</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4 mt-8 mb-10">
    Welcome to AveriasPR
  </div>
  
  <CreateReportCondensed/>
  
</main>

