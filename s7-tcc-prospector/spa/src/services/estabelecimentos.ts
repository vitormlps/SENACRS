import { EntityServices } from './entities';
import { IEstabelecimento } from '../../../types';

export class EstabelecimentoServices extends EntityServices<IEstabelecimento> {
    constructor () {
        const _baseUrl: string = '/estabelecimentos';
        super('Estabelecimento', _baseUrl)
    }
}
