import type { PageServerLoad, Actions } from './$types';
import { postDashboardData } from '../../api/dashboard';

export const load = (async () => {
    return {};
}) satisfies PageServerLoad;

export const actions: Actions = {
    dashboardGraph: async ({ request }) => {
        console.log(request);
        // Await form data
        const formData = await request.formData();
        // Extract form data
        const var_1 = Object.fromEntries(formData).var_1 as string;
        const var_2 = Object.fromEntries(formData).var_2 as string;
        const var_2_val = Object.fromEntries(formData).var_2_val as string[];
        const var_opt = Object.fromEntries(formData).var_opt as string[];
        console.log(var_1, var_2, var_2_val, var_opt);
        // Send POST request to API server with form data
        const response = await postDashboardData(var_1, var_2, var_2_val, var_opt);
        // Process received data
        console.log(response);
    }
};