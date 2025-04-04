import api from '../services';
import { IUsers } from '../types';

export interface IAuth {
	url: string;
    token: string;
}

export class AuthServices {

    url: string = import.meta.env.VITE_AUTH_PREFIX;
    hasInit: boolean = false;
    authenticated: boolean = false;
    static token: string;
    onTokenExpired: () => void = () => {};

    constructor () {}

    async init(): Promise<any> {
        this.hasInit = true;

    }

    async login(email: string, password: string): Promise<IUsers> {
        const response = await api.post(
            this.url, 
            {
                email: email,
                psw: password,
            }
        );

        if (response.data && response?.request?.status === 200) {
            this.authenticated = true;
            return response.data

        }
        const error = Error(response.data as string);
        console.log(error);
        throw error
    }

    async loadUserProfile(): Promise<any> {
    }

    async updateToken(): Promise<any> {
    }

    unloadAuthentication = () => {
    };
    
}