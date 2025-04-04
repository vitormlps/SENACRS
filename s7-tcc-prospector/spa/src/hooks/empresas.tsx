import { FC, createContext, useContext, useState, useReducer } from 'react';
import { toast } from 'react-toastify';

import { EmpresaServices } from '../services/empresas';
import { IEmpresa, IEmpresaContext, IHookProvider, IFilterParams } from '../types';
import { reducer } from '../utils/reducer';

const EmpresasContext = createContext<IEmpresaContext>({} as IEmpresaContext);
const DispatchContext = createContext<any>({} as any);

export const EmpresasProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const empresaServices = new EmpresaServices();

	const [selectedEmpresaIndex, setSelectedEmpresaIndex] = useState<number>(0);
	const [entities, setEmpresas] = useState<IEmpresa[]>([]);
	const [loading, setLoading] = useState<boolean>(false);
	const [exportingFile, setExportingFile] = useState<boolean>(false);
	const [searchEntity, setSearchEntity] = useState<string>('');
	const [entitiesPerRow, setEntitiesPerRow] = useState<string>('8');
	const [paginate, setPaginate] = useState<number>(0);

	const [empresas, dispatch] = useReducer(reducer, entities);

	const createNewEntity = async (_empresa: IEmpresa) => {
		try {
			const empresa = await empresaServices.createEntity(_empresa);

			fetchEntities();
			return empresa;
		} catch (_err) {
			throw _err;
		}
	};

	const editEntity = async (_id: string, _empresa: IEmpresa) => {
		try {
			const empresa = await empresaServices.updateEntity(_id, _empresa);

			const temp_empresas = [...entities];
			for (let index = 0; index < temp_empresas.length; index++) {
				if (temp_empresas[index].id === _id) {
					temp_empresas[index] = empresa;
				}
			}
			setEmpresas([...temp_empresas]);

			return empresa;
		} catch (_err) {
			throw _err;
		}
	};

	const deleteEntity = async (_id: string) => {
		try {
			const empresa = await empresaServices.deleteEntity(_id);

			fetchEntities();
			return empresa;
		} catch (_err) {
			throw _err;
		}
	};

	const fetchEntities = async (_query?: string) => {
		let empresas: IEmpresa[] = [];
		setLoading(true);
		try {
			empresas = await empresaServices.getEntities(_query);
			toast.success('Encontramos empresas!');
		} catch (_err) {
			console.log(_err);
			toast.error('Nenhuma empresa foi encontrada.');
		} finally {
			setEmpresas([...empresas]);
			setLoading(false);
		}
	};

	const fetchEntity = async (_id: string) => {
		const empresa: IEmpresa = await empresaServices.getEntity(_id);
		return empresa;
	};

	const clearEmpresas = () => {
		setEmpresas([]);
	};

	const generateFile = async (_payload: string[]) => {
		const date = new Date(Date.now());
		setExportingFile(true);
		const file: any = await empresaServices.generateFile(_payload);

		if (file) {
			const link = document.createElement('a');
			const blob = new Blob([file]);
			link.href = window.URL.createObjectURL(blob);

			link.setAttribute(
				'download',
				'empresas_' +
					`${date.getDate()}-${date.getMonth()}-${date.getFullYear()}_${date.getHours()}-${date.getMinutes()}-${date.getSeconds()}` +
					'.csv'
			);

			document.body.appendChild(link);
			link.click();
			link.parentNode?.removeChild(link);
		}
		setExportingFile(false);
	};

	const createQuery = (params: IFilterParams) => {
		let query: string = '';

		if (params.estados && params.estados.length > 0) {
			for (let index = 0; index < params.estados.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `uf=${params.estados[index]}`;
			}
		}

		if (params.municipios && params.municipios.length > 0) {
			for (let index = 0; index < params.municipios.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `municipio=${params.municipios[index]}`;
			}
		}

		if (params.cnaes && params.cnaes.length > 0) {
			for (let index = 0; index < params.cnaes.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `cnae=${params.cnaes[index]}`;
			}
		}

		if (params.situCads && params.situCads.length > 0) {
			for (let index = 0; index < params.situCads.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `situacao_cadastral=${params.situCads[index]}`;
			}
		}

		if (params.natJurs && params.natJurs.length > 0) {
			for (let index = 0; index < params.natJurs.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `natureza_juridica=${params.natJurs[index]}`;
			}
		}

		if (params.portesEmpresa && params.portesEmpresa.length > 0) {
			for (let index = 0; index < params.portesEmpresa.length; index++) {
				if (query.length > 0) {
					query += '&';
				}
				query += `porte_empresa=${params.portesEmpresa[index]}`;
			}
		}

		if (query.length > 0) {
			query += '&';
		}
		query += `min_capital_social=${params.minCapitalSocial}`;
		query += `&max_capital_social=${params.maxCapitalSocial}`;

		return query;
	};

	return (
		<EmpresasContext.Provider
			value={{
				selectedEmpresaIndex,
				setSelectedEmpresaIndex,
				empresas,
				entities,
				loading,
				fetchEntities,
				fetchEntity,
				createNewEntity,
				editEntity,
				deleteEntity,
				clearEmpresas,
				createQuery,
				generateFile,
				exportingFile,

				searchEntity,
				setSearchEntity,
				entitiesPerRow,
				setEntitiesPerRow,
				paginate,
				setPaginate,
			}}
		>
			<DispatchContext.Provider value={dispatch}>{_params.children}</DispatchContext.Provider>
		</EmpresasContext.Provider>
	);
};

export function useEmpresas() {
	const context = useContext(EmpresasContext);

	if (!context) {
		throw new Error('useEmpresas must be used within an EmpresasProvider');
	}

	return context;
}

export function useDispatch() {
	const context = useContext(DispatchContext);

	if (!context) {
		throw new Error('useDispatch must be used within an DispatchContext.Provider');
	}

	return context;
}
