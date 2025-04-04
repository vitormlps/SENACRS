import { EntityServices } from './entities';
import { ISideEntity } from '../types';

export class CnaeServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/cnaes';
        super('CNAE', _baseUrl)
    }
}

export class NatJurServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/naturezas-juridicas';
        super('Natureza jurídica', _baseUrl)
    }
}

export class SituCadServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/situacoes-cadastrais';
        super('Situação cadastral', _baseUrl)
    }
}

export class MotivoServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/motivos';
        super('Motivo', _baseUrl)
    }
}

export class QualificacaoServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/qualificacoes';
        super('Qualificação', _baseUrl)
    }
}

export class PorteServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/portes-empresas';
        super('Porte empresa', _baseUrl)
    }
}

export class MatrizFilialServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/matriz-filiais';
        super('Matriz ou filial', _baseUrl)
    }
}

export class FaixaEtariaServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/faixas-etarias';
        super('Faixa etária', _baseUrl)
    }
}

export class LogradouroServices extends EntityServices<any> {
    constructor () {
        const _baseUrl: string = '/logradouros/estados';
        super('Logradouro', _baseUrl)
    }
}

export class MunicipioServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/municipios';
        super('Municipio', _baseUrl)
    }
}

export class PaisServices extends EntityServices<ISideEntity> {
    constructor () {
        const _baseUrl: string = '/paises';
        super('Pais', _baseUrl)
    }
}
