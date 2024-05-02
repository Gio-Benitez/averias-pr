<script lang="ts">
    import { enhance } from '$app/forms';
	import type { PageData, ActionData } from './$types';
    import DashboardPanel from '$components/DashboardPanel.svelte';
    import MapDashNav from '$components/MapDashNav.svelte';
    import { mapDataStore, filterCategoriesStore, municipios } from '$lib/stores';
    import { redirect } from '@sveltejs/kit';

    
    export let data: PageData;
    export let form: ActionData;

    // Dashboard Data Panel Logic
    const municipalities = $municipios.municipiosList;
    let var1: string;
    let var2: string;
    let var2_val: string;
    let var_opt: string;
    function test (){
        console.log(var1);
        console.log(var2);
        console.log(var2_val);
        console.log(var_opt);
    }
    // Resets the value of var2_val and var_opt when var2 is changed
    function yeet () {
        var2_val = '';
        var_opt = '';
    }
</script>

<main class="grid grid-rows-10 grid-cols-10 h-full w-full gap-8 pb-8">
    <!--Map and Dashboard Nav Buttons-->
    <MapDashNav />
    <!--Dashboard Data Panel Segement-->
    <div id="dataPanelSlot" class="min-w-72 min-h-[697px] col-start-8 col-end-10 row-start-2 row-end-10">
        <div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 pt-8 pb-1 rounded-2xl">
            <div class="flex flex-col w-full text-center">
                <!-- Panel Title -->
                <h1>Filtros</h1>
                <div class="divider divider-neutral"></div>
                <!--Form section to handle dynamic filter options for Dashboard Panel Parameters-->
                <h2>Variable 1 (Eje Vertical)</h2>
                <form action="?/dashboardGraph" name="dashboard" method="POST">
                    <!-- Variable 1 Dropdown -->
                    <select name="var_1" bind:value={var1}>
                        <option value='# de Reportes'># de Reportes</option>
                        <option value='% de Reportes'>% de Reportes</option>  
                    </select>
                    <!-- Variable 2 Dropdown -->
                    <h2>Variable 2 (Eje Horizontal)</h2>
                    <select name="var_2" bind:value={var2} on:change={yeet}>
                        <option value='Municipios'>Municipios</option>
                        <option value='Categorías'>Categorías</option> 
                    </select>
                    {#if var2 === 'Categorías'}
                        <select name="var_2_val" bind:value={var2_val}>
                            <option disabled selected value>Seleccione Categoría(s)</option>
                            {#each $filterCategoriesStore as category}
                                <option value={category}>{category}</option>
                            {/each}
                        </select>
                    {:else if var2 === 'Municipios'}
                        <select name="var_2_val" bind:value={var2_val}>
                            <option disabled selected value>Seleccione Municipio(s)</option>
                            {#each municipalities as municipio}
                                <option value={municipio.name}>{municipio.name}</option>
                            {/each}
                        </select>
                    {/if}
                    {#if var2 === 'Municipios' && var2_val}
                        <h2>Variable Opcional (Categorías)</h2>
                        <select name="var_opt" bind:value={var_opt}>
                            <option disabled selected value>Seleccione Categoría(s)</option>
                            {#each $filterCategoriesStore as category}
                                <option value={category}>{category}</option>
                            {/each}
                        </select>
                    {:else if var2 === 'Categorías'&& var2_val}
                        <h2>Variable Opcional (Municipios)</h2>
                        <select name="var_opt" bind:value={var_opt}>
                            <option disabled selected value>Seleccione Municipio(s)</option>
                            {#each municipalities as municipio}
                                <option value={municipio.name}>{municipio.name}</option>
                            {/each}
                        </select>
                    {/if}
                    <button type="submit" on:click={test} class="btn">Submit</button>
                </form>
                <div class="divider divider-neutral"></div>
                <h1>Selección</h1>
            </div>
        </div>
    </div>
    <!--Dashboard Panel Segment-->
    <div id="dashboard" class="min-h-[697px] col-start-2 col-end-8 row-start-2 row-end-10">
        <DashboardPanel />
    </div>
</main>

<style lang="postcss">
    button {
        @apply  btn-md text-primary font-medium text-lg;
    }
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    h2 {
        @apply text-primary-content text-lg font-medium;
    }
    .stat-title {
        @apply text-lg font-semibold;
    }
    .stat-value {
        @apply text-2xl font-bold;
    }
    option {
        @apply font-medium;
    }
    select {
        @apply select mb-1 select-secondary w-full text-lg font-medium;
    }
    
</style>