import { FC, useEffect, useState } from 'react';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { useEmpresas } from '../../hooks/empresas';
import AppHeader from '../../components/appHeader';
import {
	MainFilters,
	EmpresasListItem,
	LoadingDisplay,
	ExportButton,
	Divider,
} from '../../components';
import { IEmpresa, IFilterParams } from '../../types';

const SearchPage: FC = () => {
	const empresasHook = useEmpresas();

	const [filteredEmpresas, setFilteredEmpresas] = useState<IEmpresa[]>([]);
	const [selectedEmpresasIds, setSelectedEmpresasIds] = useState<string[]>([]);

	const filterEmpresas = async (params: IFilterParams) => {
		const query: string = empresasHook.createQuery(params);
		empresasHook.fetchEntities(query);
	};

	useEffect(() => {
		setFilteredEmpresas(empresasHook.entities);
	}, [empresasHook.entities]);

	return (
		<div className='flex space-between'>
			<div
				className='flex column space-between p-1'
				style={{
					width: '25%',
					height: '95.8vh',
				}}
			>
				<AppHeader />

				<MainFilters onFilter={filterEmpresas} />
			</div>

			<Divider vertical />

			<div
				className='flex column space-between p-1'
				style={{
					width: '70%',
				}}
			>
				<div className='flex space-between'>
					<div className='flex center'>
						<span className='bold secondary'>{filteredEmpresas.length}</span>
						{filteredEmpresas.length === 1 ? (
							<span className='nowrap m-2'> empresa foi encontrada</span>
						) : (
							<span className='nowrap m-2'> empresas foram encontradas</span>
						)}
					</div>

					<ExportButton
						service={empresasHook.generateFile}
						selectedIds={selectedEmpresasIds}
						exportingFile={empresasHook.exportingFile}
					/>
				</div>

				{empresasHook.loading ? (
					<LoadingDisplay classNames='container app-page flex column center' />
				) : filteredEmpresas.length === 0 ? (
					<div
						className='flex'
						style={{
							height: '100%',
						}}
					>
						<span className='container flex center bold text primary m-0'>
							No menu ao lado esquerdo, selecione os filtros e clique em FILTRAR para
							visualizar a pesquisa desejada
						</span>
					</div>
				) : (
					<EmpresasListItem items={filteredEmpresas} onSelect={setSelectedEmpresasIds} />
				)}
			</div>
			<ToastContainer
				position='top-right'
				autoClose={1500}
				hideProgressBar={false}
				newestOnTop={false}
				closeOnClick
				rtl={false}
				pauseOnFocusLoss
				draggable={false}
				pauseOnHover
				theme='colored'
			/>
		</div>
	);
};

export default SearchPage;
