import { FC, createContext, useContext, useState } from 'react';
import { toast } from 'react-toastify';

import {
	CnaeServices,
	NatJurServices,
	SituCadServices,
	MotivoServices,
	QualificacaoServices,
	PorteServices,
	MatrizFilialServices,
	FaixaEtariaServices,
	LogradouroServices,
	PaisServices,
} from '../services/sideEntities';
import { ISideEntity, IEstadoMunicipio, ISideEntityContext, IHookProvider } from '../types';

const SideEntitiesContext = createContext<ISideEntityContext>({} as ISideEntityContext);

export const SideEntitiesProvider: FC<IHookProvider> = (_params: IHookProvider) => {
	const cnaeServices = new CnaeServices();
	const natJurServices = new NatJurServices();
	const situCadServices = new SituCadServices();
	const motivoServices = new MotivoServices();
	const qualificacaoServices = new QualificacaoServices();
	const porteServices = new PorteServices();
	const matrizFilialServices = new MatrizFilialServices();
	const faixaEtariaServices = new FaixaEtariaServices();
	const logradouroServices = new LogradouroServices();
	const paisServices = new PaisServices();

	const [cnaes, setCnaes] = useState<ISideEntity[]>([]);
	const [natJurs, setNatJurs] = useState<ISideEntity[]>([]);
	const [situCads, setSituCads] = useState<ISideEntity[]>([]);
	const [motivos, setMotivos] = useState<ISideEntity[]>([]);
	const [qualificacoes, setQualificacoes] = useState<ISideEntity[]>([]);
	const [porteEmpresas, setPorteEmpresas] = useState<ISideEntity[]>([]);
	const [matrizFiliais, setMatrizFiliais] = useState<ISideEntity[]>([]);
	const [faixasEtarias, setFaixasEtarias] = useState<ISideEntity[]>([]);
	const [estadosMunicipios, setEstadosMunicipios] = useState<IEstadoMunicipio>(
		{} as IEstadoMunicipio
	);
	const [paises, setPaises] = useState<ISideEntity[]>([]);
	const [loadingCnaes, setLoadingCnaes] = useState<boolean>(false);
	const [loadingNatJurs, setLoadingNatJurs] = useState<boolean>(false);
	const [loadingSituCads, setLoadingSituCads] = useState<boolean>(false);
	const [loadingMotivos, setLoadingMotivos] = useState<boolean>(false);
	const [loadingQualif, setLoadingQualif] = useState<boolean>(false);
	const [loadingPortes, setLoadingPortes] = useState<boolean>(false);
	const [loadingMatrizFiliais, setLoadingMatrizFiliais] = useState<boolean>(false);
	const [loadingFaixasEtarias, setLoadingFaixasEtarias] = useState<boolean>(false);
	const [loadingEstadosMunicipios, setLoadingEstadosMunicipios] = useState<boolean>(false);
	const [loadingPaises, setLoadingPaises] = useState<boolean>(false);

	const fetchCnaes = async () => {
		let tempCnaes: ISideEntity[] = [];
		setLoadingCnaes(true);
		try {
			tempCnaes = await cnaeServices.getEntities();
			toast.success('CNAEs carregados!');
		} catch (_err) {
			toast.error('Nenhum CNAE foi encontrado.');
		}
		setCnaes([...tempCnaes]);
		setLoadingCnaes(false);
	};

	const fetchNatJurs = async () => {
		let tempNatJurs: ISideEntity[] = [];
		setLoadingNatJurs(true);
		try {
			tempNatJurs = await natJurServices.getEntities();
			toast.success('Naturezas Jurídicas carregadas!');
		} catch (_err) {
			toast.error('Nenhuma Natureza Jurídica foi encontrada.');
		}
		setNatJurs([...tempNatJurs]);
		setLoadingNatJurs(false);
	};

	const fetchSituCads = async () => {
		let tempSituCads: ISideEntity[] = [];
		setLoadingSituCads(true);
		try {
			tempSituCads = await situCadServices.getEntities();
			toast.success('Situações de Cadastro carregados!');
		} catch (_err) {
			toast.error('Nenhuma Situação de Cadastro foi encontrada.');
		}
		setSituCads([...tempSituCads]);
		setLoadingSituCads(false);
	};

	const fetchMotivos = async () => {
		let tempMotivos: ISideEntity[] = [];
		setLoadingMotivos(true);
		try {
			tempMotivos = await motivoServices.getEntities();
			toast.success('Motivos de Situação carregados!');
		} catch (_err) {
			toast.error('Nenhum Motivo de Situação foi encontrado.');
		}
		setMotivos([...tempMotivos]);
		setLoadingMotivos(false);
	};

	const fetchQualificacoes = async () => {
		let tempQualificacoes: ISideEntity[] = [];
		setLoadingQualif(true);
		try {
			tempQualificacoes = await qualificacaoServices.getEntities();
			toast.success('Qualificações carregadas!');
		} catch (_err) {
			toast.error('Nenhuma Qualificação foi encontrada.');
		}
		setQualificacoes([...tempQualificacoes]);
		setLoadingQualif(false);
	};

	const fetchPorteEmpresas = async () => {
		let tempPorteEmpresas: ISideEntity[] = [];
		setLoadingPortes(true);
		try {
			tempPorteEmpresas = await porteServices.getEntities();
			toast.success('Portes de Empresa carregados!');
		} catch (_err) {
			toast.error('Nenhum Porte de Empresa foi encontrado.');
		}
		setPorteEmpresas([...tempPorteEmpresas]);
		setLoadingPortes(false);
	};

	const fetchMatrizFiliais = async () => {
		let tempMatrizFiliais: ISideEntity[] = [];
		setLoadingMatrizFiliais(true);
		try {
			tempMatrizFiliais = await matrizFilialServices.getEntities();
			toast.success('Matrizes/Filiais carregadas!');
		} catch (_err) {
			toast.error('Nenhuma Matriz/Filial foi encontrada.');
		}
		setMatrizFiliais([...tempMatrizFiliais]);
		setLoadingMatrizFiliais(false);
	};

	const fetchFaixasEtarias = async () => {
		let tempFaixasEtarias: ISideEntity[] = [];
		setLoadingFaixasEtarias(true);
		try {
			tempFaixasEtarias = await faixaEtariaServices.getEntities();
			toast.success('Faixas Etárias carregadas!');
		} catch (_err) {
			toast.error('Nenhuma Faixa Etária foi encontrada.');
		}
		setFaixasEtarias([...tempFaixasEtarias]);
		setLoadingFaixasEtarias(false);
	};

	const fetchEstadosMunicipios = async () => {
		let tempEstadosMunicipios: any = {};
		setLoadingEstadosMunicipios(true);
		try {
			tempEstadosMunicipios = await logradouroServices.getEntities();
			toast.success('Estados e Municípios carregados!');
		} catch (_err) {
			toast.error('Nenhum Estado ou Município foi encontrado.');
		}
		setEstadosMunicipios(tempEstadosMunicipios);
		setLoadingEstadosMunicipios(false);
	};

	const fetchPaises = async () => {
		let tempPaises: ISideEntity[] = [];
		setLoadingPaises(true);
		try {
			tempPaises = await paisServices.getEntities();
			toast.success('Paises carregados!');
		} catch (_err) {
			toast.error('Nenhum País foi encontrado.');
		}
		setPaises([...tempPaises]);
		setLoadingPaises(false);
	};

	return (
		<SideEntitiesContext.Provider
			value={{
				cnaes,
				natJurs,
				situCads,
				motivos,
				qualificacoes,
				porteEmpresas,
				matrizFiliais,
				faixasEtarias,
				estadosMunicipios,
				paises,
				loadingCnaes,
				loadingNatJurs,
				loadingSituCads,
				loadingMotivos,
				loadingQualif,
				loadingPortes,
				loadingMatrizFiliais,
				loadingFaixasEtarias,
				loadingEstadosMunicipios,
				loadingPaises,

				fetchCnaes,
				fetchNatJurs,
				fetchSituCads,
				fetchMotivos,
				fetchQualificacoes,
				fetchPorteEmpresas,
				fetchMatrizFiliais,
				fetchFaixasEtarias,
				fetchEstadosMunicipios,
				fetchPaises,
			}}
		>
			{_params.children}
		</SideEntitiesContext.Provider>
	);
};

export function useSideEntities() {
	const context = useContext(SideEntitiesContext);

	if (!context) {
		throw new Error('useSideEntities must be used within an SideEntitiesProvider');
	}

	return context;
}
