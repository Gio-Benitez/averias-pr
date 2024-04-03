/** @type {import('./$types').PageLoad} */
export function load({ cookies }) {
    if (cookies.get("access")==="true") {
        return {
            access: true,
            failedAuth: false
        }
    }
    else if (cookies.get("failedAuth")==="true") {
        return {
            access: false,
            failedAuth: true
        }
    }
    else {
        return {
            access: false,
            failedAuth: false
        }
    }
    
};