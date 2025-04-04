import { FC, useState } from 'react';
import { Button, IconButton, TextField } from '@mui/material';

import { ExpandLess as ExpandLessIcon, ExpandMore as ExpandMoreIcon } from '@mui/icons-material';

import { IFilter, IFilterParams } from '../../types';
import { useSideEntities } from '../../hooks/sideEntities';
import { SideEntityFilter, EstadosMunicipiosFilter, Divider } from '..';
import { blankFilterParams } from '../../utils/consts';

const MainFilters: FC<IFilter> = (props: IFilter) => {
	const sideEntitiesHook = useSideEntities();

	const [selectedEstadosIds, setSelectedEstadosIds] = useState<string[]>([]);
	const [selectedMunicipiosIds, setSelectedMunicipiosIds] = useState<string[]>([]);
	const [selectedCnaesIds, setSelectedCnaesIds] = useState<string[]>([]);
	const [selectedPortesIds, setSelectedPortesIds] = useState<string[]>([]);
	const [selectedSituCadsIds, setSelectedSituCadsIds] = useState<string[]>([]);
	const [selectedNatJursIds, setSelectedNatJursIds] = useState<string[]>([]);
	const [showCapitalSocial, setShowCapitalSocial] = useState<boolean>(false);
	const [minCapitalSocial, setMinCapitalSocial] = useState<number>(
		blankFilterParams.minCapitalSocial
	);
	const [maxCapitalSocial, setMaxCapitalSocial] = useState<number>(
		blankFilterParams.maxCapitalSocial
	);

	const cleanFilter = () => {
		setSelectedEstadosIds([]);
		setSelectedMunicipiosIds([]);
		setSelectedCnaesIds([]);
		setSelectedPortesIds([]);
		setSelectedSituCadsIds([]);
		setSelectedNatJursIds([]);
	};

	const filterEmpresas = () => {
		const filterParams: IFilterParams = {
			estados: selectedEstadosIds,
			municipios: selectedMunicipiosIds,
			cnaes: selectedCnaesIds,
			portesEmpresa: selectedPortesIds,
			situCads: selectedSituCadsIds,
			natJurs: selectedNatJursIds,
			minCapitalSocial: minCapitalSocial,
			maxCapitalSocial: maxCapitalSocial,
		};

		props.onFilter(filterParams);
	};

	return (
		<div
			className='flex column of-hidden'
			style={{
				height: '100%',
				marginTop: '5%',
			}}
		>
			<div className='flex space-between'>
				<Button
					style={{ width: '45%' }}
					size='small'
					variant='outlined'
					color='inherit'
					disableRipple
					onClick={() => cleanFilter()}
				>
					<span className='flex center text-9 bold m-0'>Limpar filtros</span>
				</Button>
				<Button
					style={{ width: '45%' }}
					size='small'
					variant='contained'
					color='secondary'
					disableRipple
					disableElevation
					onClick={filterEmpresas}
				>
					<span className='flex center text-9 bold white m-0'>Filtrar</span>
				</Button>
			</div>

			<div className='outer-scroll' style={{ marginTop: '5%' }}>
				<EstadosMunicipiosFilter
					sideEntities={sideEntitiesHook.estadosMunicipios}
					fetchSideEntities={sideEntitiesHook.fetchEstadosMunicipios}
					selectedEstadosIds={selectedEstadosIds}
					setSelectedEstadosIds={setSelectedEstadosIds}
					showEstadoSearchBar={false}
					selectedMunicipiosIds={selectedMunicipiosIds}
					setSelectedMunicipiosIds={setSelectedMunicipiosIds}
					showMunicipioSearchBar={true}
				/>
				<SideEntityFilter
					sideEntityName='CNAEs'
					sideEntities={sideEntitiesHook.cnaes}
					fetchSideEntities={sideEntitiesHook.fetchCnaes}
					selectedFiltersIds={selectedCnaesIds}
					setSelectedFiltersIds={setSelectedCnaesIds}
					showSearchBar={true}
					loading={sideEntitiesHook.loadingCnaes}
				/>
				<div className='flex space-between' style={{ marginTop: '5%' }}>
					<div className='half'>
						<SideEntityFilter
							sideEntityName='Portes'
							sideEntities={sideEntitiesHook.porteEmpresas}
							fetchSideEntities={sideEntitiesHook.fetchPorteEmpresas}
							selectedFiltersIds={selectedPortesIds}
							setSelectedFiltersIds={setSelectedPortesIds}
							showSearchBar={false}
							loading={sideEntitiesHook.loadingPortes}
						/>
					</div>

					<Divider vertical />

					<div className='half'>
						<SideEntityFilter
							sideEntityName='Situações Cadastrais'
							sideEntities={sideEntitiesHook.situCads}
							fetchSideEntities={sideEntitiesHook.fetchSituCads}
							selectedFiltersIds={selectedSituCadsIds}
							setSelectedFiltersIds={setSelectedSituCadsIds}
							showSearchBar={false}
							loading={sideEntitiesHook.loadingSituCads}
						/>
					</div>
				</div>
				<SideEntityFilter
					sideEntityName='Naturezas Jurídicas'
					sideEntities={sideEntitiesHook.natJurs}
					fetchSideEntities={sideEntitiesHook.fetchNatJurs}
					selectedFiltersIds={selectedNatJursIds}
					setSelectedFiltersIds={setSelectedNatJursIds}
					showSearchBar={true}
					loading={sideEntitiesHook.loadingNatJurs}
				/>

				<div
					style={{
						marginTop: '5%',
					}}
				>
					<div className='flex space-between'>
						<h3 className='flex center bold text primary m-0'>Capital Social</h3>

						<IconButton
							size='small'
							onClick={() => {
								setShowCapitalSocial(!showCapitalSocial);
							}}
						>
							{showCapitalSocial ? (
								<ExpandLessIcon fontSize='small' color='action' />
							) : (
								<ExpandMoreIcon fontSize='small' color='action' />
							)}
						</IconButton>
					</div>
					<hr
						style={{
							marginTop: '0',
							marginBottom: '2%',
							backgroundColor: '#d2d2d2',
							border: 'none',
							height: '1px',
						}}
					/>
					{showCapitalSocial && (
						<div className='container flex space-between'>
							<TextField
								style={{ width: '47%' }}
								variant='outlined'
								fullWidth
								size='small'
								label=''
								helperText={null}
								placeholder='Valor mínimo'
								value={minCapitalSocial}
								onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
									setMinCapitalSocial(parseFloat(event.target.value) || 0);
								}}
								slotProps={{
									htmlInput: {
										style: { fontSize: '11pt', textAlign: 'right' },
									},
									input: {
										startAdornment: (
											<span
												className='text-11 nowrap'
												style={{ marginRight: '3%' }}
											>
												De R$
											</span>
										),
										endAdornment: (
											<span
												className='text-11 nowrap'
												style={{ marginLeft: '1%' }}
											>
												,00
											</span>
										),
									},
								}}
							/>
							<TextField
								style={{ width: '47%' }}
								variant='outlined'
								fullWidth
								size='small'
								label=''
								helperText={null}
								placeholder='Valor máximo'
								value={maxCapitalSocial}
								onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
									setMaxCapitalSocial(parseFloat(event.target.value) || 0);
								}}
								slotProps={{
									htmlInput: {
										style: { fontSize: '11pt', textAlign: 'right' },
									},
									input: {
										startAdornment: (
											<span
												className='text-11 nowrap'
												style={{ marginRight: '3%' }}
											>
												De R$
											</span>
										),
										endAdornment: (
											<span
												className='text-11 nowrap'
												style={{ marginLeft: '1%' }}
											>
												,00
											</span>
										),
									},
								}}
							/>
						</div>
					)}
				</div>
			</div>
		</div>
	);
};

export default MainFilters;
