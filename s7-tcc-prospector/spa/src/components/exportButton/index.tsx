import { FC, useEffect, useState } from 'react';
import { Button } from '@mui/material';

import { theme } from '..';
import { IEmpresasButton } from '../../types';
import CircularProgress from '@mui/material/CircularProgress';

const element = <span className='flex center bold text nowrap m-0'>Exportar pesquisa</span>;

const ExportButton: FC<IEmpresasButton> = (params: IEmpresasButton) => {
	const [isClicked, setIsClicked] = useState(false);
	const [text, setText] = useState(element);

	useEffect(() => {
		if (params.exportingFile) {
			setText(<CircularProgress color='secondary' size='2rem' />);
		} else {
			setText(element);
		}
	}, [params.exportingFile]);

	return (
		<Button
			style={{
				minWidth: 'fit-content',
				color: theme.palette.common.white,
				backgroundColor: params.exportingFile
					? theme.palette.common.white
					: theme.palette.secondary.main,
			}}
			disabled={params.selectedIds.length === 0}
			variant='contained'
			disableRipple
			disableElevation
			onClick={() => {
				setIsClicked(!isClicked);
				params.service(params.selectedIds);
				setIsClicked(!isClicked);
			}}
		>
			{text}
		</Button>
	);
};

export default ExportButton;
