<script lang="ts">
    import electrical_pole_icon from '$lib/images/electric_pole.png';
    import landslide_icon from '$lib/images/landslide_icon.png';
    import landslidehazard_icon from '$lib/images/landslidehazard_icon.png';
    import lightning_icon from '$lib/images/lightning_icon.png';
    import pothole_icon from '$lib/images/pothole_icon.png';
    import water_drop_icon from '$lib/images/water_drop_icon.png';
    import { reportCategories, buttonNext } from '$lib/stores';
    
    export let value;

    let catDict: {[key: number]: string} = {};
    let pressedStates = Array(6).fill(false);
    
    reportCategories.subscribe(value => {
        catDict = value;
    });
    
    function selection(key: number){
        pressedStates.fill(false);
        toggleSelected(key);
        value = catDict[key];
        $buttonNext = true;
    }

    function toggleSelected(index:number) {
        pressedStates[index] = !pressedStates[index];
    }

</script>

<div class="flex flex-col gap-4">
    <div class="flex flex-row justify-center space-x-40 mb-20">
        <button class="btn btn-lg btn-circle btn-primary {pressedStates[0] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(0)}>
            <div class="w-20 h-20 overflow-hidden">
                <img alt="Lightining Icon" src="{lightning_icon}" />              
            </div>
            ¡No tengo luz!    
        </button>

        <button class="btn btn-lg btn-circle btn-primary {pressedStates[1] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(1)}>
            <div class="w-20 h-20 overflow-hidden">
                <img alt="Water Drop Icon" src="{water_drop_icon}" />              
            </div>
            ¡No tengo agua!    
        </button>

        <button class="btn btn-lg btn-circle btn-primary {pressedStates[2] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(2)}>
            <div class="w-20 h-20 overflow-hidden">
                <img alt="Pothole Icon" src="{pothole_icon}" />              
            </div>
            Carretera Dañada   
        </button>
    </div>
    <div class="flex flex-row justify-center space-x-40 mb-20">
        <button class="btn btn-lg btn-circle btn-primary {pressedStates[3] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(3)}>
            <div class="w-20 h-20 overflow-hidden">
                <img alt="Electrical Pole Icon" src="{electrical_pole_icon}" />              
            </div>
            Poste Caído   
        </button>

        <button class="btn btn-lg btn-circle btn-primary {pressedStates[4] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(4)}>
            <div class="w-20 h-20 overflow-hidden">
            <img alt="Landslide Icon" src="{landslide_icon}" />              
            </div>
            Deslizamiento   
        </button>

        <button class="btn btn-lg btn-circle btn-primary {pressedStates[5] ? 'btn-active' : ''} text-sm text-base-content" on:click={() => selection(5)}>
            <div class="w-20 h-20 overflow-hidden">
                <img alt="Potential Landslide Icon" src="{landslidehazard_icon}" />              
            </div>
            Peligro de deslizamiento   
        </button>
    </div>
</div>