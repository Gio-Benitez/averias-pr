<script lang="ts">
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import AccountBubble from './AccountBubble.svelte';
  import theme_icon from '$lib/images/theme_icon.png';
  import { page } from '$app/stores';
  
  // let signedIn = false;
  // initialize theme change
  // Theme array
  const themes = [
      {
        name: 'Light',
        value: 'light'
      },
      {
        name: 'Dark',
        value: 'dark'
      },
      {
        name: 'Dim',
        value: 'dim'
      },
      {
        name: 'Cupcake',
        value: 'cupcake'
      },
      {
        name: 'Retro',
        value: 'retro'
      },
      {
        name: 'Business',
        value: 'business'
      },
      {
        name: 'Cyberpunk',
        value: 'cyberpunk'
      },
      {
        name: 'Aqua',
        value: 'aqua'
      },
      {
        name: 'Valentine',
        value: 'valentine'
      },
      {
        name: 'Coffee',
        value: 'coffee'
      },
      {
        name: 'Forest',
        value: 'forest'
      },
      {
        name: 'Night',
        value: 'night'
      },
      {
        name: 'Autumn',
        value: 'autumn'
      },
      {
        name: 'Corporate',
        value: 'corporate'
      },
  ];

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
      <a data-sveltekit-preload-data="hover" href="/" class="ml-16 {$page.url.pathname==='/map' ? 'btn btn-ghost btn-md font-normal' : 'font-semibold'}" style="font-size: 1.15rem;" class:active={$page.url.pathname==='/map'}>Inicio</a>
      <div class="divider divider-horizontal"></div>
      <a href="/map" class="{$page.url.pathname==='/' ? 'btn btn-ghost btn-md font-normal' : 'font-semibold'}" style="font-size: 1.15rem;" class:active={$page.url.pathname==='/'}>Mapa</a>
    </section>
    <section class="flex items-center mr-16 py-1">
      <section class="dropdown dropdown-left ml-8 mr-1">
        <div tabindex="0" role="button" class="btn btn-xm btn-ghost m-1 btn-circle ">
          <!-- Theme -->
          <div class="w-5 h-5 rounded-full overflow-hidden">
            <img alt="Theme Icon" src="{theme_icon}" />
          </div>
        </div>
        <ul class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52">
          {#each themes as theme}
            <li><input data-set-theme={theme.value} data-act-class="ACTIVECLASS" type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label={theme.name} value={theme.value}/></li>
          {/each} 
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
