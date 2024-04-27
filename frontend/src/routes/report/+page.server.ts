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


// /** @type {import('./$types').PageLoad} */
// export async function load({ cookies, fetch }) {
//     // Retrieve form data from Step 1
//     const step1FormData = await fetch('/reportstep1/data');
//     const { location, municipality } = await step1FormData.json();

//     console.log(location)
//     console.log(municipality)
// }