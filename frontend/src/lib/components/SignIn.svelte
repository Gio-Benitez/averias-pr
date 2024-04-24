<script>
  import { invalidAuth, isSignInModalOpen } from "$lib/stores";
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  function openForgotModal() {
    dispatch('handleOpenForgotModal');
  }

  function close() {
    $isSignInModalOpen = false;
    $invalidAuth = false;
  }

</script>

<!--If Sign In button is pressed, open modal-->
<dialog id="signInModal" class="modal" class:modal-open={$isSignInModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={close}>✕</button>
            </form>
            <form class="card-body" method="post" action="auth/?/login">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Email</span>
                    </label>
                    <input type="email" name ="email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Contraseña</span>
                    </label>
                    <input type="password" name= "password" placeholder="contraseña" class="input input-bordered" required />
                    <form method="dialog">
                        <button class="label-text-alt link link-hover" on:click={openForgotModal}>¿Has olvidado tu contraseña?</button>
                    </form>
                </div>
                {#if $invalidAuth}
                    <p class="text-error font-semibold ml-2 mt-2">El email o la contraseña no son válidos</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" type = "submit">Iniciar</button>
                </div>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={close}></button>
    </form>
</dialog>

<style>
    button:hover{
        color: white; /* Change text color on hover */
    }
</style>