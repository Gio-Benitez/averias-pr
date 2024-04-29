<script lang="ts">
    import { mapDataStore } from "$lib/stores";
</script>

<div class="card grow-0 shrink-0 min-w-full min-h-full font-Alpino text-primary-content bg-primary shadow-lg " >
    <h1 class="card-title justify-center pt-8">{$mapDataStore.dataRegion}</h1>
    <div class="card-body">
        <div class="grid min-w-full gap-y-4 grid-col-2 grid-row-12 grid-flow-auto">
            <div class="grid grid-rows-subgrid col-span-2 row-start-5 row-span-5">
                <div class="stats-horizontal">
                    <div class="stat w-1/2 col-span-1 shadow-lg">
                        <div class="stat-title"># of Reports</div>
                        <div class="stat-value">{$mapDataStore.numOfReports}</div>
                    </div>
                    <div class="stat w-1/2 col-span-1 shadow-lg">
                        <div class="stat-title">Population</div>
                        <div class="stat-value">{$mapDataStore.populationData}</div>
                    </div>
                    <div class="stat w-1/2 col-span-1 shadow-lg">
                        <div class="stat-title">Stat 1</div>
                        <div class="stat-value">{$mapDataStore.stat1}</div>
                    </div> 
                    <div class="stat w-1/2 col-span-1 shadow-lg">
                        <div class="stat-title">Stat 2</div>
                        <div class="stat-value">{$mapDataStore.stat2}</div>
                    </div>
                </div> 
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