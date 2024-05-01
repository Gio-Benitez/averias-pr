/** @type {import('./$types').PageLoad} */
export function load({ cookies}) {
    if (cookies.get("access")==="true") {
        // @ts-ignore
        let user_data = JSON.parse(cookies.get("UserData"));
        return {
            access: true,
            failedAuth: false,
            UserData: user_data
        }
    }
    else if (cookies.get("failedAuth")==="true") {
        cookies.delete("failedAuth",{path:"/",sameSite:"strict",httpOnly:true});
        const path = cookies.get("failedAuthPath")
        cookies.delete("failedAuthPath",{path:"/",sameSite:"strict",httpOnly:true});
        return {
            access: false,
            failedAuth: true,
            failedPath: path
        }
    }
    else {
        return {
            access: false,
            failedAuth: false
        }
    }
    
};