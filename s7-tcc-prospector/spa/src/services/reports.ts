import { AxiosResponse } from 'axios';

import api from '.';
import { IEmpresaCsvGenerate } from '../types';

export class ReportServices {
    entityForLog: string;
    baseUrl: string;

    constructor() {
        this.entityForLog = 'Relatório';
        this.baseUrl = 'report';
    }

    async generateCsv(_payload: IEmpresaCsvGenerate, _query?: string): Promise<any> {
        const response: AxiosResponse = await api.post(`${this.baseUrl}${_query}`, _payload);
        
        if (response.data && response?.request?.status === 200) {

        let entity: any = response.data
            return entity
        } else if (response.data && response?.request?.status === 400) {
            throw new Error(response.data as string);
        }
        return undefined;
    }
}
