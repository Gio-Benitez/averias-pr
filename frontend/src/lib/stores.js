import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export let signedIn = writable(false);
export let isSignInModalOpen = writable(false);
export let isCreateAccountModalOpen = writable(false);
export let isForgotPasswordModalOpen = writable(false);
export let invalidAuth = writable(false);

// Interactive Map Stores
// Initialize Map data panel with default values (Stats for all of Puerto Rico)
let mapDataStore = writable({
    dataRegion: 'Puerto Rico',
    numOfReports: 100,
    populationData: 0,
    stat1: 0,
    stat2: 0
});

export default mapDataStore;