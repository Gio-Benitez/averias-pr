<script>
    import { isCreateAccountModalOpen, invalidAuth} from "$lib/stores";
    import axios from 'axios';

    let message="";

    function closeModal() {
        $isCreateAccountModalOpen = false;
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
        
        axios.post('http://localhost:5000/averias/users/', jsonData, {
        headers: {
                'Content-Type': 'application/json'
        }
        })
        .then(res=> {
            console.log(res.data.message);
            document.cookie = 'access' + "=" + ('true' || "") + "; path=/";
            let userData = {
                UserID: 0,
                user_report_count: 0,
                user_reports: []
            }
            // @ts-ignore
            userData.UserID = getCookie('UserData').UserID;
            document.cookie = 'UserData' + "=" + (JSON.stringify(userData) || "") + "; path=/";
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

<dialog id="my_modal_2" class="modal" class:modal-open={$isCreateAccountModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={closeModal}>✕</button>
                <!-- <button class="label-text-alt link link-hover" on:click={openSecondModal}>Create an account</button> -->
            </form>
            <form id="formu" class="card-body" method="POST">
                <div class="form-control mb-10">
                    <!-- <label class="label">
                        <span class="label-text">¿De qué municipio eres?</span>
                    </label>
                    <input name ="municipality" placeholder="Arecibo" class="input input-bordered" required /> -->
                    <label class="label">
                        <span class="label-text">Nombre</span>
                    </label>
                    <input name ="FirstName" placeholder="Kiara" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Apellidos</span>
                    </label>
                    <input name ="LastName" placeholder="Velazquez Ortiz" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Entre su email</span>
                    </label>
                    <input type="email" name ="Email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Crea una contraseña</span>
                    </label>
                    <input type="password" name= "Password" placeholder="contraseña" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Confirme su contraseña</span>
                    </label>
                    <input type="password" name= "PasswordConf" placeholder="confirma contraseña" class="input input-bordered" required />
                </div>
                {#if message}
                    <p class="text-error font-semibold ml-2 mt-2">{message}</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" on:click|preventDefault={sendData}>Crear cuenta</button>
                </div>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={closeModal}></button>
    </form>
</dialog>

<style>
    button:hover{
        color: white; /* Change text color on hover */
    }
</style>