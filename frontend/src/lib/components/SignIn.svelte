<script>
  import { invalidAuth, isSignInModalOpen } from "$lib/stores";
  import axios from "axios";
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let message="";

  function openForgotModal() {
    dispatch('handleOpenForgotModal');
  }

  function openCreateAccountModal() {
    dispatch('handleOpenCreateAccountModal')
  }

  function close() {
    $isSignInModalOpen = false;
    $invalidAuth = false;
  }

  const sendData = () => {
        let formu = document.getElementById('formu');
        // @ts-ignore
        let form = new FormData(formu);
        const jsonData = {};
        form.forEach((value, key) => {
        // @ts-ignore
        jsonData[key] = value;
        });
        
        axios.post('http://localhost:5000/averias/users/login', jsonData, {
        headers: {
                'Content-Type': 'application/json'
        }
        })
        .then(res=> {
            console.log(res.data.message);
            document.cookie = 'access' + "=" + ('true' || "") + "; path=/"; // Sets a cookie named 'access' with value 'true' that expires in half a day
            window.location.reload();
        })
        .catch(error => {
            // Handle error response here
            if (error.response) {
                console.error('Error:', error.response.data.error); // Log the error message
                // Handle the error message here (e.g., display it on the UI)
                message = error.response.data.error;
            } else {
                console.error('Error:', error);
            }
    });
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
            <form id="formu" class="card-body" method="POST">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Email</span>
                    </label>
                    <input type="email" name ="Email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Contraseña</span>
                    </label>
                    <input type="password" name= "Password" placeholder="contraseña" class="input input-bordered" required />
                    <form method="dialog">
                        <button class="label-text-alt link link-hover" on:click={openForgotModal}>¿Has olvidado tu contraseña?</button>
                    </form>
                </div>
                {#if message}
                    <p class="text-error font-semibold ml-2 mt-2">{message}</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" on:click|preventDefault={sendData}>Iniciar</button>
                </div>
                <label class="label" style="display: flex; justify-content: center;">
                    <button class="label-text-alt link link-hover" on:click={openCreateAccountModal}>Crear una cuenta</button>
                </label>
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