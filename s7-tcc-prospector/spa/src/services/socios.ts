import { EntityServices } from './entities';
import { ISocio } from '../../../types';

export class SocioServices extends EntityServices<ISocio> {
    constructor () {
        const _baseUrl: string = '/socios';
        super('Socio', _baseUrl)
    }
}
