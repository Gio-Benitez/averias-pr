<script>
    import SignIn from './SignIn.svelte';
    import CreateAccount from './CreateAccount.svelte';
    import { isSignInModalOpen, isCreateAccountModalOpen, isForgotPasswordModalOpen, invalidAuth} from '$lib/stores';
    import ForgotPassword from './ForgotPassword.svelte';
  
    let showSignIn = true;
    function handleOpenSecondModal() {
      $isSignInModalOpen = false;
      $isCreateAccountModalOpen = true;
      $invalidAuth = false;
    }
    function handleOpenForgotModal (){
        $isSignInModalOpen = false; 
        $isForgotPasswordModalOpen = true;
        $invalidAuth = false;
    }
    function handleCreatetoSignIn (){
        $isCreateAccountModalOpen = false;
        $isSignInModalOpen = true;
        $invalidAuth = false;
    }

    function handleForgottoSignIn (){
        $isForgotPasswordModalOpen = false;
        $isSignInModalOpen = true;
        $invalidAuth = false;
    }

  </script>
  <main>
  {#if showSignIn}
    <SignIn on:handleOpenSecondModal={handleOpenSecondModal} on:handleOpenForgotModal={handleOpenForgotModal} />
  {/if}
  
  {#if $isCreateAccountModalOpen}
    <CreateAccount on:handleCreatetoSignIn={handleCreatetoSignIn}/>
  {/if}

  {#if $isForgotPasswordModalOpen}
    <ForgotPassword on:handleForgottoSignIn={handleForgottoSignIn}/>
  {/if}
  </main>