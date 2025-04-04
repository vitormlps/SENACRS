import { FC, createContext, useContext, useState } from 'react';
import { SocioServices } from '../services/socios';
import { ISocio, ISocioContext, IHookProvider } from '../types';

const SociosContext = createContext<ISocioContext>({} as ISocioContext);

export const SociosProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const socioServices = new SocioServices();

	const [entities, setSocios] = useState<ISocio[]>([]);
	const [loading, setLoading] = useState<boolean>(false);
	const [searchEntity, setSearchEntity] = useState<string>('');
	const [entitiesPerRow, setEntitiesPerRow] = useState<string>('8');
	const [paginate, setPaginate] = useState<number>(0);

	const createNewEntity = async (_socio: ISocio) => {
		try {
			const socio = await socioServices.createEntity(_socio);

			fetchEntities();
			return socio;
		} catch (_err) {
			throw _err;
		}
	};

	const editEntity = async (_id: string, _socio: ISocio) => {
		try {
			const socio = await socioServices.updateEntity(_id, _socio);

			fetchEntities();
			return socio;
		} catch (_err) {
			throw _err;
		}
	};

	const deleteEntity = async (_id: string) => {
		try {
			const socio = await socioServices.deleteEntity(_id);

			fetchEntities();
			return socio;
		} catch (_err) {
			throw _err;
		}
	};

	const fetchEntities = async (_query?: string) => {
		setLoading(true);
		try {
			const socios: ISocio[] = await socioServices.getEntities(_query);
			setSocios([...socios]);
		} catch (_err) {
			console.log(_err);
		} finally {
			setLoading(false);
		}
	};

	const fetchEntity = async (_id: string) => {
		const socio: ISocio = await socioServices.getEntity(_id);
		return socio;
	};

	return (
		<SociosContext.Provider
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
		</SociosContext.Provider>
	);
};

export function useSocios() {
	const context = useContext(SociosContext);

	if (!context) {
		throw new Error('useSocios must be used within an SociosProvider');
	}

	return context;
}
