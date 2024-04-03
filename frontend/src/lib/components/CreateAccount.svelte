<script>
    import { isCreateAccountModalOpen } from "$lib/stores";
</script>

<dialog id="my_modal_2" class="modal" class:modal-open={$isCreateAccountModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={()=>$isCreateAccountModalOpen = false}>✕</button>
                <!-- <button class="label-text-alt link link-hover" on:click={openSecondModal}>Create an account</button> -->
            </form>
            <form class="card-body" method="post" action="auth/?/createAccount">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Enter your email</span>
                    </label>
                    <input type="email" name ="email" placeholder="Enter your email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Enter a password</span>
                    </label>
                    <input type="password" name= "password" placeholder="Enter a password" class="input input-bordered" required />
                    <label class="label">
                        <span class="label-text">Confirm password</span>
                    </label>
                    <input type="password" name= "password-confirmation" placeholder="Confirm password" class="input input-bordered" required />
                </div>
                <div class="form-control mt-6">
                    <button class="btn btn-primary" type = "submit">Create Account</button>
                </div>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={()=>$isCreateAccountModalOpen = false}></button>
    </form>
</dialog>

<style>
    button:hover{
        color: white; /* Change text color on hover */
    }
</style>