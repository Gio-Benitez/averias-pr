import { redirect } from "@sveltejs/kit";
import axios from 'axios';

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

    createAccount: async ({cookies,request}) => {
        const formData = await request.formData();
        const email = formData.get("Email");
        const password = formData.get("PasswordHash");
        const passwordConf = formData.get("PasswordConf");
        console.log(email, password, passwordConf);

        // const sendData = () => {
        //     let formu = document.getElementById('formu');
        //     axios.post('http://localhost:5000/averias/users/', new FormData(formu))
        //           .then(res => {
        //               console.log(res);
        //           })
        // }
        // Do backend stuff here
        if (password === passwordConf) {
            // Do backend shit
            cookies.set("access", "true",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.delete("failedAuth",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.delete("failedAuthPath",{path:"/",sameSite:"strict",httpOnly:true});
            //Redirect user to home page
            throw redirect(302,"/")
        }
        else{
            cookies.set("failedAuth", "true",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.set("failedAuthPath", "create",{path:"/",sameSite:"strict",httpOnly:true});
            throw redirect(302,"/")
        }
    },

    forgotPassword: async ({cookies,request}) => {
        const formData = await request.formData();
        const email = formData.get("email");
        const password = formData.get("password");
        const passwordConf = formData.get("password-confirmation");
        console.log(email, password, passwordConf);
        // Do backend stuff here
        if (password === passwordConf) {
            // Do backend shit
            cookies.set("access", "true",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.delete("failedAuth",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.delete("failedAuthPath",{path:"/",sameSite:"strict",httpOnly:true});
            //Redirect user to home page
            throw redirect(302,"/")
        }
        else{
            cookies.set("failedAuth", "true",{path:"/",sameSite:"strict",httpOnly:true});
            cookies.set("failedAuthPath", "forgot",{path:"/",sameSite:"strict",httpOnly:true});
            throw redirect(302,"/")
        }
    }
};