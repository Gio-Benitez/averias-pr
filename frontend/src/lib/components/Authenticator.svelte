<script>
    import SignIn from './SignIn.svelte';
    import CreateAccount from './CreateAccount.svelte';
    import { isSignInModalOpen, isCreateAccountModalOpen, isForgotPasswordModalOpen } from '$lib/stores';
    import ForgotPassword from './ForgotPassword.svelte';
  
    let showSignIn = true;
    function handleOpenSecondModal() {
      $isSignInModalOpen = false;
      $isCreateAccountModalOpen = true;
    }
    function handleOpenForgotModal (){
        $isSignInModalOpen = false; 
        $isForgotPasswordModalOpen = true;
    }
  </script>
  <main>
  {#if showSignIn}
    <SignIn on:handleOpenSecondModal={handleOpenSecondModal} on:handleOpenForgotModal={handleOpenForgotModal} />
  {/if}
  
  {#if $isCreateAccountModalOpen}
    <CreateAccount />
  {/if}

  {#if $isForgotPasswordModalOpen}
    <ForgotPassword />
  {/if}
  </main>