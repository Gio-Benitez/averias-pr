<script>
    import { invalidAuth, isModalOpen } from "$lib/stores";
</script>

<!--Initially just the Sign In button-->
<button class="btn mr-8 modal-button" on:click={()=>$isModalOpen =true}>Sign In</button>
<!--If Sign In button is pressed, open modal-->
<dialog id="my_modal_2" class="modal" class:modal-open={$isModalOpen}>
    <!-- {#if form?.message}
        <p style="bg-error">{form.message}</p>
    {/if} -->
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={()=>$isModalOpen = false}>✕</button>
            </form>
            <form class="card-body" method="post" action="auth/?/login">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Email</span>
                    </label>
                    <!-- <input type="email" name ="email" placeholder="email" class="input input-bordered" value = {form?.email || ""} required /> -->
                    <input type="email" name ="email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <input type="password" name= "password" placeholder="password" class="input input-bordered" required />
                    <label class="label">
                        <a href="#" class="label-text-alt link link-hover">Forgot password?</a>
                    </label>
                </div>
                {#if $invalidAuth}
                    <p class="text-error font-semibold ml-2 mt-2">Email or password is not valid</p>
                {/if}
                <div class="form-control mt-6">
                    <button class="btn btn-primary" type = "submit">Login</button>
                </div>
                <label class="label" style="display: flex; justify-content: center;">
                    <a href="#" class="label-text-alt link link-hover">Create an account</a>
                </label>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={()=>$isModalOpen = false}></button>
    </form>
</dialog>

<style>
    button:hover{
        color: white; /* Change text color on hover */
    }
</style>