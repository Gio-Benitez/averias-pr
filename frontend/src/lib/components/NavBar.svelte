<script lang="ts">
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import AccountBubble from './AccountBubble.svelte';
  import theme_icon from '$lib/images/theme_icon.png';
  import { page } from '$app/stores';
  // let signedIn = false;
  // initialize theme change
  onMount(() => {
    themeChange(false);
  });
</script>

<!-- Navigation Bar Svelte Component -->
  <nav class="navbar">
    <!-- Section containing the -->
    <section class="flex items-center">
      <a href="/" class="ml-16 btn btn-ghost" style="font-size: 1.50rem;">AveriasPR</a>
      <!-- <a href="/map" class="flex items-center bg-slate ml-8 mr-2">Map</a>
      <a href="/dashboard" class="flex items-center bg-slate ml-8 mr-2">Dashboard</a>
      <a href="/report" class="flex items-center bg-slate ml-8 mr-2" style="white-space: nowrap;"> Create a Report</a> -->
    </section>
    <section>
      <a href="/" class="ml-16 {$page.url.pathname==='/map' ? 'btn btn-ghost btn-md font-normal' : 'font-semibold'}" style="font-size: 1.15rem;" class:active={$page.url.pathname==='/map'}>Dashboard</a>
      <div class="divider divider-horizontal"></div>
      <a href="/map" class="{$page.url.pathname==='/' ? 'btn btn-ghost btn-md font-normal' : 'font-semibold'}" style="font-size: 1.15rem;" class:active={$page.url.pathname==='/'}>Map</a>
    </section>
    <section class="flex items-center mr-16 py-1">
      <section class="dropdown dropdown-left ml-8 mr-1">
        <!-- <button class="btn btn-outline btn-primary">Theme</button> -->
        <div tabindex="0" role="button" class="btn btn-xm btn-ghost m-1 btn-circle ">
          <!-- Theme -->
          <!-- <svg width="12px" height="12px" class="h-2 w-2 fill-current opacity-60 inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path></svg> -->
          <div class="w-5 h-5 rounded-full overflow-hidden">
            <img alt="Theme Icon" src="{theme_icon}" />
          </div>
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
      <AccountBubble />
    </section>
  </nav>

  <style>
    .navbar{
      display: flex;
      justify-content: space-between;
    }
  </style>
