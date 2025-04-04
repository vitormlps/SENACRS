import { IEntity, IEntityContext } from './entities';

interface IUsers extends IEntity {
    first_name: string;
    last_name: string;
    email: string;
    token?: string;
}

interface IUsersContext extends IEntityContext<IUsers> {
}

export type { IUsers, IUsersContext };
