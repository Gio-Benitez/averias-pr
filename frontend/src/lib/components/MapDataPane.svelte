<script lang="ts">
    import mapDataStore from "$lib/stores";
</script>

<div class="card flex-grow flex-shrink w-full h-full font-Alpino text-black bg-slate-200  shadow-lg">
    <div class="card-body">
        <h1 class="card-title justify-center">{$mapDataStore.dataRegion}</h1>
        <div class="flex flex-nowrap space-x-4">
            <div class="SmallCard">
                <p># of Reports</p>
                <h1>{$mapDataStore.numOfReports}</h1>
            </div>
            <div class="SmallCard">
                <p>Population</p>
                <h1>{$mapDataStore.populationData}</h1>
            </div>      
        </div>
    </div>
</div>

<style lang="postcss">
    .SmallCard {
        @apply flex flex-wrap bg-secondary rounded shadow px-2 py-4 w-full h-full text-center justify-center text-secondary-content;
    }

    h1 {
        @apply font-black text-3xl;
    }
    p {
        @apply font-medium text-lg;
    }
    
</style>