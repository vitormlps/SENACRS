import { createContext } from 'react';
import { AuthServices } from './service';
import { IUsers } from '../types';

export interface AuthContext {
	manager: AuthServices;
	token: string;
	setToken: (newToken: string) => void;
	user?: IUsers;
	setUser: React.Dispatch<React.SetStateAction<IUsers | undefined>>;
}

const AuthContext = createContext<AuthContext>({} as AuthContext);

export default AuthContext;
