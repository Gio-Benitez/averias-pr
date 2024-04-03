<script>
  import Footer from '$components/Footer.svelte';
  import NavBar from '$components/NavBar.svelte';
  import { onMount } from 'svelte';
  import { themeChange } from 'theme-change';
  import '../app.postcss';
  import SignIn from '$components/SignIn.svelte'; 
  /** @type {import('./$types').ActionData} */
  export let form;
  

  // initialize theme change
  onMount(() => {
    themeChange(false);
  });
</script>

<div class="flex items-center">
  <NavBar />
  <!-- If signed in, show Account hyperlink. If not, show Sign In modal-->
  {#if form?.success}
    <a href="/account" class="flex items-center bg-slate mr-5">Account</a>
  {:else}
    <SignIn />
  {/if}
</div>

<slot />


<Footer />
