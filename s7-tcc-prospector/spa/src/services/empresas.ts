import { AxiosResponse } from 'axios';

import api from '.';
import { EntityServices } from './entities';
import { IEmpresa } from '../../../types';

export class EmpresaServices extends EntityServices<IEmpresa> {
    constructor () {
        const _baseUrl: string = '/empresas';
        super('Empresa', _baseUrl)
    }

    async generateFile(_payload: string[]): Promise<any> {
        const response: AxiosResponse = await api.post(`${this.baseUrl}/export`, _payload);

        if (response.data && response?.request?.status === 200) {
            return response.data

        } else if (response.data && response?.request?.status === 400) {
            throw new Error(response.data as string);
        }
        return undefined;
    }
}
