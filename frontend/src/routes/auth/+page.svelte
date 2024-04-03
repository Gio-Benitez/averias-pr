<script>
    import { isModalOpen } from '$lib/stores.js';
    export let form;

    if (form?.message) {
        isModalOpen.set(true);
    }
</script>


<main>

    {#if isModalOpen}
        <p class="text-red-500 font-semibold">{form?.message}</p>
    {/if}

</main>
