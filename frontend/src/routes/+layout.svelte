<script lang="ts">
  import Footer from '$components/Footer.svelte';
  import NavBar from '$components/NavBar.svelte';
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import '../app.postcss';

  // initialize theme change
  onMount(() => {
    themeChange(false);
  });
</script>

<NavBar />

<slot class="slot-content"/>

<Footer/>


<style>
  .slot-content {
    overflow-y: auto; /* Add scrollbar if content exceeds height */
  }
</style>

