export async function load() {
    
    const userData = {
      
    };
    console.log(userData);
    }
    



export const actions = {
    userSelection: async ({ request }) => {
        const formData = await request.formData();
        const user = Object.fromEntries(formData);
        console.log(user);
    }
}