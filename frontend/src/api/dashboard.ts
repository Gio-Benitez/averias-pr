import axios from 'axios';

export async function postData(var_1: string, var_2: string, var_2_val: string, var_opt: string) {
    const url = 'https://your-api-endpoint.com'; // replace with your API endpoint
    const data = {
        var_1: var_1,
        var_2: var_2,
        var_2_val: var_2_val,
        var_opt: var_opt
    };

    try {
        const response = await axios.post(url, data);
        console.log(response.data);
        return response.data;
    } catch (error) {
        console.error(`Error posting data: ${error}`);
    }
}