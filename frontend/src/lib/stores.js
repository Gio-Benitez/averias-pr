import { writable } from 'svelte/store';

// Initialize the store with the initial value (e.g., false for not logged in)
export let signedIn = writable(false);
export let isSignInModalOpen = writable(false);
export let isCreateAccountModalOpen = writable(false);
export let isForgotPasswordModalOpen = writable(false);
export let invalidAuth = writable(false);

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