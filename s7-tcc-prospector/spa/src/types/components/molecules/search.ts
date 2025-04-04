import { IEmpresa } from '../../hooks/empresas';

interface IListItem {
    index: number;
    item: any;
    onSelect: (itemId: string) => void;
    selectedItemsIds: string[];
    }

interface IListItems {
    items: any[];
    onSelect: any;
    }

interface IEmpresaItem {
    index: number;
    empresa: IEmpresa;
    onSelect: (empresaId: string) => void;
    selectedEmpresasIds: string[];
}

interface IFilterParams {
    estados?: string[];
    municipios?: string[];
    cnaes?: string[];
    situCads?: string[];
    natJurs?: string[];
    portesEmpresa?: string[];
    minCapitalSocial: number;
    maxCapitalSocial: number;
};

interface IFilter {
    defaultParams?: IFilterParams;
    onFilter: (params: IFilterParams) => void;
}

interface ISideEntityFilter {
    sideEntityName: string;
    sideEntities: any;
    fetchSideEntities: any;
    defaultParams?: IFilterParams;
    onFilter?: (params: IFilterParams) => void;
    selectedFiltersIds: any[]
    setSelectedFiltersIds: (ids: any[]) => void;
    showSearchBar: boolean;
    loading: boolean;
}

interface IEstadoMunicipioFilter {
    sideEntities: any;
    fetchSideEntities: any;
    defaultParams?: IFilterParams;
    onFilter?: (params: IFilterParams) => void;
    selectedEstadosIds: any[]
    setSelectedEstadosIds: (ids: any[]) => void;
    showEstadoSearchBar: boolean;
    selectedMunicipiosIds: any[]
    setSelectedMunicipiosIds: (ids: any[]) => void;
    showMunicipioSearchBar: boolean;
}

interface IConfirmModal {
    open: boolean;
    onClose: () => void;
    onConfirm: (withImages: boolean) => void;
}

export type { IListItems, IListItem, IEmpresaItem, IFilterParams, IFilter, ISideEntityFilter, IEstadoMunicipioFilter, IConfirmModal };
