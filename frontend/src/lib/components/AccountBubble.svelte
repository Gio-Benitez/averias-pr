<script lang="ts">
    import avatar_icon from '$lib/images/avatar_icon.png';
    import { invalidAuth, isCreateAccountModalOpen, isForgotPasswordModalOpen, isSignInModalOpen, signedIn} from '$lib/stores'; 
    import CreateAccount from './CreateAccount.svelte';
    import ForgotPassword from './ForgotPassword.svelte';
    import SignIn from './SignIn.svelte';
    import { signIn, signOut } from "@auth/sveltekit/client"
    
    function handleOpenForgotModal (){
        $isSignInModalOpen = false; 
        $isForgotPasswordModalOpen = true;
        $invalidAuth = false;
    }

    function handleOpenCreateAccountModal() {
        $isSignInModalOpen = false;
        $isCreateAccountModalOpen = true;
        $invalidAuth = false;
    }

    function handleForgottoSignIn (){
        $isForgotPasswordModalOpen = false;
        $isSignInModalOpen = true;
        $invalidAuth = false;
    }

    // function signOut() {
    //     document.cookie = 'access' + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    //     document.cookie = 'UserData' + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    //     $signedIn = false;
    //     window.location.reload();
    // }

</script>

{#if $isCreateAccountModalOpen}
    <CreateAccount />
{/if}

{#if $isSignInModalOpen}
    <SignIn on:handleOpenForgotModal={handleOpenForgotModal} on:handleOpenCreateAccountModal={handleOpenCreateAccountModal}/>
{/if}

{#if $isForgotPasswordModalOpen}
    <ForgotPassword on:handleForgottoSignIn={handleForgottoSignIn}/>
{/if}

<div class="dropdown dropdown-end">
        <div class="flex-none">
            <button tabindex="0" class="btn btn-md flex items-center rounded-full px-2">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-4 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
              <div class="avatar {$signedIn ? 'online' : 'offline'}">
                <div class="w-8 h-8 rounded-full overflow-hidden">
                    <img alt="Avatar Icon" src="{avatar_icon}" />
                </div>
              </div>
            </button>
        </div>
    {#if $signedIn}
        <ul class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
            <li>
            <a class="justify-between">
                Mis Reportes
                <span class="badge">Nuevo</span>
            </a>
            </li>
            <li><a>Ajustes</a></li>
            <li><button on:click={() => signOut()}>Cerrar Sesión</button></li>
            
        </ul>
        
    {:else}
        <ul class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
            <li><button class="justify-between" on:click={()=>$isCreateAccountModalOpen = true}>Crear una cuenta</button></li>
            <li><button class="justify-between" on:click={()=>$isSignInModalOpen =true}>Iniciar Sesión</button></li>
            <!-- <li><a>Logout</a></li> -->
        </ul>
    {/if}
    
</div>