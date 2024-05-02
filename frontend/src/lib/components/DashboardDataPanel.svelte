<script lang="ts">
    import { reportCategories, municipios, dashboardStore } from "$lib/stores";
    import { createEventDispatcher } from "svelte";
    
    // Report Category Filter Logic
    let selected:string;
    let var1: string;
    let var2: string;
    let var2_options: string;
    let cat: string = '';
    let options: string = '';
    const municipalities = $municipios.municipiosList;
    const categoryArray = $reportCategories;
    const reportAxis = [{axis_id: 1, option: 'number'}, {axis_id: 2, option: 'percentage'}];
    console.log(cat);
    function updateChart (data: any) {
        $dashboardStore.chartData = data;
        console.log($dashboardStore.chartData);
    }
    function handleSubmit() {
		alert(`Selected option ${selected.name} (${selected})"`);
	}

</script>
<div class="flex flex-col flex-wrap gap-4 w-full h-full bg-primary px-8 py-8 rounded-2xl">
    <div class="flex flex-col w-full h-1/5 text-center">

        <h1>Variables Requeridas</h1>
        <div class="divider divider-neutral"></div>
        <!--Form section to handle dynamic filter options for Dashboard Panel Parameters-->
        <label for="var_1">Variable 1 (Eje Vertical)</label>
        <form action="?/CreateGraph" name="dashboard" method="POST">
            <!-- Variable 1 Dropdown -->
            <select name="var_1" id="var_1">
                <option value='# de Reportes'># de Reportes</option>
                <option value='% de Reportes'>% de Reportes</option>  
            </select>
            <!-- Variable 2 Dropdown -->
            <select bind:value={selected}>
                {#each municipalities as municipio}
                    <option value={municipio}>{municipio.name}</option>
                {/each}
            </select>
            <button class="btn btn-primary">Submit</button>
        </form>

        
        <h2>Variable 2 (Eje Horizontal)</h2>
        <select bind:value={selected} >
            <option selected value='Municipio'>Municipios</option>
            <option value='Categoría'>Categorías</option> 
        </select>

        <h2>Seleccione Municipios</h2>
        <select >
            <option selected>Municipios</option>
            <option>Categorías</option> 
        </select>
        <div class="divider divider-neutral"></div>
        <h1>Variables Opcionales</h1>
            
    </div>
</div>

<style lang="postcss">
    h1 {
        @apply text-primary-content text-3xl font-bold;
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
        @apply select text-lg font-medium select-secondary w-full;
    }
</style>
