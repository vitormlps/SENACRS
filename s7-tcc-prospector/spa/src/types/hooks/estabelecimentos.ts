import { IEntity, IEntityContext } from './entities';

interface IEstabelecimento extends IEntity {
    cnpj: string;
    razaoSocial: string;
    nomeFantasia: string;
}

interface IEstabelecimentoContext extends IEntityContext<IEstabelecimento> {

}

export function isEstabelecimento(_data: any): _data is IEstabelecimento {
    return 'cnpj' in _data
}

export type { IEstabelecimento, IEstabelecimentoContext };
