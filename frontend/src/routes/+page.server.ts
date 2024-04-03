import {redirect} from "@sveltejs/kit";
import { signedIn,isModalOpen } from "$lib/signinGlobalVars.js";


/** @type {import('./$types').Actions} */
export const actions = {
    // @ts-ignore
    login: async ({cookies,request}) => {
        try{
            const formData = await request.formData();
            const email = formData.get("email");
            const password = formData.get("password");
            console.log(email,password) //Here we would send this shit or fetch backend
            // Dummy frontend authentication (This should be done by backend with db.getUser(email))
            if (email === "a@gmail.com" && password === "pass"){
                cookies.set("access", "true",{path:"/",sameSite:"strict",httpOnly:true});
                //Redirect user to home page
                return {
                    success: true,
                }
                // throw redirect(302,"/")
            }
            return {
                success: false,
                email,
                message: "Email or password is not valid",
            };
        } catch (error) {
            console.error("Error:", error);

        }
    },
};