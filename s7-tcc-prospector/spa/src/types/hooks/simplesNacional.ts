import { IEntity, IEntityContext } from './entities';

interface ISimplesNacional extends IEntity {
    cnpj: string;
    razaoSocial: string;
    nomeFantasia: string;
}

interface ISimplesNacionalContext extends IEntityContext<ISimplesNacional> {

}

export function isSimplesNacional(_data: any): _data is ISimplesNacional {
    return 'cnpj' in _data
}

export type { ISimplesNacional, ISimplesNacionalContext };
