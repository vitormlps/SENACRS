import { FC } from 'react';

import CircularProgress from '@mui/material/CircularProgress';

const LoadingDisplay: FC<any> = (params: any) => {
	return (
		<div className={params.classNames}>
			<CircularProgress color='primary' />
			<div>
				<h1>Carregando</h1>
			</div>
		</div>
	);
};

export default LoadingDisplay;
