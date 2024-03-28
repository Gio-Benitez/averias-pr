<script>
import { signedIn } from '$lib/signinGlobalVars';
let isModalOpen = false
</script>


<button class="btn mr-8 modal-button" on:click={()=>isModalOpen = true}>Sign In</button>
<dialog id="my_modal_2" class="modal" class:modal-open={isModalOpen}>
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <!--This form allows you to close modal by clicking x-->
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2" on:click={()=>isModalOpen = false}>✕</button>
            </form>
            <form class="card-body">
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Email</span>
                    </label>
                    <input type="email" placeholder="email" class="input input-bordered" required />
                </div>
                <div class="form-control">
                    <label class="label">
                        <span class="label-text">Password</span>
                    </label>
                    <input type="password" placeholder="password" class="input input-bordered" required />
                    <label class="label">
                        <a href="#" class="label-text-alt link link-hover">Forgot password?</a>
                    </label>
                </div>
                <div class="form-control mt-6">
                    <button class="btn btn-primary">Login</button>
                </div>
                <label class="label" style="display: flex; justify-content: center;">
                    <a href="#" class="label-text-alt link link-hover">Create an account</a>
                </label>
            </form>
        </div>
    </div>
    <!--This form allows you to close modal by clicking outside of it-->
    <form method="dialog" class="modal-backdrop">
        <button on:click={()=>isModalOpen = false}>close</button>
    </form>
</dialog>