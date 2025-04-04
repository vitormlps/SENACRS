import { IEntity, IEntityContext } from './entities';

interface ISocio extends IEntity {
    cnpj: string;
    razaoSocial: string;
    nomeFantasia: string;
}

interface ISocioContext extends IEntityContext<ISocio> {

}

export function isSocio(_data: any): _data is ISocio {
    return 'cnpj' in _data
}

export type { ISocio, ISocioContext };
