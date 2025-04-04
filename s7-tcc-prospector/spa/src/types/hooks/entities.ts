interface IEntity {
    id: string;
}

interface IEntityContext<T extends IEntity> {
    entities: T[];
    loading: boolean;

    fetchEntity: (_id: string) => Promise<T>;
    fetchEntities: (_query?: string) => void;

    createNewEntity: (payload: T) => Promise<T>;
    editEntity: (_id: string, _payload: T) => Promise<T>;
    deleteEntity: (_id: string) => any;

    searchEntity: string;
    setSearchEntity: (_value: string) => void;
    entitiesPerRow: string;
    setEntitiesPerRow: (_value: string) => void;
    paginate: number;
    setPaginate: (_value: number) => void;
}

export function isEntity(_data: any): _data is IEntity {
    return 'id' in _data;
}

export type { IEntity, IEntityContext };
