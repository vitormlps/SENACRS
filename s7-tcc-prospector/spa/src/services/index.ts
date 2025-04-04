import axios, { AxiosResponse } from 'axios';
import { AuthServices } from '../auth/service'


const apiUrl = import.meta.env.VITE_API_URL;
const api = axios.create({
        baseURL: apiUrl,
        headers: { 'Content-Type': 'application/json' },
    }
);

api.interceptors.request.use((config) => {       
        if (!config.url?.includes('auth')) {
            const token = AuthServices.token;
            if (token) {
                config.headers.Authorization = `Bearer ${token}`;
            }
        }
        return config;
    },
    (err) => Promise.reject(err)
);


api.interceptors.response.use((response: AxiosResponse) => {
        return Promise.resolve(response);
    },
    (err: any) => {
        let statusCode = err?.response?.status;

        if (statusCode === 401) {
            if (window.location.pathname !== '/') {
                window.location.href = '/';
            }
        }
        return Promise.resolve(err);
    }
);

export default api;
