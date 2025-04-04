import { FC, createContext, useContext, useState } from 'react';
import { UsersServices } from '../services/users';
import { IUsers, IUsersContext, IHookProvider } from '../types';

const UsersContext = createContext<IUsersContext>({} as IUsersContext);

export const UsersProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const userServices = new UsersServices();

	const [entities, setUsers] = useState<IUsers[]>([]);
	const [loading, setLoading] = useState<boolean>(false);
	const [searchEntity, setSearchEntity] = useState<string>('');
	const [entitiesPerRow, setEntitiesPerRow] = useState<string>('8');
	const [paginate, setPaginate] = useState<number>(0);

	const createNewEntity = async (_user: IUsers) => {
		try {
			const user = await userServices.createEntity(_user);

			fetchEntities();
			return user;
		} catch (_err) {
			throw _err;
		}
	};

	const editEntity = async (_id: string, _user: IUsers) => {
		try {
			const user = await userServices.updateEntity(_id, _user);

			fetchEntities();
			return user;
		} catch (_err) {
			throw _err;
		}
	};

	const deleteEntity = async (_id: string) => {
		try {
			const user = await userServices.deleteEntity(_id);

			fetchEntities();
			return user;
		} catch (_err) {
			throw _err;
		}
	};

	const fetchEntities = async (_query?: string) => {
		setLoading(true);
		try {
			const users: IUsers[] = await userServices.getEntities(_query);
			setUsers([...users]);
		} catch (_err) {
			console.log(_err);
		} finally {
			setLoading(false);
		}
	};

	const fetchEntity = async (_id: string) => {
		const user: IUsers = await userServices.getEntity(_id);
		return user;
	};

	return (
		<UsersContext.Provider
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
		</UsersContext.Provider>
	);
};

export function useUsers() {
	const context = useContext(UsersContext);

	if (!context) {
		throw new Error('useUsers must be used within an UsersProvider');
	}

	return context;
}
