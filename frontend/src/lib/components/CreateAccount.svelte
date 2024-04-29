<script>
    import { isCreateAccountModalOpen } from "$lib/stores";
    import { invalidAuth } from "$lib/stores";
    import axios from 'axios';

    function closeModal() {
        $isCreateAccountModalOpen = false;
        $invalidAuth = false;
    }

    // const sendData = () => {
    //     let formu = document.getElementById('formu');
    //     axios.post('http://localhost:5000/averias/users/', new FormData(formu))
    //             .then(res => {
    //                 console.log(res);
    //             })
    // }
</script>

<dialog id="my_modal_2" class="modal" class:modal-open={$isCreateAccountModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={closeModal}>✕</button>
                <!-- <button class="label-text-alt link link-hover" on:click={openSecondModal}>Create an account</button> -->
            </form>
            <form class="card-body" method="post" action="auth/?/createAccount">
                <!-- <div class="form-control mb-10">
                    <label class="label">
                        <span class="label-text">¿De qué municipio eres?</span>
                    </label>
                    <input name ="municipality" placeholder="Arecibo" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Nombre</span>
                    </label>
                    <input name ="FirstName" placeholder="Kiara" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Apellidos</span>
                    </label>
                    <input name ="LastName" placeholder="Velazquez Ortiz" class="input input-bordered" required />
                </div> -->
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
                    <input type="password" name= "PasswordHash" placeholder="contraseña" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Confirme su contraseña</span>
                    </label>
                    <input type="password" name= "PasswordConf" placeholder="confirma contraseña" class="input input-bordered" required />
                </div>
                {#if $invalidAuth}
                    <p class="text-error font-semibold ml-2 mt-2">Las contraseñas no son iguales</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" type="submit">Crear cuenta</button>
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