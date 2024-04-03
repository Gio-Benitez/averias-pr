import { redirect } from "@sveltejs/kit";

/** @type {import('./$types').Actions} */
export const actions = {
    // @ts-ignore
    login: async ({cookies,request}) => {
        const formData = await request.formData();
        const email = formData.get("email");
        const password = formData.get("password");
        console.log(email,password) //Here we would send this shit or fetch backend
        // Dummy frontend authentication (This should be done by backend with db.getUser(email))
        if (email === "a@gmail.com" && password === "pass"){
            cookies.set("access", "true",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.delete("failedAuth",{path:"/",sameSite:"strict",httpOnly:true});
            //Redirect user to home page
            throw redirect(302,"/")
        }
        else {
            cookies.set("failedAuth", "true",{path:"/",sameSite:"strict",httpOnly:true});
            throw redirect(302,"/")
        }
    },
};