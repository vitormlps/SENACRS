import { FC } from 'react';
import { ThemeProvider } from '@mui/material/styles';

import RouterProvider from './routes';
import AuthProvider from './auth/provider';
import Theme from './components/theme';
import './css/App.css';

const App: FC = () => {
	return (
		<AuthProvider>
			<ThemeProvider theme={Theme}>
				<RouterProvider />
			</ThemeProvider>
		</AuthProvider>
	);
};

export default App;
