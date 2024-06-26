import type { PageServerLoad, Actions } from './$types';
import axios from 'axios';
import { SERVER_URL } from '$env/static/private';


const prod_url: string = SERVER_URL;
const form_route: string = '/averias/report_data';
const prod_form_route: string = prod_url + form_route;
// eslint-disable-next-line @typescript-eslint/no-unused-vars


export const load: PageServerLoad = async (events) => {

    const session = await events.locals.auth()
    // if (cookies.get("access")==="true") {
    //     const user_data = JSON.parse(cookies.get("UserData"));
    //     return {
    //         access: true,
    //         failedAuth: false,
    //         UserData: user_data
    //     }
    // }
    // else if (cookies.get("failedAuth")==="true") {
    //     cookies.delete("failedAuth",{path:"/",sameSite:"strict",httpOnly:true});
    //     const path = cookies.get("failedAuthPath")
    //     cookies.delete("failedAuthPath",{path:"/",sameSite:"strict",httpOnly:true});
    //     return {
    //         access: false,
    //         failedAuth: true,
    //         failedPath: path
    //     }
    // }
    // else {
    //     return {
    //         access: false,
    //         failedAuth: false
    //     }
    // }
    return {
        session,
    }
};

export const actions: Actions = {
    submitReport: async ({ request }) => {
        // Receive form data from Report Form component
        const formData = await request.formData();
        // Extract data from form data
        const reportData = Object.fromEntries(formData);
        // Send a POST request to the server to submit the report
        let message = '';
        await axios.post(prod_form_route, reportData)
        .then(res=> {
            console.log(res.data);
            message = res.data.message;
        })
        .catch(error => {
            // Handle error response here
            if (error.response) {
                console.error('Error:', error.response.data.error); // Log the error message
                // Handle the error message here (e.g., display it on the UI)
                message = error.response.data.error;
            } else {
                console.error('Error:', error);
            }
        });
        return {
            props: {
                message
            }
        };
    }
};