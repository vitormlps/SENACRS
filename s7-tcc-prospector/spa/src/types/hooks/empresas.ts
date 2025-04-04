import { IEntity, IEntityContext } from './entities';
import { IFilterParams } from '../components/molecules/search';

interface IEmpresa extends IEntity {
    cnpj: string;
    razaoSocial: string;
    nomeFantasia: string;
}

interface IEmpresaCsvGenerate {
    file_name?: string;
    ids?: string[];
}

interface IEmpresaContext extends IEntityContext<IEmpresa> {
    exportingFile: boolean;
    selectedEmpresaIndex: number;
    setSelectedEmpresaIndex: (_value: number) => void;
    empresas: IEmpresa[];
    clearEmpresas: () => void;
    createQuery: (params: IFilterParams) => string;
    generateFile: (_payload: string[]) => Promise<any>;
}

export function isEmpresa(_data: any): _data is IEmpresa {
    return 'cnpj' in _data
}

export type { IEmpresa, IEmpresaContext, IEmpresaCsvGenerate };
