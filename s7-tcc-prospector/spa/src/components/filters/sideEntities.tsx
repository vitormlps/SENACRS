import { FC, useEffect, useState } from 'react';
import { IconButton, TextField } from '@mui/material';
import {
	Search as SearchIcon,
	ExpandLess as ExpandLessIcon,
	ExpandMore as ExpandMoreIcon,
} from '@mui/icons-material';

import { Divider, ListItem, LoadingDisplay, Title } from '..';
import { ISideEntityFilter, ISideEntity } from '../../types';

const SideEntityFilter: FC<ISideEntityFilter> = (params: ISideEntityFilter) => {
	const [showFilter, setShowFilter] = useState<boolean>(false);
	const [searchFilter, setSearchFilter] = useState<string>('');
	const [filteredSideEntities, setFilteredSideEntities] = useState<ISideEntity[]>([]);

	const selectSideEntity = (id: string, arrayIds: string[]) => {
		let auxSelectedIds = [...arrayIds];
		const index = auxSelectedIds.indexOf(id);

		if (index !== -1) {
			auxSelectedIds = auxSelectedIds.filter((itemId) => itemId !== id);
		} else {
			auxSelectedIds.push(id);
		}

		return auxSelectedIds;
	};

	const getSideEntityFilter = (filter?: string[]) => {
		if (filter) {
			setFilteredSideEntities([]);
		} else {
			if (params.sideEntities.length === 0) {
				params.fetchSideEntities();
			}
		}
	};

	const selectFilter = (id: string) => {
		const selectedIds = selectSideEntity(id, params.selectedFiltersIds);
		params.setSelectedFiltersIds([...selectedIds]);
	};

	useEffect(() => {
		setFilteredSideEntities([...params.sideEntities]);
	}, [params.sideEntities]);

	useEffect(() => {
		let auxFilteredArray: ISideEntity[] = [];

		if (searchFilter !== '') {
			const lowerSearchFilter = searchFilter.toLowerCase();

			auxFilteredArray = filteredSideEntities.filter((item) => {
				return (
					item.id.includes(lowerSearchFilter) ||
					item.descricao.toLowerCase().includes(lowerSearchFilter)
				);
			});
		} else {
			auxFilteredArray = [...params.sideEntities];
		}
		setFilteredSideEntities([...auxFilteredArray]);
	}, [searchFilter]);

	return (
		<div style={{ marginTop: '5%', marginRight: '1%' }}>
			<div className='flex space-between'>
				<Title title={params.sideEntityName} />
				<IconButton
					size='small'
					onClick={() => {
						if (!showFilter) getSideEntityFilter();
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
					{params.loading ? (
						<LoadingDisplay classNames='container flex column center my-5 text-8' />
					) : (
						<>
							{filteredSideEntities.length !== 0 ? (
								<>
									{params.showSearchBar && (
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
										{[...filteredSideEntities].map((item, index) => {
											return (
												<ListItem
													key={index.toString()}
													index={index}
													item={item}
													onSelect={selectFilter}
													selectedItemsIds={params.selectedFiltersIds}
												/>
											);
										})}
									</div>
								</>
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

export default SideEntityFilter;
