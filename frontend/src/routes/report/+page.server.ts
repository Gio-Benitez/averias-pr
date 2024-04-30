import { redirect } from "@sveltejs/kit";
import { reset, steps_counter } from "$lib/stores.js";

/** @type {import('./$types').Actions} */
export const actions = {
    createReport: async ({cookies,request}) => {
        const formData = await request.formData();
        const location = formData.get("location");
        const municipality = formData.get("municipality");
        const category = formData.get("category");
        const image = formData.get("image");

        // Create report that will be sent to database
        
        throw redirect(302,"/");
    }
}
