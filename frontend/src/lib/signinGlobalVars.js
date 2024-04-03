// src/lib/signinGlobalVars.js

import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export const myObject = writable({
    message: '',
    isModalOpen: true,
    signedIn: true
});
// export const signedIn = writable(false);
// export const isModalOpen = writable(false);




