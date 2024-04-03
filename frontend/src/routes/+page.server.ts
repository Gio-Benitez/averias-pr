/** @type {import('./$types').PageLoad} */
export function load({ cookies }) {
    if (cookies.get("access")==="true") {
        return {
            access: true
        }
    }
    return {
        access: false
    }
};