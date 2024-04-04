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

<NavBar />

<slot />


<Footer />