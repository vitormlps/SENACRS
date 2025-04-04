import { IFilterParams } from '../types';


export const formatCnpj = (cnpj: string) => {
    return `${cnpj.substring(0, 2)
    }.${cnpj.substring(2,5)
    }.${cnpj.substring(5)}`;
};

export const blankFilterParams: IFilterParams = {
    cnaes: [],
    situCads: [],
    natJurs: [],
    minCapitalSocial: 0,
    maxCapitalSocial: 0,
};
