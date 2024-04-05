<!--
    This component will provide an ordered list of available report categories in a dropdown menu.
    This component will export the value of the selected report category to the parent component.
    The parent component will use the selected report category to populate the report form.
-->
<script lang="ts">
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';

    export let selectedCategory: string = '';
    export const categories: string[] = ['hole', 'pole', 'road', 'tree', 'water', 'other'];

    const selectedCategoryStore = writable(selectedCategory);

    onMount(() => {
        selectedCategoryStore.set(selectedCategory);
    });

    selectedCategoryStore.subscribe((value) => {
        selectedCategory = value;
    });

    function selectCategory(category: string): void {
        selectedCategoryStore.set(category);
    }
</script>

<select bind:value={selectedCategory} on:change={e => selectCategory(e.target.value)}>
    {#each categories as category}
        <option value={category}>{category}</option>
    {/each}
</select>

<style>
    select {
        min-width: 15rem;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 0.25rem;
    }
</style>