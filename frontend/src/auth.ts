import { SvelteKitAuth } from "@auth/sveltekit";
// import Github from "@auth/sveltekit/providers/github";
import Credentials from "@auth/sveltekit/providers/credentials";
import { checkUserExists } from "./api/auth";


export const { signIn, signOut, handle } = SvelteKitAuth({
    providers: [
        Credentials({
        credentials: {
            email: {},
            password: {},
        },
        authorize: async (credentials) => {
            let user = null;
            // TO-DO: Add hashing and salting

            // Check if user exists
            user = await checkUserExists(credentials.email as string, credentials.password as string);
            if (!user) {
                throw new Error("User not found.");
            }
            return user;
        }
        
        })
    ],
})