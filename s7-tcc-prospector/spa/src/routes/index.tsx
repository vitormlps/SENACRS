import { FC } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Outlet } from 'react-router-dom';

import PrivateRoute from './privateRoute';
import { UsersProvider } from '../hooks/users';
import { SideEntitiesProvider } from '../hooks/sideEntities';
import { EmpresasProvider } from '../hooks/empresas';
import { EstabelecimentosProvider } from '../hooks/estabelecimentos';
import { SociosProvider } from '../hooks/socios';
import { SimplesNacionalProvider } from '../hooks/simplesNacional';
import { SearchPage, LoginPage } from '../pages';

const paths = {
	home: '/',
	login: 'login',
	dashboard: 'dashboard',
	search: 'search',
	administration: 'administration',
};

const RouterProvider: FC = () => {
	return (
		<UsersProvider>
			<BrowserRouter>
				<Routes>
					<Route path={paths.login} element={<LoginPage />} />
					<Route path='*' element={<Navigate to='/login' />} />
					<Route element={<PrivateRoute />}>
						<Route
							path={paths.search}
							element={
								<SideEntitiesProvider>
									<EstabelecimentosProvider>
										<SociosProvider>
											<SimplesNacionalProvider>
												<EmpresasProvider>
													<Outlet />
												</EmpresasProvider>
											</SimplesNacionalProvider>
										</SociosProvider>
									</EstabelecimentosProvider>
								</SideEntitiesProvider>
							}
						>
							<Route index element={<SearchPage />} />
						</Route>
					</Route>
				</Routes>
			</BrowserRouter>
		</UsersProvider>
	);
};

export default RouterProvider;
