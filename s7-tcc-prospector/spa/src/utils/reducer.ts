import { IEmpresa } from '../types';

export const reducer = (empresas: IEmpresa[], action: any) => {
    switch (action.type) {
        case 'selection':
            return empresas.map((empresa: IEmpresa) => {
                if (empresa.id === action.empresa.id) {
                  return action.empresa;
                } else {
                  return empresa;
                }
              });

        case 'updateList':
            return empresas
    
        default:
            throw Error('Unknown action: ' + action.type);
    }
}