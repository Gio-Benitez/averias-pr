<script lang="ts">
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import SignIn from '$components/SignIn.svelte'; 
  //import { signedIn } from '$lib/signinGlobalVars'; // Keep signedIn as false for now
  let signedIn = false;
  // initialize theme change
  onMount(() => {
    themeChange(false);
  });
</script>

<!-- Navigation Bar Svelte Component -->
  <nav class="navbar">
    <!-- Section containing the -->
    <section class="grid-cols-6 flex items-center">
      <a href="/" class="flex items-center bg-slate ml-8 mr-2">AveriasPR</a>
      <a href="/map" class="flex items-center bg-slate ml-8 mr-2">Map</a>
      <a href="/dashboard" class="flex items-center bg-slate ml-8 mr-2">Dashboard</a>
      <a href="/report" class="flex items-center bg-slate ml-8 mr-2" style="white-space: nowrap;"> Create a Report</a>
      <section class="dropdown w-full py-4 pr-8 ml-8 mr-2">
        <!-- <button class="btn btn-outline btn-primary">Theme</button> -->
        <div tabindex="0" role="button" class="btn m-1 btn-outline">
          Theme
          <svg width="12px" height="12px" class="h-2 w-2 fill-current opacity-60 inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path></svg>
        </div>
        <ul tabindex="0" class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52">
          <li><input  data-set-theme="dark" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Dark" value="dark"/></li>
          <li><input data-set-theme="night" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Night" value="night"/></li>
          <li><input data-set-theme="light" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Light" value="light"/></li>
          <li><input data-set-theme="retro" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Retro" value="retro"/></li>
          <li><input data-set-theme="cyberpunk" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Cyberpunk" value="cyberpunk"/></li>
          <li><input data-set-theme="valentine" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Valentine" value="valentine"/></li>
          <li><input data-set-theme="aqua" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Aqua" value="aqua"/></li>
          <li><input data-set-theme="autumn" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Autumn" value="autumn"/></li>
          <li><input data-set-theme="coffee" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Coffee" value="coffee"/></li>
          <li><input data-set-theme="forest" data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label="Forest" value="forest"/></li>
        </ul>
      </section>
    </section>
    <!-- If signed in, show Account hyperlink. If not, show Sign In modal-->
    {#if signedIn} 
      <a href="/account" class="flex items-center bg-slate mr-5">Account</a>
    {:else}
      <SignIn />
    {/if}
  </nav>

  <style>
    a:hover {
      color: white; /* Change background color on hover */
    }
    .navbar{
      display: flex;
      justify-content: space-between;
    }
  </style>
