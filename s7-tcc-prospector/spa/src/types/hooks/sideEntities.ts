import { IEntity } from './entities';

interface ISideEntity extends IEntity {
    id: string;
    descricao: string;
}

interface IEstadoMunicipio {
    estado: ISideEntity[];
}

interface ISideEntityContext {
    cnaes: ISideEntity[];
    natJurs: ISideEntity[];
    situCads: ISideEntity[];
    motivos: ISideEntity[];
    qualificacoes: ISideEntity[];
    porteEmpresas: ISideEntity[];
    matrizFiliais: ISideEntity[];
    faixasEtarias: ISideEntity[];
    estadosMunicipios: IEstadoMunicipio;
    paises: ISideEntity[];
    loadingCnaes: boolean;
    loadingNatJurs: boolean;
    loadingSituCads: boolean;
    loadingMotivos: boolean;
    loadingQualif: boolean;
    loadingPortes: boolean;
    loadingMatrizFiliais: boolean;
    loadingFaixasEtarias: boolean;
    loadingEstadosMunicipios: boolean;
    loadingPaises: boolean;

    fetchCnaes: () => void;
    fetchNatJurs: () => void;
    fetchSituCads: () => void;
    fetchMotivos: () => void;
    fetchQualificacoes: () => void;
    fetchPorteEmpresas: () => void;
    fetchMatrizFiliais: () => void;
    fetchFaixasEtarias: () => void;
    fetchEstadosMunicipios: () => void;
    fetchPaises: () => void;
}

export type { ISideEntity, IEstadoMunicipio, ISideEntityContext };
