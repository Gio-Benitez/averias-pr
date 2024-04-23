<script lang="ts">
    import { mapDataStore } from "$lib/stores";
</script>
<div class="flex flex-col flex-wrap w-full h-full bg-primary px-8 py-12 rounded-2xl">
    <div class="flex flex-col w-full h-2/5 text-center gap-1">
        <h1>Filters</h1>
        <div class="divider divider-neutral"></div>
        <div class="dropdown">
            <div tabindex="0" role="button" class="btn m-1 w-full">Select Region</div>
            <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
            <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-full">
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </div>
        <div class="dropdown">
            <div tabindex="0" role="button" class="btn m-1 w-full">Select Report Category</div>
            <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
            <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-full">
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </div>
    </div>
    <div class="flex flex-col w-full h-1/5 text-center">
        <h1>Statistics</h1>
        <div class="divider divider-neutral"></div>
    </div>
    <div class="flex flex-col flex-wrap w-full h-2/5 text-center gap-2">
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title"># of Reports</div>
            <div class="stat-value">{$mapDataStore.numOfReports}</div>
        </div>
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Population</div>
            <div class="stat-value">{$mapDataStore.populationData}</div>
        </div>
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Stat 1</div>
            <div class="stat-value">{$mapDataStore.stat1}</div>
        </div> 
        <div class="stat w-1/2 shadow-lg">
            <div class="stat-title">Stat 2</div>
            <div class="stat-value">{$mapDataStore.stat2}</div>
        </div>
    </div>
    
</div>

<style lang="postcss">
    h1 {
        @apply text-primary-content text-3xl font-bold;
    }
    .stat-title {
        @apply text-primary-content text-lg;
    }
    .stat-value {
        @apply text-primary-content text-2xl;
    }
</style>
