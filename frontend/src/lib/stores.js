import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export let signedIn = writable(false);
export let isModalOpen = writable(false);