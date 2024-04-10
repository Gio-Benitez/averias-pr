<script lang="ts">
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
  import { invalidAuth, isSignInModalOpen, isForgotPasswordModalOpen, isCreateAccountModalOpen, signedIn } from '$lib/stores';

  /** @type {import('./$types').PageData} */
	export let data;

  if (data.access) {
    signedIn.set(true)
  }
  else if (data.failedAuth) {
    if (data.failedPath === "forgot") {
      isForgotPasswordModalOpen.set(true);
      invalidAuth.set(true);
    }
    else if (data.failedPath === "create") {
      isCreateAccountModalOpen.set(true);
      invalidAuth.set(true);
    }
    else {
      isSignInModalOpen.set(true);
      invalidAuth.set(true);
    }
  }

</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
  <!-- <div
    class="relative grid grid-cols-1 grid-rows-1 justify-items-center whitespace-nowrap text-center text-6xl lg:flex lg:items-center lg:justify-center lg:gap-4 mt-8 mb-10">
    Welcome to AveriasPR
  </div> -->
  
  <!-- <CreateReportCondensed/> -->

  <!-- <div class="stats shadow">
  
    <div class="stat">
      <div class="stat-figure text-primary">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
      </div>
      <div class="stat-title">Total Likes</div>
      <div class="stat-value text-primary">25.6K</div>
      <div class="stat-desc">21% more than last month</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
      </div>
      <div class="stat-title">Page Views</div>
      <div class="stat-value text-secondary">2.6M</div>
      <div class="stat-desc">21% more than last month</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <div class="avatar online">
          <div class="w-16 rounded-full">
            <img src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
          </div>
        </div>
      </div>
      <div class="stat-value">86%</div>
      <div class="stat-title">Tasks done</div>
      <div class="stat-desc text-secondary">31 tasks remaining</div>
    </div>
    
  </div> -->
  
</main>

