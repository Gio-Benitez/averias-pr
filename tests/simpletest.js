import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    // Tests one user conducting many requests over 10 seconds
    // vus: 1,
    // duration: '10s'

    // Load Test: Tests 200 users entering the site over a 5m period, staying for 20m, then slowly leaving the site over 5m
    // stages: [
    //     {duration: '5m', target: 200}, // Ramp up
    //     {duration: '20m', target: 200}, // Stable
    //     {duration: '5m', target: 0}, // Ramp-down to 0 users
    // ],

    // Stress Test: Increase load gradually to see how much server can take
    // stages: [
    //     {duration: '1m', target: 200}, // Ramp up
    //     {duration: '5m', target: 200}, // Stable
    //     {duration: '1m', target: 800}, // Ramp up
    //     {duration: '5m', target: 800}, // Stable
    //     {duration: '1m', target: 1000}, // Ramp up
    //     {duration: '5m', target: 1000}, // Stable
    //     {duration: '5m', target: 0}, // Ramp up
    // ],

    // Spike Test: Quickly inrease amount of traffic for a short time (burst in traffic)
    stages: [
        {duration: '30s', target: 2000},
        {duration: '2m', target: 2000},
        {duration: '30s', target: 0},
    ],
};

export default () => {
    http.get('https://averias-pr.vercel.app');
    sleep(1) // For Load Testing (many users submitting many requests)
}