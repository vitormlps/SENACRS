import { FC, createContext, useContext, useState } from 'react';
import { toast } from 'react-toastify';

import { SimplesNacionalServices } from '../services/simplesNacional';
import { ISimplesNacional, ISimplesNacionalContext, IHookProvider } from '../types';

const SimplesNacionalContext = createContext<ISimplesNacionalContext>(
	{} as ISimplesNacionalContext
);

export const SimplesNacionalProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const simplesNacionalServices = new SimplesNacionalServices();

	const [entities, setSimplesNacional] = useState<ISimplesNacional[]>([]);
	const [loading, setLoading] = useState<boolean>(false);
	const [searchEntity, setSearchEntity] = useState<string>('');
	const [entitiesPerRow, setEntitiesPerRow] = useState<string>('8');
	const [paginate, setPaginate] = useState<number>(0);

	const createNewEntity = async (_simplesNacional: ISimplesNacional) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const editEntity = async (_id: string, _simplesNacional: ISimplesNacional) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const deleteEntity = async (_id: string) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const fetchEntities = async (_query?: string) => {
		let simplesNacional: ISimplesNacional[] = [];
		setLoading(true);
		try {
			simplesNacional = await simplesNacionalServices.getEntities(_query);
			toast.success('Simples Nacional carregado!');
		} catch (_err) {
			toast.error('Nenhum Simples Nacional foi encontrado.');
		}
		setSimplesNacional([...simplesNacional]);
		setLoading(false);
	};

	const fetchEntity = async (_id: string) => {
		const simplesNacional: ISimplesNacional = await simplesNacionalServices.getEntity(_id);
		return simplesNacional;
	};

	return (
		<SimplesNacionalContext.Provider
			value={{
				entities,
				loading,
				fetchEntities,
				fetchEntity,
				createNewEntity,
				editEntity,
				deleteEntity,

				searchEntity,
				setSearchEntity,
				entitiesPerRow,
				setEntitiesPerRow,
				paginate,
				setPaginate,
			}}
		>
			{_params.children}
		</SimplesNacionalContext.Provider>
	);
};

export function useSimplesNacional() {
	const context = useContext(SimplesNacionalContext);

	if (!context) {
		throw new Error('useSimplesNacional must be used within an SimplesNacionalProvider');
	}

	return context;
}
