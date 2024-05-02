import axios from 'axios';

export async function checkUserExists(email: string, password: string) {
    //const url = 'https://averias-pr.onrender.com/test'; // replace with your API endpoint
    const url = 'http://127.0.0.1:5000/averias/users/verify_user_email/';
    const data = {
        email: email,
        password: password
    };

    try {
        const response = await axios.post(url, data);
        console.log(response.data);
        return response.data;
    } catch (error) {
        console.error(`Error posting data: ${error}`);
    }
};