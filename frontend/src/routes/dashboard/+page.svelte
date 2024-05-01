<script lang="ts">
    import { enhance } from '$app/forms';
	import type { PageData, ActionData } from './$types';
    import DashboardPanel from '$components/DashboardPanel.svelte';
    import { mapDataStore, filterCategoriesStore, municipios } from '$lib/stores';
    import { redirect } from '@sveltejs/kit';
    
    export let data: PageData;
    export let form: ActionData;

    // Dashboard Data Panel Logic
    const municipalities = $municipios.municipiosList;
    let var1: string;
    let var2: string;
    let var2_val: string;
    function test (){
        console.log(var1);
        console.log(var2);

    }
</script>

<main class="grid grid-rows-10 grid-cols-10 h-full w-full gap-8 pb-8">
    <!--Map and Dashboard Nav Buttons-->
    <div class="flex pt-12 pl-0 space-x-2 col-span-3 row-span-1 col-start-2 row-start-1 ">
        <div class="flex h-full ">
            <div class="tabs-lifted tabs-lg w-full h-full">
                <a role="tab" href="/map" class="tab">Interactive Map</a>
                <a role="tab" href="/dashboard" class="tab">Dashboard</a>
            </div>
        </div>
    </div>
    <!--Dashboard Component Segment-->
    <div id="dashboard" class="min-h-[697px] col-start-2 col-end-8 row-start-2 row-end-10">
        <DashboardPanel />
    </div>
    <!--Dashboard Data Panel Segement-->
    <div id="dataPanelSlot" class="min-w-72 min-h-[697px] col-start-8 col-end-10 row-start-2 row-end-10">
        <div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 pt-8 pb-1 rounded-2xl">
            <div class="flex flex-col w-full text-center">
                <!-- Panel Title -->
                <h1>Variables Requeridas</h1>
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
                    <select name="var_2" bind:value={var2}>
                        <option value='Municipios'>Municipios</option>
                        <option value='Categorías'>Categorías</option> 
                    </select>
                    {#if var2 === 'Categorías'}
                        <select name="var_2_val" bind:value={var2_val}>
                            {#each $filterCategoriesStore as category}
                                <option value={category}>{category}</option>
                            {/each}
                        </select>
                    {:else if var2 === 'Municipios'}
                        <select name="var_2_val" bind:value={var2_val}>
                            {#each municipalities as municipio}
                                <option value={municipio.name}>{municipio.name}</option>
                            {/each}
                        </select>
                    {/if}
                    <h2>Seleccione Municipios</h2>
                    <select >
                        <option selected>Municipios</option>
                        <option>Categorías</option> 
                    </select>
                        <button type="submit" on:click={test} class="btn btn-primary">Submit</button>
                </form>
                <div class="divider divider-neutral"></div>
                <h1>Selección</h1>
                
            </div>
        </div>
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
        @apply select select-secondary w-full text-lg font-medium;
    }
    
</style>