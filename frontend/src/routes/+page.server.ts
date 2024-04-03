import {redirect} from "@sveltejs/kit";
import { signedIn,isModalOpen } from "$lib/signinGlobalVars.js";


/** @type {import('./$types').Actions} */
export const actions = {
    // @ts-ignore
    login: async ({cookies,request}) => {
        const formData = await request.formData();
        const email = formData.get("email");
        const password = formData.get("password");
        console.log(email,password) //Here we would send this shit or fetch backend
        // Dummy frontend authentication (This should be done by backend with db.getUser(email))
        if (email === "crack@gmail.com" && password === "password"){
            cookies.set("access", "true",{path:"/",sameSite:"strict",httpOnly:true});
            signedIn.set(true);
            //Redirect user to home page
            throw redirect(302,"/")
        }
        isModalOpen.set(false);
        return {
            email,
            message: "Email or password is not valid",
        };
    },
};