import type { PageServerLoad, Actions } from './$types';

export const load = (async () => {
    return {};
}) satisfies PageServerLoad;

export const actions: Actions = {
    dashboardGraph: async ({ request }) => {
        console.log(request);
        const formData = await request.formData();
        console.log(Object.fromEntries(formData));
        const var_1 = Object.fromEntries(formData).var_1 as string;
        const var_2 = Object.fromEntries(formData).var_2 as string;
        const var_2_val = Object.fromEntries(formData).var_2_val as string;
        
        console.log(var_1, var_2, var_2_val);
    }
};