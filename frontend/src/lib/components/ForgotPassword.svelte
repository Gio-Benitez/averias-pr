<script>
    import { isForgotPasswordModalOpen, invalidAuth} from "$lib/stores";
    import axios from "axios";
    import { createEventDispatcher } from "svelte";
    
    const dispatch = createEventDispatcher();

    function returntoSignIn() {
        dispatch('handleForgottoSignIn');
    }

    let message = "";

    const sendData = () => {
        let formu = document.getElementById('formu');
        // @ts-ignore
        let form = new FormData(formu);
        const jsonData = {};
        form.forEach((value, key) => {
        // @ts-ignore
        jsonData[key] = value;
        });
        
        axios.post('http://localhost:5000/averias/users/update_password', jsonData, {
        headers: {
                'Content-Type': 'application/json'
        }
        })
        .then(res=> {
            console.log(res.data.message);
            document.cookie = 'access' + "=" + ('true' || "") + "; path=/"; // Sets a cookie named 'access' with value 'true' that expires in half a day
            document.cookie = 'UserID' + "=" + (res.data.UserID || "") + "; path=/";
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

<dialog id="my_modal_2" class="modal" class:modal-open={$isForgotPasswordModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={returntoSignIn}>✕</button>
            </form>
            <form id="formu" class="card-body" method="POST">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Entre su email</span>
                    </label>
                    <input type="email" name ="Email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Entre una nueva contraseña</span>
                    </label>
                    <input type="password" name= "Password" placeholder="Nueva contraseña" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Confirme su nueva contraseña</span>
                    </label>
                    <input type="password" name= "PasswordConf" placeholder="Confirme contraseña" class="input input-bordered" required />
                </div>
                {#if $invalidAuth}
                    <p class="text-error font-semibold ml-2 mt-2">Las contraseñas no son iguales</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" on:click|preventDefault={sendData}>Cambiar contraseña</button>
                </div>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={()=>$isForgotPasswordModalOpen = false}></button>
    </form>
</dialog>

<style>
    button:hover{
        color: white; /* Change text color on hover */
    }
</style>