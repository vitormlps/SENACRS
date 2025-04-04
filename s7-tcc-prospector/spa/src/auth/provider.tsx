import React from 'react';
import AuthContext from './context';
import { AuthServices } from './service';
import { IUsers } from '../types';

export interface IAuthenticationProps {
	children: Array<JSX.Element> | JSX.Element | undefined;
}

export default function AuthProvider(props: IAuthenticationProps) {
	const [manager, _] = React.useState(new AuthServices());
	const [token, _setToken] = React.useState<string>('');
	const [user, setUser] = React.useState<IUsers | undefined>();

	const setToken = (newToken: string) => {
		AuthServices.token = newToken;
		_setToken(newToken);
	};

	return (
		<AuthContext.Provider
			value={{
				manager,
				token,
				setToken,
				user,
				setUser,
			}}
		>
			{props.children}
		</AuthContext.Provider>
	);
}
