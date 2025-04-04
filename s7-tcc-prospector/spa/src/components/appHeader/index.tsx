import { FC } from 'react';
import { AppBar } from '@mui/material';
import { theme } from '..';

const AppHeader: FC = () => {
	return (
		<AppBar
			color='transparent'
			position='static'
			elevation={0}
			style={{
				display: 'flex',
				flexDirection: 'row',
				justifyContent: 'space-between',
			}}
		>
			<div className='flex' style={{ height: 43 }}>
				<h1 className='m-0'>Data</h1>
				<h1 className='m-0' style={{ color: theme.palette.secondary.main }}>
					Trib
				</h1>
			</div>
		</AppBar>
	);
};

export default AppHeader;
