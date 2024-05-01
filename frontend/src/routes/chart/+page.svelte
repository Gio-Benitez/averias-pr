<script>
    export let data;
    import { municipios } from '$lib/stores.js';

    let selectedUser = '';
    let selectedAsset = '';

    function handleUserChange(event) {
        selectedUser = event.target.value;
        selectedAsset = ''; // Reset selected course when user changes
    }

    function handleCourseChange(event) {
        selectedAsset = event.target.value;
    }

    async function showSelection() {
        console.log('Selected User:', selectedUser);
        console.log('Selected Course:', selectedAsset);
    }
</script>

<div>
    {#if data}
        <form action="?/userSelection" method="POST">
            <select
                class="select select-accent w-full max-w-xs"
                value={selectedUser}
                on:change={handleUserChange}
            >
                <option disabled selected>Select a User</option>
                {#each $municipios.municipiosList as user}
                    <option name="user" value={user.muni_id}>{user.muni_id}</option>
                {/each}
            </select>
            {#if selectedUser !== ''}
                <select
                    class="select select-accent w-full max-w-xs"
                    value={selectedAsset}
                    on:change={handleCourseChange}
                >
                    <option disabled selected>Select a Course</option>
                    {#each $municipios.municipiosList.find((user) => user.name === selectedUser)?.name || [] as course}
                        <option name="course" value={course}>{course}</option>
                    {/each}
                </select>
            {/if}
            <button type="button" on:click={showSelection}>Get Data</button>
        </form>
    {:else}
        <p>Loading...</p>
    {/if}
</div>