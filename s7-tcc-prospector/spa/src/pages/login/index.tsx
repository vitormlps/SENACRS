import { FC, useEffect, useState, useCallback } from 'react';
import { useNavigate } from 'react-router';

import loginImage from '../../assets/login-icon.svg';
import { useAuth } from '../../auth/hook';
import { theme } from '../../components';

const LoginPage: FC = () => {
	const auth = useAuth();
	const navigate = useNavigate();

	const [email, setEmail] = useState<string>('');
	const [password, setPassword] = useState<string>('');

	const login = useCallback(async () => {
		const user = await auth.manager.login(email, password);
		if (user.token) auth.setToken(user.token);
		auth.setUser(user);
	}, [auth, email, password]);

	useEffect(() => {
		if (!auth.token) {
			return;
		}
		if (auth.user) {
			navigate('/search');
		}
	}, [auth.user, navigate]);

	return (
		<div
			className='page flex column center space-evenly'
			style={{ backgroundColor: theme.palette.primary.main }}
		>
			<div
				className='box flex space-between p-3'
				style={{
					width: '50vw',
					height: '50vh',
					backgroundColor: theme.palette.background.default,
				}}
			>
				<div className='half flex column space-between'>
					<div className='text-center'>
						<h2 className='text-18 no-pm'>Bem vindo ao</h2>
						<div className='flex center' style={{ height: 43 }}>
							<h1 className='text-40 no-pm'>Data</h1>
							<h1
								className='text-40 no-pm'
								style={{ color: theme.palette.secondary.main }}
							>
								Trib
							</h1>
						</div>
					</div>
					<div
						style={{
							width: '100%',
							height: '300px',
							color: 'white',
							textAlign: 'center',
						}}
					>
						<img style={{ height: '100%' }} src={loginImage}></img>
					</div>
				</div>
				<hr
					style={{
						marginTop: '0',
						marginBottom: '2%',
						backgroundColor: '#d2d2d2',
						border: 'none',
						width: '1px',
					}}
				/>
				<div className='half flex column space-between'>
					<div className='text-center'>
						<h2 className='text-18 no-pm'>Log-in</h2>
					</div>
					<div className='container h-3 flex column space-evenly'>
						<div>
							<div className='flex column my-5'>
								<span>E-mail</span>
								<input
									className='p-1'
									type='text'
									required
									placeholder='usuario@email.com.br'
									value={email}
									onChange={(event) => {
										setEmail(event.target.value);
									}}
								/>
							</div>
							<div className='flex column my-5'>
								<span>Senha</span>
								<input
									className='p-1'
									type='password'
									required
									value={password}
									onChange={(event) => {
										setPassword(event.target.value);
									}}
								/>
							</div>
						</div>
						<button className='p-2' onClick={login}>
							<span className='text-14'>Entrar</span>
						</button>
					</div>
				</div>
			</div>
		</div>
	);
};

export default LoginPage;
