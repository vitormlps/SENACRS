import { EntityServices } from './entities';
import { ISimplesNacional } from '../../../types';

export class SimplesNacionalServices extends EntityServices<ISimplesNacional> {
    constructor () {
        const _baseUrl: string = '/simples-nacional';
        super('SimplesNacional', _baseUrl)
    }
}
