// place files you want to import through the `$lib` alias in this folder.

// Font Awesome Alias as Fa for simplicity
export { FontAwesomeIcon as Fa } from '@fortawesome/svelte-fontawesome';

// Interface for the data used to populate the Map Data Panel
export interface MapData {
    municipality: string;
    category: string;
    population: number;
    totalReports: number;
    mostCommonCategory: string;
    totalResolvedReports: number;
}

// Interface for the data used to populate the Dashboard Filters Panel
export interface DashboardFilters {
    y_axis_label: string;
    x_axis_label: string;
    x_axis_label_secondary: string;
    x_axis_values: string[];
    x_axis_values_secondary: string[];
}
