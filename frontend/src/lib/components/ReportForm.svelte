<script lang="ts">
    import target_icon from '$lib/images/target_icon.png';
    import check_mark from '$lib/images/green_checkmark.png';
    import { getUserLocation } from "$lib/geolocation";
    import { fade } from 'svelte/transition';
    import { municipalities, buttonNext, steps_counter,reset} from '$lib/stores';
    import { onMount } from 'svelte';
    import CategoryIconCloud from './CategoryIconCloud.svelte';
    import { CldUploadButton } from 'svelte-cloudinary';
    import { enhance } from '$app/forms';
    
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
    let success: boolean = false; // Measures if the user's location was obtained successfully
    let errorMessage: string | null = null;  

    let formData = {
        userID: 0,
        location: [0, 0],
        municipality: '',
        category: '',
        image: ''
    };

    function getCookie(name: string) {
        const cookieName = name + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookieArray = decodedCookie.split(';');

        for(let i = 0; i < cookieArray.length; i++) {
            let cookie = cookieArray[i].trim();
            if (cookie.indexOf(cookieName) === 0) {
                return cookie.substring(cookieName.length, cookie.length);
            }
        }
        return null;
    }

    async function fetchUserLocation() {
        try {
            const userLocation: GeoJSONPoint = await getUserLocation();
            errorMessage = null; // Reset error message on success
            console.log("User location retrieved successfully");

            formData.location = userLocation.coordinates;
            console.log(formData.location);
            // @ts-ignore
            let cookie_parse = JSON.parse(getCookie('UserData'));
            console.log(cookie_parse);
            if (cookie_parse === null || cookie_parse.UserID === undefined) {
                // If user is not signed in, set userID to default value of 0
                formData.userID = 0;
            }else {
                // If user is signed in, set userID to the value stored in the cookie
                formData.userID = cookie_parse.UserID;
            }
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

    function handleSelectionChange() {
        if (success) {
            $buttonNext = true;
        }
        formData.municipality = selectedMunicipality;
        console.log(selectedMunicipality);
    }

    let message ="";
    // const sendData = () => {
    //     const jsonData = JSON.stringify(formData);
    
    //     axios.post('https://averias-pr.onrender.com/averias/report_data/', jsonData, {
    //     headers: {
    //             'Content-Type': 'application/json'
    //     }
    //     })
    //     .then(res=> {
    //         console.log(res.data);
    //         let userData = {
    //             UserID: 0,
    //             user_report_count: 0,
    //             user_reports: []
    //         }
    //         // @ts-ignore
    //         userData.UserID = getCookie('UserData').UserID;
    //         userData.user_report_count = res.data.report_count;
    //         userData.user_reports = res.data.user_reports;
    //         document.cookie = 'UserData' + "=" + (JSON.stringify(userData) || "") + "; path=/";
    //         reset()
    //         window.location.reload();
    //     })
    //     .catch(error => {
    //         // Handle error response here
    //         if (error.response) {
    //             console.error('Error:', error.response.data.error); // Log the error message
    //             // Handle the error message here (e.g., display it on the UI)
    //             message = error.response.data.error;
    //         } else {
    //             console.error('Error:', error);
    //         }
    //  });
    // }

    // Result type is any because it is the result of the Cloudinary upload, it is guaranteed to have an info object
    function handleUpload(result: any) {
        formData.image = result.info.url;
        console.log(formData.image);
        $buttonNext=true;
    }
</script>

<form class="form-container flex justify-center" action="?/submitReport" method="POST">
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
        {#if success}
            <div class="w-1/2 relative">
                <select class="select select-bordered w-full max-w-xs absolute left-0" style="top:25px;" bind:value={selectedMunicipality} on:change={handleSelectionChange}>
                    <option disabled selected>¿En qué municipio se encuentra?</option>
                    {#each municipalityNames as muni}
                        <option value={muni}>{muni}</option>
                    {/each}
                </select>
            </div>
        {/if}
    {/if}

    {#if $steps_counter ===2}
        <form method="dialog">
            <CategoryIconCloud bind:value={formData.category}/>
        </form>
    {/if}
    {#if $steps_counter===3}
            
            <div class="flex flex-col">
                <h2>Subir Imagen</h2>
                <CldUploadButton 
                    class="btn btn-primary btn-md mb-4"
                    uploadPreset="uw_test"
                    onUpload={result => handleUpload(result) }
                    bind:value={formData.image}
                />
            </div>
    {/if}
    {#if $steps_counter===4}
        <div class="flex flex-col">
            <div class="label mb-10">
                <span class="label-text font-semibold" style="font-size: 1.5rem;">¿Todo listo?</span>
            </div>
            <!-- Map FormData variable values to FormData of actual form using hidden inputs -->
            <input type="hidden" name="userID" value={formData.userID} />
            <input type="hidden" name="location" value={formData.location} />
            <input type="hidden" name="municipality" value={formData.municipality} />
            <input type="hidden" name="category" value={formData.category} />
            <input type="hidden" name="image" value={formData.image} />
            <button type="submit" class="btn btn-success btn-lg mb-10">Crear</button>
        </div>
    {/if}
</form>    

<style lang="postcss">
    h2 {
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
</style>