import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export let signedIn = writable(false);
export let isSignInModalOpen = writable(false);
export let isCreateAccountModalOpen = writable(false);
export let isForgotPasswordModalOpen = writable(false);
export let invalidAuth = writable(false);
export let buttonNext = writable(false);
export let steps_counter = writable(0);

const municipalityNames = [
    "Adjuntas", "Aguada", "Aguadilla", "Aguas Buenas", "Aibonito", "Añasco", "Arecibo",
    "Arroyo", "Barceloneta", "Barranquitas", "Bayamón", "Cabo Rojo", "Caguas", "Camuy",
    "Canóvanas", "Carolina", "Cataño", "Cayey", "Ceiba", "Ciales", "Cidra", "Coamo",
    "Comerío", "Corozal", "Culebra", "Dorado", "Fajardo", "Florida", "Guánica", "Guayama",
    "Guayanilla", "Guaynabo", "Gurabo", "Hatillo", "Hormigueros", "Humacao", "Isabela",
    "Jayuya", "Juana Díaz", "Juncos", "Lajas", "Lares", "Las Marías", "Las Piedras",
    "Loíza", "Luquillo", "Manatí", "Maricao", "Maunabo", "Mayagüez", "Moca", "Morovis",
    "Naguabo", "Naranjito", "Orocovis", "Patillas", "Peñuelas", "Ponce", "Quebradillas",
    "Rincón", "Río Grande", "Sabana Grande", "Salinas", "San Germán", "San Juan",
    "San Lorenzo", "San Sebastián", "Santa Isabel", "Toa Alta", "Toa Baja", "Trujillo Alto",
    "Utuado", "Vega Alta", "Vega Baja", "Vieques", "Villalba", "Yabucoa", "Yauco"
];
export let municipalities = writable(municipalityNames);

const categories = {
    0: 'Servicio de Luz',
    1: 'Servicio de Agua',
    2: 'Carretera Dañada',
    3: 'Poste Caido',
    4: 'Deslizamiento',
    5: 'Peligro de Deslizamiento'
};

export const reportCategories = writable(categories);

// Handler for when you press reset button
export function reset() {
    steps_counter.set(0);
    buttonNext.set(false);
}

// Handler for when you press next button
export function forward() {
    steps_counter.update((n) => n + 1);
    buttonNext.set(false);
}

// Handler for when you press back button
export function backward() {
    steps_counter.update((n) => n - 1);
    buttonNext.set(true);
}