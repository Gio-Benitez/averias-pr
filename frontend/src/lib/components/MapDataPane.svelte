<script lang="ts">
    import mapDataStore from "$lib/stores";
</script>

<div class="card grow-0 shrink-0 min-w-full min-h-full font-Alpino text-secondary-content bg-secondary shadow-lg " >
    <div class="card-body">
        <h1 class="card-title justify-center">{$mapDataStore.dataRegion}</h1>
        <div class="grid min-w-full  grid-col-2 grid-row-5 grid-flow-row gap-y-4">
            <div class="SmallCard">
                <p># of Reports</p>
                <h1>{$mapDataStore.numOfReports}</h1>
            </div>
            <div class="SmallCard">
                <p>Population</p>
                <h1>{$mapDataStore.populationData}</h1>
            </div>
            <div class="SmallCard">
                <p>Stat 1</p>
                <h1>{$mapDataStore.stat1}</h1>
            </div> 
            <div class="SmallCard">
                <p>Stat 2</p>
                <h1>{$mapDataStore.stat2}</h1>
            </div>     
        </div>
    </div>
</div>

<style lang="postcss">
    .SmallCard {
        @apply flex flex-wrap col-span-1 row-span-1 bg-primary rounded shadow px-2 py-4 w-full h-full text-secondary-content;
    }

    h1 {
        @apply font-black text-3xl text-right align-middle;
    }
    p {
        @apply font-medium text-lg text-left align-middle;
    }
    
</style>