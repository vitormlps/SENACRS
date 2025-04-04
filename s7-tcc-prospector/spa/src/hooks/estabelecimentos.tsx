import { FC, createContext, useContext, useState } from 'react';
import { toast } from 'react-toastify';

import { EstabelecimentoServices } from '../services/estabelecimentos';
import { IEstabelecimento, IEstabelecimentoContext, IHookProvider } from '../types';

const EstabelecimentosContext = createContext<IEstabelecimentoContext>(
	{} as IEstabelecimentoContext
);

export const EstabelecimentosProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const estabelecimentoServices = new EstabelecimentoServices();

	const [entities, setEstabelecimentos] = useState<IEstabelecimento[]>([]);
	const [loading, setLoading] = useState<boolean>(false);
	const [searchEntity, setSearchEntity] = useState<string>('');
	const [entitiesPerRow, setEntitiesPerRow] = useState<string>('8');
	const [paginate, setPaginate] = useState<number>(0);

	const createNewEntity = async (_estabelecimento: IEstabelecimento) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const editEntity = async (_id: string, _estabelecimento: IEstabelecimento) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const deleteEntity = async (_id: string) => {
		const mock: Promise<any> = new Promise(() => {});
		return mock;
	};

	const fetchEntities = async (_query?: string) => {
		let estabelecimentos: IEstabelecimento[] = [];
		setLoading(true);
		try {
			estabelecimentos = await estabelecimentoServices.getEntities(_query);
			toast.success('Estabelecimentos carregados!');
		} catch (_err) {
			toast.error('Nenhum estabelecimento foi encontrado.');
		}
		setEstabelecimentos([...estabelecimentos]);
		setLoading(false);
	};

	const fetchEntity = async (_id: string) => {
		const estabelecimento: IEstabelecimento = await estabelecimentoServices.getEntity(_id);
		return estabelecimento;
	};

	return (
		<EstabelecimentosContext.Provider
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
		</EstabelecimentosContext.Provider>
	);
};

export function useEstabelecimentos() {
	const context = useContext(EstabelecimentosContext);

	if (!context) {
		throw new Error('useEstabelecimentos must be used within an EstabelecimentosProvider');
	}

	return context;
}
