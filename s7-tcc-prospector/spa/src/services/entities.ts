import { AxiosResponse } from 'axios';

import api from '.';
import { IEntity } from '../types';

export class EntityServices<T extends IEntity> {

    entityForLog: string;
    baseUrl: string;
    entitiesCount: number;

    constructor (_entity: string, _baseUrl: string) {
        this.entityForLog = _entity;
        this.baseUrl = _baseUrl;
        this.entitiesCount = 0
    }

    async getEntities (_query?: string): Promise<T[]> {
        const response: AxiosResponse = await api.get(`${this.baseUrl}${_query ? '?' + _query : ''}`);
        
        // console.log(response);
        if (response.data && response?.request?.status === 200) {
            return response.data;
        }
        throw new Error(`Não foi possível buscar os(as) ${this.entityForLog}s`);
    }

    async getEntity (_id: string): Promise<T> {
        const response: AxiosResponse = await api.get(`${this.baseUrl}/${_id}`);
    
        if (response.data && response?.request?.status === 200) {
            return response.data
        }
        throw new Error(`Não foi possível buscar o(a) ${this.entityForLog}`);
    }

    async getEntitiesCount (): Promise<number> {
        const response: AxiosResponse = await api.get(`${this.baseUrl}/count`);
    
        if (response.data && response?.request?.status === 200) {
            const count: number = response.data;
            return count;
        }
        throw new Error(`Não foi possível contar os(as) ${this.entityForLog}s`);
    }

    async createEntity (_payload: T): Promise<T> {
        const response: AxiosResponse = await api.post(`${this.baseUrl}`, _payload);

        if (response.data && response?.request?.status === 200) {
            let entity: T = response.data

            if (!entity.id) throw new Error(`Erro ao criar um(a) ${this.entityForLog}.`);
                return entity;

        } else if (response.data && response?.request?.status === 400) {
            throw new Error(response.data as string);
        }
        throw new Error(`Não foi possível criar um(a) ${this.entityForLog}.`);
    }

    async updateEntity (_id: string, _payload: T): Promise<T> {
        const response: AxiosResponse = await api.put(`${this.baseUrl}/${_id}`, _payload);
    
        if (response.data && response?.request?.status === 200) {
            return response.data
        }
        throw new Error(`Não foi possível editar um(a) ${this.entityForLog}.`);
    }

    async deleteEntity (_id: string): Promise<T> {
        const response: AxiosResponse = await api.delete(`${this.baseUrl}/${_id}`);
    
        if (response.data && response?.request?.status === 200) {
            return response.data

        } else if (response.data && response?.request?.status === 400) {
            throw new Error(response.data as string);
        }
        throw new Error(`Não foi possível remover um(a) ${this.entityForLog}.`);
    }

}
