<script lang="ts">
  import Footer from '$components/Footer.svelte';
  import NavBar from '$components/NavBar.svelte';
  import NavBarAlt from '$components/NavBarAlt.svelte';
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import '../app.postcss';
  import { AppShell } from '@skeletonlabs/skeleton';

  // initialize theme change
  onMount(() => {
    themeChange(false);
  });
</script>

<AppShell>
  <svelte:fragment slot="header"><NavBar /></svelte:fragment>
	<svelte:fragment slot="sidebarLeft"></svelte:fragment>
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
	<svelte:fragment slot="footer"><Footer /></svelte:fragment>
  
	<!-- (footer) -->
</AppShell>

