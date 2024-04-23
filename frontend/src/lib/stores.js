import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export let signedIn = writable(false);
export let isSignInModalOpen = writable(false);
export let isCreateAccountModalOpen = writable(false);
export let isForgotPasswordModalOpen = writable(false);
export let invalidAuth = writable(false);

// Interactive Map Stores
// Initialize Map data panel with default values (Stats for all of Puerto Rico)
export let mapDataStore = writable({
    dataRegion: 'Puerto Rico',
    numOfReports: 100,
    populationData: 0,
    stat1: 0,
    stat2: 0
});


// Dashboard Stores
export let dashboardStore = writable({
    chartType: '',
    xaxis: 100,
    yaxis: 0,
    filter1: 0,
    filter2: 0
});

