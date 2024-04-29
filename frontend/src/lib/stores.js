import { writable, readable } from 'svelte/store';

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

// Report Categories used for filters in /map route
const filterCategories = [
    'Servicio de Luz',
    'Servicio de Agua',
    'Carretera Dañada',
    'Poste Caido',
    'Deslizamiento',
    'Peligro de Deslizamiento'
];
export const filterCategoriesStore = writable(filterCategories);

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

// Interactive Map Stores
// Initialize Map data panel with default values (Stats for all of Puerto Rico)
export let mapDataStore = writable({
    dataRegion: 'Puerto Rico',
    numOfReports: 110,
    population: 3205691,
    reportCategory: 'Carretera Rota',
    resolved: 0
});


// Dashboard Stores
export let dashboardStore = writable({
    chartType: 'Bar',
    xaxis: 'Municipio',
    yaxis: '# de Reportes',
    requiredFilter: 'Por Municipio',
    optionalFilter: 'Por Categoría',
    chartData: {},
});


export const municipios = readable({
    municipiosList: [
        { muni_id: 1, name: 'Adjuntas' },
        { muni_id: 2, name: 'Aguada' },
        { muni_id: 3, name: 'Aguadilla' },
        { muni_id: 4, name: 'Aguas Buenas' },
        { muni_id: 5, name: 'Aibonito' },
        { muni_id: 6, name: 'Añasco' },
        { muni_id: 7, name: 'Arecibo' },
        { muni_id: 8, name: 'Arroyo' },
        { muni_id: 9, name: 'Barceloneta' },
        { muni_id: 10, name: 'Barranquitas' },
        { muni_id: 11, name: 'Bayamón' },
        { muni_id: 12, name: 'Cabo Rojo' },
        { muni_id: 13, name: 'Caguas' },
        { muni_id: 14, name: 'Camuy' },
        { muni_id: 15, name: 'Canóvanas' },
        { muni_id: 16, name: 'Carolina' },
        { muni_id: 17, name: 'Cataño' },
        { muni_id: 18, name: 'Cayey' },
        { muni_id: 19, name: 'Ceiba' },
        { muni_id: 20, name: 'Ciales' },
        { muni_id: 21, name: 'Cidra' },
        { muni_id: 22, name: 'Coamo' },
        { muni_id: 23, name: 'Comerío' },
        { muni_id: 24, name: 'Corozal' },
        { muni_id: 25, name: 'Culebra' },
        { muni_id: 26, name: 'Dorado' },
        { muni_id: 27, name: 'Fajardo' },
        { muni_id: 28, name: 'Florida' },
        { muni_id: 29, name: 'Guánica' },
        { muni_id: 30, name: 'Guayama' },
        { muni_id: 31, name: 'Guayanilla' },
        { muni_id: 32, name: 'Guaynabo' },
        { muni_id: 33, name: 'Gurabo' },
        { muni_id: 34, name: 'Hatillo' },
        { muni_id: 35, name: 'Hormigueros' },
        { muni_id: 36, name: 'Humacao' },
        { muni_id: 37, name: 'Isabela' },
        { muni_id: 38, name: 'Jayuya' },
        { muni_id: 39, name: 'Juana Díaz' },
        { muni_id: 40, name: 'Juncos' },
        { muni_id: 41, name: 'Lajas' },
        { muni_id: 42, name: 'Lares' },
        { muni_id: 43, name: 'Las Marías' },
        { muni_id: 44, name: 'Las Piedras' },
        { muni_id: 45, name: 'Loíza' },
        { muni_id: 46, name: 'Luquillo' },
        { muni_id: 47, name: 'Manatí' },
        { muni_id: 48, name: 'Maricao' },
        { muni_id: 49, name: 'Maunabo' },
        { muni_id: 50, name: 'Mayagüez' },
        { muni_id: 51, name: 'Moca' },
        { muni_id: 52, name: 'Morovis' },
        { muni_id: 53, name: 'Naguabo' },
        { muni_id: 54, name: 'Naranjito' },
        { muni_id: 55, name: 'Orocovis' },
        { muni_id: 56, name: 'Patillas' },
        { muni_id: 57, name: 'Peñuelas' },
        { muni_id: 58, name: 'Ponce' },
        { muni_id: 59, name: 'Quebradillas' },
        { muni_id: 60, name: 'Rincón' },
        { muni_id: 61, name: 'Río Grande' },
        { muni_id: 62, name: 'Sabana Grande' },
        { muni_id: 63, name: 'Salinas' },
        { muni_id: 64, name: 'San Germán' },
        { muni_id: 65, name: 'San Juan' },
        { muni_id: 66, name: 'San Lorenzo' },
        { muni_id: 67, name: 'San Sebastián' },
        { muni_id: 68, name: 'Santa Isabel' },
        { muni_id: 69, name: 'Toa Alta' },
        { muni_id: 70, name: 'Toa Baja' },
        { muni_id: 71, name: 'Trujillo Alto' },
        { muni_id: 72, name: 'Utuado' },
        { muni_id: 73, name: 'Vega Alta' },
        { muni_id: 74, name: 'Vega Baja' },
        { muni_id: 75, name: 'Vieques' },
        { muni_id: 76, name: 'Villalba' },
        { muni_id: 77, name: 'Yabucoa' },
        { muni_id: 78, name: 'Yauco' }
    ]
});
