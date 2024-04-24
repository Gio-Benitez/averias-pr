<script lang="ts">
    import target_icon from '$lib/images/target_icon.png';
    import check_mark from '$lib/images/green_checkmark.png';
    import { getUserLocation } from "$lib/geolocation";
    import { fade } from 'svelte/transition';
    import { municipalities, buttonNext, steps_counter } from '$lib/stores';
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';

    // Define type for GeoJSON Point
    interface GeoJSONPoint {
        type: string;
        coordinates: [number, number];
    }

    let municipalityNames: string[] = [];

    onMount(() => {
        municipalities.subscribe((value: string[]) => {
        municipalityNames = value;
        });
    });

    let selectedMunicipality = '¿En qué municipio se encuentra?';
    let success = false; // Measures if the user's location was obtained successfully
    let errorMessage: string | null = null;  

    export const formData = writable({
        location: { type: "Point", coordinates: [0, 0] },
        municipality: '',
        category: '',
        image: ''
    });

    

    async function fetchUserLocation() {
        try {
            const userLocation: GeoJSONPoint = await getUserLocation();
            errorMessage = null; // Reset error message on success
            console.log("User location retrieved successfully:", userLocation);

            formData.update(data => ({
                ...data,
                location: userLocation
            }));
            success = true;

        } catch (error) {
        if (error instanceof Error) {
            errorMessage = error.message;
        } else {
            errorMessage = "An unknown error occurred.";
        }
        console.error(errorMessage);
        }
    }

    async function handleSubmit() {
        console.log("Your form data => ",formData)
        
    }

    function handleSelectionChange() {
        if (success) {
            $buttonNext = true;
        }
        formData.update(data => ({
                ...data,
                municipality: selectedMunicipality
        }));
        console.log(selectedMunicipality);
    }

</script>

<form class="form-container flex justify-center" method="post" action="report/?/createReport" on:submit={handleSubmit}>
    {#if $steps_counter === 1}
        <form method="dialog" class="flex flex-col justify-center w-1/2">
            <div class="flex justify-center">
                <button class="btn btn-lg btn-square btn-primary" on:click={fetchUserLocation}>
                    <div class="w-20 h-20 overflow-hidden">
                        <img alt="Theme Icon" src="{target_icon}" />              
                    </div>
                </button>
            </div>
            <span class="whitespace-no-wrap text-lg flex justify-center">
                {#if !success}
                    Presione para detectar su ubicación
                {:else if !success && errorMessage}
                    {errorMessage}
                {:else}
                    <div class="w-1/12 h-1/12 mt-5 transition-opacity duration-1000 ease-in-out">
                        <img alt="Check Mark Icon" src="{check_mark}" transition:fade /> 
                    </div>
                {/if}
            </span>
        </form>
        <div class="w-1/2 relative">
            <select class="select select-bordered w-full max-w-xs absolute left-0 transition-opacity duration-1000 ease-in-out" style="top:25px;" bind:value={selectedMunicipality} transition:fade on:change={handleSelectionChange}>
                <option disabled selected>¿En qué municipio se encuentra?</option>
                {#each municipalityNames as muni}
                    <option value={muni}>{muni}</option>
                {/each}
            </select>
        </div>
    {/if}
    <!-- <button class="btn btn-success" type="submit">Submit</button> -->
</form>    