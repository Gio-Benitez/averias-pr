import { SvelteKitAuth } from '@auth/sveltekit'
import GitHub from '@auth/sveltekit/providers/github'
import Credentials from '@auth/sveltekit/providers/credentials'
import { GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET } from '$env/static/private'
import axios from 'axios';
import { SERVER_URL } from '$env/static/private';

const auth_login = SERVER_URL + '/averias/users/login';

export const { signIn, signOut, handle } = SvelteKitAuth({
    providers: 
        [
            // Github OAuth
            GitHub({clientId: GITHUB_CLIENT_ID, clientSecret: GITHUB_CLIENT_SECRET}),
            // Email and password Authentication
            Credentials({
                credentials: {
                    email: {},
                    password: {}
                },
                authorize: async (credentials) => {
                    // eslint-disable-next-line prefer-const
                    let user = {
                        id: '',
                        name: '',
                        email: '',
                        image: ''
                    };
                    // Salt and Hash user password
                    const userCredentials = {
                        Email: credentials.email,
                        Password: credentials.password
                    };
                    await axios.post(auth_login, userCredentials)
                    .then((res) => {
                        user.id = res.data.user_id;
                        user.name = res.data.name;
                        user.email = res.data.email;
                    });
                    return user;
                }
            })
        ],
})

