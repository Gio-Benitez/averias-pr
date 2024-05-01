/* 
Server-side functions for Interactive Map and Dashboard page, all requests to the data server are handled here.
Functions here are used to fetch the statistics data corresponding to the selected filters in the Map or Dashboard. 
*/

// Imports
import type { PageServerLoad, Actions } from './$types';

// Map Data Stores


// Dashboard Data Stores


// Map Data Fetching

export const load: PageServerLoad = (async () => {
    // Fetch map data
    //const mapDataResponse = await fetch('/api/map-data');

    const whatIwant = {
        'Adjuntas': {
            'population': 1000,
            'total_reports': 5,
            'common_cat': 'Acera Rota',
            'resolved_reports': 2
        },
        'Aguada': {
            'population': 2000,
            'total_reports': 10,
            'common_cat': 'Pothole',
            'resolved_reports': 5
        }
        //etc...
        }
        
        const mapData = {
            dataRegion: 'Puerto Rico',
            numOfReports: 110,
            population: 3205691,
            reportCategory: 'Carretera Rota',
            resolved: 0
        }
        //const mapData = await mapDataResponse.json();
    
        return {
            props: {
                mapData,
                whatIwant
            }
        };
    });


export const actions: Actions = {
    mapCategorySelection: async ({ request }) => {
        console.log(request);
        const formData = await request.formData();
        console.log(Object.fromEntries(formData));
        const region = Object.fromEntries(formData).region as string;
        const category = Object.fromEntries(formData).category as string;
        console.log(region, category);
        // TO-DO: Send a fetch request to the data server to get the data for the selected region and category
        

        // TO-DO: Return data from request properly formatted
        
        const mapData = {
            dataRegion: region,
            numOfReports: 5,
            population: 2000,
            reportCategory: category,
            resolved: 0
        }
        return { 
            props: {
                mapData
            }
        };
    },

    dashboardGraph: async ({ request }) => {
        console.log(request);
        const formData = await request.formData();
        console.log(Object.fromEntries(formData));
        const var_1 = Object.fromEntries(formData).var_1 as string;
        const var_2 = Object.fromEntries(formData).var_2 as string;
        const var_2_opt = Object.fromEntries(formData).var_2_opt as string;
        
        console.log(var_1, var_2, var_2_opt);
    }

};

// Dashboard Data Fetching

