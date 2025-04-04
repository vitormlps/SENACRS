import { FC, useEffect, useState } from 'react';
import { IconButton, TextField } from '@mui/material';

import { Divider, Title } from '..';
import { useSideEntities } from '../../hooks/sideEntities';
import { ufToName } from '../../utils/ufMap';

import {
	Search as SearchIcon,
	ExpandLess as ExpandLessIcon,
	ExpandMore as ExpandMoreIcon,
} from '@mui/icons-material';

import { IEstadoMunicipioFilter, ISideEntity, IEstadoMunicipio } from '../../types';
import { ListItem, LoadingDisplay } from '..';

const EstadosMunicipiosFilter: FC<IEstadoMunicipioFilter> = (params: IEstadoMunicipioFilter) => {
	const { loadingEstadosMunicipios } = useSideEntities();

	const [showFilter, setShowFilter] = useState<boolean>(false);
	const [searchFilter, setSearchFilter] = useState<string>('');
	const [estadosMunicipios, setEstadosMunicipios] = useState<[string, [string, string][]][]>([]);
	const [filteredEstados, setFilteredEstados] = useState<string[]>([]);
	const [filteredMunicipios, setFilteredMunicipios] = useState<ISideEntity[]>([]);

	const getEstadosMunicipiosFilter = (filter?: string[]) => {
		if (filter) {
			setEstadosMunicipios([]);
			setFilteredEstados([]);
			setFilteredMunicipios([]);
		} else {
			if (Object.keys(params.sideEntities).length === 0) {
				params.fetchSideEntities();
			}
		}
	};

	const searchInput = (entityArray: any[]) => {
		let auxFilteredArray: ISideEntity[] = [];

		if (searchFilter !== '') {
			const lowerSearchFilter = searchFilter.toLowerCase();

			auxFilteredArray = entityArray.filter((item) => {
				item.id.includes(lowerSearchFilter) ||
					item.descricao.toLowerCase().includes(lowerSearchFilter);
			});
		} else {
			auxFilteredArray = params.sideEntities;
		}
		setFilteredMunicipios(auxFilteredArray);
	};

	const selectSideEntityIds = (id: string, arrayIds: string[]) => {
		let auxSelectedIds = [...arrayIds];
		const index = auxSelectedIds.indexOf(id);

		if (index !== -1) {
			auxSelectedIds = auxSelectedIds.filter((itemId) => itemId !== id);
		} else {
			auxSelectedIds.push(id);
		}

		return auxSelectedIds;
	};

	const selectEstadosFilter = (id: string) => {
		const selectedIds = selectSideEntityIds(id, params.selectedEstadosIds);
		params.setSelectedEstadosIds([...selectedIds]);
	};

	const selectMunicipiosFilter = (id: string) => {
		const selectedIds = selectSideEntityIds(id, params.selectedMunicipiosIds);
		params.setSelectedMunicipiosIds([...selectedIds]);
	};

	const mapEstadosMunicipios = (estadosIds: any[]) => {
		for (let index = 0; index < estadosIds.length; index++) {
			const municipios = params.sideEntities[estadosIds[index]];
			if (municipios) setFilteredMunicipios([...municipios]);
		}
	};

	const organizeEstadosMunicipios = (inputEstadosMunicipios: IEstadoMunicipio) => {
		const tempUFsMunicipios = Object.entries(inputEstadosMunicipios);
		setEstadosMunicipios([...tempUFsMunicipios]);

		const tempUFs = [];
		let tempMunics: any[] = [];

		for (let index = 0; index < tempUFsMunicipios.length; index++) {
			tempUFs.push(tempUFsMunicipios[index][0]);
			tempMunics = tempMunics.concat(tempUFsMunicipios[index][1]);
		}

		setFilteredEstados(tempUFs.sort());
		setFilteredMunicipios([...tempMunics.sort()]);
	};

	useEffect(() => {
		if (params.selectedEstadosIds.length > 0) mapEstadosMunicipios(params.selectedEstadosIds);
	}, [params.selectedEstadosIds.length]);

	useEffect(() => {
		organizeEstadosMunicipios(params.sideEntities);
	}, [params.sideEntities]);

	return (
		<div style={{ marginTop: '5%', marginRight: '1%' }}>
			<div className='flex space-between'>
				<Title title='Estados e Municipios' />
				<IconButton
					size='small'
					onClick={() => {
						if (!showFilter) getEstadosMunicipiosFilter();
						setShowFilter(!showFilter);
					}}
				>
					{showFilter ? (
						<ExpandLessIcon fontSize='small' color='action' />
					) : (
						<ExpandMoreIcon fontSize='small' color='action' />
					)}
				</IconButton>
			</div>

			<Divider />

			{showFilter && (
				<>
					{loadingEstadosMunicipios ? (
						<LoadingDisplay classNames='container flex column center my-5 text-8' />
					) : (
						<>
							{estadosMunicipios.length > 0 ? (
								<div className='container flex space-between'>
									<div className='half flex column'>
										{params.showEstadoSearchBar && (
											<TextField
												style={{ marginBottom: '2%' }}
												variant='outlined'
												fullWidth
												size='small'
												label=''
												helperText={null}
												placeholder='Pesquisar'
												value={searchFilter}
												onChange={(
													event: React.ChangeEvent<HTMLInputElement>
												) => {
													setSearchFilter(event.target.value);
												}}
												onKeyUp={(
													event: React.KeyboardEvent<HTMLDivElement>
												) => {
													if (event.key === 'Enter')
														searchInput(filteredEstados);
												}}
												slotProps={{
													input: (
														<SearchIcon
															style={{ marginRight: '2%' }}
															fontSize='small'
															color='secondary'
														/>
													),
												}}
											/>
										)}
										<div className='container h-2'>
											{filteredEstados.map((uf, index) => {
												const tempItem = {
													id: uf,
													descricao: ufToName(uf),
												};
												// PAREI AQUI, IMPLEMENTAR MAPA UF -> NOME ESTADO
												return (
													<ListItem
														key={'estado' + index.toString()}
														index={index}
														item={tempItem}
														onSelect={selectEstadosFilter}
														selectedItemsIds={params.selectedEstadosIds}
													/>
												);
											})}
										</div>
									</div>

									<Divider vertical />

									<div className='half flex column'>
										{params.showMunicipioSearchBar && (
											<TextField
												style={{ marginBottom: '2%' }}
												variant='outlined'
												fullWidth
												size='small'
												label=''
												helperText={null}
												placeholder='Pesquisar'
												value={searchFilter}
												onChange={(
													event: React.ChangeEvent<HTMLInputElement>
												) => {
													setSearchFilter(event.target.value);
												}}
												onKeyUp={(
													event: React.KeyboardEvent<HTMLDivElement>
												) => {
													if (event.key === 'Enter')
														searchInput(filteredMunicipios);
												}}
												slotProps={{
													input: (
														<SearchIcon
															style={{ marginRight: '2%' }}
															fontSize='small'
															color='secondary'
														/>
													),
												}}
											/>
										)}
										<div className='container h-2 scroll'>
											{filteredMunicipios.map((item, index) => {
												return (
													<ListItem
														key={'municipio' + index.toString()}
														index={index}
														item={item}
														onSelect={selectMunicipiosFilter}
														selectedItemsIds={
															params.selectedMunicipiosIds
														}
													/>
												);
											})}
										</div>
									</div>
								</div>
							) : (
								<div className='container my-5'>
									<span>Não foi possível carregar os filtros.</span>
								</div>
							)}
						</>
					)}
				</>
			)}
		</div>
	);
};

export default EstadosMunicipiosFilter;
