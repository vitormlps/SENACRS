import { FC, useState } from 'react';
import { Button } from '@mui/material';

const FilterProfiles: FC = () => {
	const [selectedProfile, setSelectedProfile] = useState<string>('');
	const [selectedEmpresasIds, setSelectedEmpresasIds] = useState<string[]>([]);

	const selectFilterProfile = (id: string) => {
		setSelectedProfile(id);
		const auxSelectedIds = [...selectedEmpresasIds];
		const index = auxSelectedIds.indexOf(id);

		if (index !== -1) {
			auxSelectedIds.splice(index, 1);
		} else {
			auxSelectedIds.push(id);
		}
		setSelectedEmpresasIds([...auxSelectedIds]);
	};

	return (
		<div className='box flex space-between'>
			{selectedProfile ? (
				<Button
					style={{ minWidth: 'fit-content' }}
					variant='outlined'
					color='secondary'
					disableRipple
					disableElevation
					onClick={() => selectFilterProfile('1')}
				>
					<span className='flex center bold text nowrap m-0'>Perfil 1</span>
				</Button>
			) : (
				<Button
					style={{ minWidth: 'fit-content' }}
					variant='contained'
					color='secondary'
					disableRipple
					disableElevation
					onClick={() => selectFilterProfile('1')}
				>
					<span className='flex center bold text nowrap m-0'>Perfil 1</span>
				</Button>
			)}
			<Button
				style={{ minWidth: 'fit-content' }}
				variant='contained'
				color='secondary'
				disableRipple
				disableElevation
			>
				<span className='flex center bold text nowrap m-0'>Perfil 2</span>
			</Button>
			<Button
				style={{ minWidth: 'fit-content' }}
				variant='contained'
				color='secondary'
				disableRipple
				disableElevation
			>
				<span className='flex center bold text nowrap m-0'>Perfil 3</span>
			</Button>
			<Button
				style={{ minWidth: 'fit-content' }}
				variant='contained'
				color='secondary'
				disableRipple
				disableElevation
			>
				<span className='flex center bold text nowrap m-0'>Perfil 4</span>
			</Button>
		</div>
	);
};

export default FilterProfiles;
