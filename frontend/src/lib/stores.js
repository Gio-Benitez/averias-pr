import { writable, readable } from 'svelte/store';

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
    population: 3205691,
    reportCategory: 'All',
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

// Filter Stores
export const reportCategories = readable({
    categoryArray: ['All', 'Acera Rota', 'Alcantarilla', 'Carretera Rota', 'Poste de Luz']
});
export const municipios = readable({
    municipiosArray: ['Adjuntas', 'Aguada', 'Aguadilla', 'Aguas Buenas', 'Aibonito', 'Añasco', 'Arecibo', 'Arroyo', 'Barceloneta', 'Barranquitas', 'Bayamón', 'Cabo Rojo', 'Caguas', 'Camuy', 'Canóvanas', 'Carolina', 'Cataño', 'Cayey', 'Ceiba', 'Ciales', 'Cidra', 'Coamo', 'Comerío', 'Corozal', 'Culebra', 'Dorado', 'Fajardo', 'Florida', 'Guánica', 'Guayama', 'Guayanilla', 'Guaynabo', 'Gurabo', 'Hatillo', 'Hormigueros', 'Humacao', 'Isabela', 'Jayuya', 'Juana Díaz', 'Juncos', 'Lajas', 'Lares', 'Las Marías', 'Las Piedras', 'Loíza', 'Luquillo', 'Manatí', 'Maricao', 'Maunabo', 'Mayagüez', 'Moca', 'Morovis', 'Naguabo', 'Naranjito', 'Orocovis', 'Patillas', 'Peñuelas', 'Ponce', 'Quebradillas', 'Rincón', 'Río Grande', 'Sabana Grande', 'Salinas', 'San Germán', 'San Juan', 'San Lorenzo', 'San Sebastián', 'Santa Isabel', 'Toa Alta', 'Toa Baja', 'Trujillo Alto', 'Utuado', 'Vega Alta', 'Vega Baja', 'Vieques', 'Villalba', 'Yabucoa', 'Yauco']
});
