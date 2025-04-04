import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../auth/hook';

export interface IPrivateRouteProps {
	children: Array<JSX.Element> | JSX.Element;
}

const PrivateRoute = () => {
	const auth = useAuth();
	return auth.token ? <Outlet /> : <Navigate to='/login' />;
};

export default PrivateRoute;
