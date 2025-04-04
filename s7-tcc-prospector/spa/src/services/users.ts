import { EntityServices } from './entities';
import { IUsers } from '../../../types';

export class UsersServices extends EntityServices<IUsers> {
    constructor () {
        const _baseUrl: string = '/users';
        super('Usuário', _baseUrl)
    }
}
