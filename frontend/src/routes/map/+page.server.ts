/* 
Server-side functions for Interactive Map and Dashboard page, all requests to the data server are handled here.
Functions here are used to fetch the statistics data corresponding to the selected filters in the Map or Dashboard. 
*/
// Imports
import type { PageServerLoad, Actions } from './$types';
import axios from 'axios';
import { redirect } from "@sveltejs/kit";

// Map Data Fetching
// API Server Link: https://averias-pr.onrender.com
export const load: PageServerLoad = (async () => {
    // Fetch map data
    const mapDataResponse = await axios.get('http://127.0.0.1:5000/averias/municipalities/map');
    console.log(mapDataResponse.data);
    const mapData = mapDataResponse.data;
    console.log(mapData.key);
    // const mapDataArray = [];
    // for (i =  of mapData[mapData.key]) {
    //     mapDataArray[item.municipality_name] = {
    //         population: item.population,
    //         total_reports: item.total_reports,
    //         common_cat: item.common_cat,
    //         resolved_reports: item.resolved_reports
    //     };
    //     console.log(mapDataArray)
    
    // }
        return {
            props: {
                mapStatistics: mapData
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


