# ### Built-in deps
from typing import List, Dict
import csv
from datetime import datetime, timezone, timedelta

# ### Third-party deps
from pydantic import BaseModel
from sqlalchemy import select, cast, Date
from sqlalchemy.sql import functions as func, or_
import pandas as pd

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Empresa
from ..qualificacoes.model import Qualificacao
from ..naturezas_juridicas.model import NaturezaJuridica
from ..portes_empresas.model import PorteEmpresa
from ..simples_nacional.model import Simples
from ..estabelecimentos.model import Estabelecimento
from ..situacoes_cadastrais.model import SituacaoCadastral
from ..matrizes_filiais.model import MatrizFilial
from ..cnaes.model import CNAE
from ..motivos.model import Motivo
from ..logradouros.model import Logradouro
from ..municipios.model import Municipio
from ..paises.model import Pais
from ..contatos.model import Contato
from ..socios.model import Socio
from ..representantes_legais.model import Representante
from ..fgts.model import FGTS
from ..sida.model import SIDA
from ..previdenciario.model import Previdenciario
from ..entidades_responsaveis.model import EntidadeResponsavel
from ..receitas_principais.model import ReceitaPrincipal
from ..situacoes_inscricao.model import SituacaoInscricao
from ..tipos_credito.model import TipoCredito
from ..tipos_devedor.model import TipoDevedor
from ..tipos_situacao_inscricao.model import TipoSituacaoInscricao
from ..unidades.model import Unidade
from .schema import EmpresasView, EmpresasCreate, EmpresasUpdate, EmpresasFilter, EmpresasMainView, EmpresasTribView

pd.set_option('display.max_columns', None)


class EmpresasRepo(BaseRepo[Empresa, EmpresasCreate, EmpresasUpdate]):

    def standard_get_all_by(self):
        return select(
            self.model.id,
            func.concat(
                self.model.id, "/", Estabelecimento.cnpj_ordem, "-", Estabelecimento.cnpj_digit_verif
            ).label("cnpj"),
            self.model.razao_social,
            NaturezaJuridica.descricao.label("natureza_juridica"),
            CNAE.descricao.label("cnae"),
            PorteEmpresa.descricao.label("porte_empresa"),
            SituacaoCadastral.descricao.label("situacao_cadastral"),
            func.concat(
                Municipio.descricao, "/", Logradouro.uf
            ).label("municipio"),
            cast(Simples.data_opcao, Date).label("data_opcao_simples"),
        ).join(NaturezaJuridica, self.model.natureza_juridica == NaturezaJuridica.id, isouter=True
               ).join(PorteEmpresa, self.model.porte_empresa == PorteEmpresa.id, isouter=True
                      ).join(Simples, self.model.id == Simples.id, isouter=True
                             ).join(Estabelecimento, self.model.id == Estabelecimento.cnpj_base, isouter=True
                                    ).join(SituacaoCadastral, Estabelecimento.situacao_cadastral == SituacaoCadastral.id, isouter=True
                                           ).join(CNAE, Estabelecimento.cnae_principal == CNAE.id, isouter=True
                                                  # ).join(Motivo, Estabelecimento.motivo == Motivo.id, isouter=True
                                                  ).join(Logradouro, Estabelecimento.logradouro == Logradouro.id, isouter=True
                                                         ).join(Municipio, Logradouro.municipio == Municipio.id, isouter=True
                                                                )

    def trib_get_all_by(self, query):
        return query.join(
            FGTS, self.model.id == FGTS.cnpj_base, isouter=True
        ).join(SIDA, self.model.id == SIDA.cnpj_base, isouter=True
               ).join(Previdenciario, self.model.id == Previdenciario.cnpj_base, isouter=True
                      ).join(EntidadeResponsavel, FGTS.entidade_responsavel == EntidadeResponsavel.id, isouter=True
                             ).join(ReceitaPrincipal, (FGTS.receita_principal == ReceitaPrincipal.id) | (SIDA.receita_principal == ReceitaPrincipal.id), isouter=True
                                    ).join(SituacaoInscricao, (FGTS.situacao_inscricao == SituacaoInscricao.id) | (SIDA.situacao_inscricao == SituacaoInscricao.id) | (Previdenciario.situacao_inscricao == SituacaoInscricao.id), isouter=True
                                           ).join(TipoCredito, Previdenciario.tipo_credito == TipoCredito.id, isouter=True
                                                  ).join(TipoDevedor, (FGTS.tipo_devedor == TipoDevedor.id) | (SIDA.tipo_devedor == TipoDevedor.id) | (Previdenciario.tipo_devedor == TipoDevedor.id), isouter=True
                                                         ).join(TipoSituacaoInscricao, (FGTS.tipo_situacao_inscricao == TipoSituacaoInscricao.id) | (SIDA.tipo_situacao_inscricao == TipoSituacaoInscricao.id) | (Previdenciario.tipo_situacao_inscricao == TipoSituacaoInscricao.id), isouter=True
                                                                ).join(Unidade, (FGTS.unidade_responsavel == Unidade.id) | (FGTS.unidade_inscricao == Unidade.id) | (SIDA.unidade_responsavel == Unidade.id) | (Previdenciario.unidade_responsavel == Unidade.id), isouter=True
                                                                       ).distinct(self.model.id)

    def fgts_get_all_by(self, query):
        return query.join(
            FGTS, self.model.id == FGTS.cnpj_base, isouter=True
        ).join(EntidadeResponsavel, FGTS.entidade_responsavel == EntidadeResponsavel.id, isouter=True
               ).join(ReceitaPrincipal, FGTS.receita_principal == ReceitaPrincipal.id, isouter=True
                      ).join(SituacaoInscricao, FGTS.situacao_inscricao == SituacaoInscricao.id, isouter=True
                             ).join(TipoDevedor, FGTS.tipo_devedor == TipoDevedor.id, isouter=True
                                    ).join(TipoSituacaoInscricao, FGTS.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                           ).join(Unidade, (FGTS.unidade_responsavel == Unidade.id) | (FGTS.unidade_inscricao == Unidade.id), isouter=True
                                                  ).distinct(self.model.id)

    def sida_get_all_by(self, query):
        return query.join(
            SIDA, self.model.id == SIDA.cnpj_base, isouter=True
        ).join(ReceitaPrincipal, SIDA.receita_principal == ReceitaPrincipal.id, isouter=True
               ).join(SituacaoInscricao, SIDA.situacao_inscricao == SituacaoInscricao.id, isouter=True
                      ).join(TipoDevedor, SIDA.tipo_devedor == TipoDevedor.id, isouter=True
                             ).join(TipoSituacaoInscricao, SIDA.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                    ).join(Unidade, SIDA.unidade_responsavel == Unidade.id, isouter=True
                                           ).distinct(self.model.id)

    def prev_get_all_by(self, query):
        return query.join(
            Previdenciario, self.model.id == Previdenciario.cnpj_base, isouter=True
        ).join(SituacaoInscricao, Previdenciario.situacao_inscricao == SituacaoInscricao.id, isouter=True
               ).join(TipoCredito, Previdenciario.tipo_credito == TipoCredito.id, isouter=True
                      ).join(TipoDevedor, Previdenciario.tipo_devedor == TipoDevedor.id, isouter=True
                             ).join(TipoSituacaoInscricao, Previdenciario.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                    ).join(Unidade, Previdenciario.unidade_responsavel == Unidade.id, isouter=True
                                           ).distinct(self.model.id)

    def define_where_clause_by_standard_filters(self, query, filters):
        if filters["natureza_juridica"]:
            query = query.where(
                self.model.natureza_juridica.in_(filters["natureza_juridica"])
            )

        if filters["porte_empresa"]:
            query = query.where(
                self.model.porte_empresa.in_(filters["porte_empresa"])
            )

        if filters["situacao_cadastral"]:
            query = query.where(
                Estabelecimento.situacao_cadastral.in_(
                    filters["situacao_cadastral"])
            )

        if filters["cnae"]:
            or_expressions = []

            for cnae in filters["cnae"]:
                or_expressions.append(
                    Estabelecimento.cnaes_secundarios.contains(cnae))

            query = query.where(
                or_(Estabelecimento.cnae_principal.in_(
                    filters["cnae"]), *or_expressions)
            )

        if filters["municipio"]:
            query = query.where(
                Logradouro.municipio.in_(filters["municipio"])
            )

        if filters["uf"]:
            query = query.where(
                Logradouro.uf.in_(filters["uf"])
            )

        if isinstance(filters["situacao_especial"], bool):
            query = query.where(
                Estabelecimento.situacao_especial == filters["situacao_especial"]
            )

        if filters["max_capital_social"] != 0:
            query = query.where(
                self.model.capital_social >= filters["min_capital_social"],
                self.model.capital_social <= filters["max_capital_social"]
            )

        return query

    def define_where_clause_by_trib_filters(self, query, filters):
        if filters["situacao_inscricao"]:
            query = query.where(
                FGTS.situacao_inscricao.in_(filters["situacao_inscricao"]) |
                SIDA.situacao_inscricao.in_(filters["situacao_inscricao"]) |
                Previdenciario.situacao_inscricao.in_(
                    filters["situacao_inscricao"])
            )

        if filters["tipo_situacao_inscricao"]:
            query = query.where(
                FGTS.tipo_situacao_inscricao.in_(filters["tipo_situacao_inscricao"]) |
                SIDA.tipo_situacao_inscricao.in_(filters["tipo_situacao_inscricao"]) |
                Previdenciario.tipo_situacao_inscricao.in_(
                    filters["tipo_situacao_inscricao"])
            )

        if filters["tipo_devedor"]:
            query = query.where(
                FGTS.tipo_devedor.in_(filters["tipo_devedor"]) |
                SIDA.tipo_devedor.in_(filters["tipo_devedor"]) |
                Previdenciario.tipo_devedor.in_(filters["tipo_devedor"])
            )

        if filters["tipo_credito"]:
            query = query.where(
                Previdenciario.tipo_credito.in_(filters["tipo_credito"])
            )

        if filters["entidade_responsavel"]:
            query = query.where(
                FGTS.entidade_responsavel.in_(filters["entidade_responsavel"])
            )

        if filters["unidade_responsavel"]:
            query = query.where(
                FGTS.unidade_responsavel.in_(filters["unidade_responsavel"]) |
                SIDA.unidade_responsavel.in_(filters["unidade_responsavel"]) |
                Previdenciario.unidade_responsavel.in_(
                    filters["unidade_responsavel"])
            )

        if filters["unidade_inscricao"]:
            query = query.where(
                FGTS.unidade_inscricao.in_(filters["unidade_inscricao"])
            )

        if filters["receita_principal"]:
            query = query.where(
                FGTS.receita_principal.in_(filters["receita_principal"]) |
                SIDA.receita_principal.in_(filters["receita_principal"])
            )

        if isinstance(filters["indicador_ajuizado"], bool):
            query = query.where(
                FGTS.indicador_ajuizado == filters["indicador_ajuizado"] |
                SIDA.indicador_ajuizado == filters["indicador_ajuizado"] |
                Previdenciario.indicador_ajuizado == filters["indicador_ajuizado"]
            )

        if filters["max_valor_consolidado"] != 0:
            min_vc = filters["min_valor_consolidado"]
            max_vc = filters["max_valor_consolidado"]

            query = query.where(
                (
                    (FGTS.valor_consolidado >= min_vc) &
                    (FGTS.valor_consolidado <= max_vc)
                ) |
                (
                    (SIDA.valor_consolidado >= min_vc) &
                    (SIDA.valor_consolidado <= max_vc)
                ) |
                (
                    (Previdenciario.valor_consolidado >= min_vc) &
                    (Previdenciario.valor_consolidado <= max_vc)
                )
            )

        return query

    def define_where_clause_by_fgts_filters(self, query, filters):
        if filters["situacao_inscricao"]:
            query = query.where(
                FGTS.situacao_inscricao.in_(filters["situacao_inscricao"])
            )

        if filters["tipo_situacao_inscricao"]:
            query = query.where(
                FGTS.tipo_situacao_inscricao.in_(
                    filters["tipo_situacao_inscricao"])
            )

        if filters["tipo_devedor"]:
            query = query.where(
                FGTS.tipo_devedor.in_(filters["tipo_devedor"])
            )

        if filters["entidade_responsavel"]:
            query = query.where(
                FGTS.entidade_responsavel.in_(filters["entidade_responsavel"])
            )

        if filters["unidade_responsavel"]:
            query = query.where(
                FGTS.unidade_responsavel.in_(filters["unidade_responsavel"])
            )

        if filters["unidade_inscricao"]:
            query = query.where(
                FGTS.unidade_inscricao.in_(filters["unidade_inscricao"])
            )

        if filters["receita_principal"]:
            query = query.where(
                FGTS.receita_principal.in_(filters["receita_principal"])
            )

        if isinstance(filters["indicador_ajuizado"], bool):
            query = query.where(
                FGTS.indicador_ajuizado == filters["indicador_ajuizado"]
            )

        if filters["max_valor_consolidado"] != 0:
            query = query.where(
                FGTS.valor_consolidado >= filters["min_valor_consolidado"],
                FGTS.valor_consolidado <= filters["max_valor_consolidado"]
            )

        return query

    def define_where_clause_by_sida_filters(self, query, filters):
        if filters["situacao_inscricao"]:
            query = query.where(
                SIDA.situacao_inscricao.in_(filters["situacao_inscricao"])
            )

        if filters["tipo_situacao_inscricao"]:
            query = query.where(
                SIDA.tipo_situacao_inscricao.in_(
                    filters["tipo_situacao_inscricao"])
            )

        if filters["tipo_devedor"]:
            query = query.where(
                SIDA.tipo_devedor.in_(filters["tipo_devedor"])
            )

        if filters["receita_principal"]:
            query = query.where(
                SIDA.receita_principal.in_(filters["receita_principal"])
            )

        if filters["unidade_responsavel"]:
            query = query.where(
                SIDA.unidade_responsavel.in_(filters["unidade_responsavel"])
            )

        if isinstance(filters["indicador_ajuizado"], bool):
            query = query.where(
                SIDA.indicador_ajuizado == filters["indicador_ajuizado"]
            )

        if filters["max_valor_consolidado"] != 0:
            query = query.where(
                SIDA.valor_consolidado >= filters["min_valor_consolidado"],
                SIDA.valor_consolidado <= filters["max_valor_consolidado"]
            )

        return query

    def define_where_clause_by_prev_filters(self, query, filters):
        if filters["situacao_inscricao"]:
            query = query.where(
                Previdenciario.situacao_inscricao.in_(
                    filters["situacao_inscricao"])
            )

        if filters["tipo_situacao_inscricao"]:
            query = query.where(
                Previdenciario.tipo_situacao_inscricao.in_(
                    filters["tipo_situacao_inscricao"])
            )

        if filters["tipo_devedor"]:
            query = query.where(
                Previdenciario.tipo_devedor.in_(filters["tipo_devedor"])
            )

        if filters["tipo_credito"]:
            query = query.where(
                Previdenciario.tipo_credito.in_(filters["tipo_credito"])
            )

        if filters["unidade_responsavel"]:
            query = query.where(
                Previdenciario.unidade_responsavel.in_(
                    filters["unidade_responsavel"])
            )

        if isinstance(filters["indicador_ajuizado"], bool):
            query = query.where(
                Previdenciario.indicador_ajuizado == filters["indicador_ajuizado"]
            )

        if filters["max_valor_consolidado"] != 0:
            query = query.where(
                Previdenciario.valor_consolidado >= filters["min_valor_consolidado"],
                Previdenciario.valor_consolidado <= filters["max_valor_consolidado"]
            )

        return query

    def get_all_by(self, filters: BaseModel) -> List[Empresa]:
        filters: Dict = filters.dict()

        query = self.standard_get_all_by()

        trib_type = filters.get("tipo_trib")
        if trib_type:
            match trib_type.upper():
                case "FGTS":
                    query = self.fgts_get_all_by(query)
                    query = self.define_where_clause_by_fgts_filters(
                        query, filters)

                case "SIDA":
                    query = self.sida_get_all_by(query)
                    query = self.define_where_clause_by_sida_filters(
                        query, filters)

                case "PREV":
                    query = self.prev_get_all_by(query)
                    query = self.define_where_clause_by_prev_filters(
                        query, filters)

                case _:
                    query = self.trib_get_all_by(query)
                    query = self.define_where_clause_by_trib_filters(
                        query, filters)

        else:
            query = query.distinct(self.model.id)

        query = self.define_where_clause_by_standard_filters(query, filters)

        if filters["skip"] != 0:
            query = query.offset(filters["skip"])

        if filters["limit"] != 0:
            query = query.limit(filters["limit"])

        results = []
        try:
            results = self.session.execute(query).all()
        except Exception as err:
            print(err)

        self.session.close()
        return results

    def get_empresas_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            func.concat(
                self.model.id, "/", Estabelecimento.cnpj_ordem, "-", Estabelecimento.cnpj_digit_verif
            ).label("cnpj"),
            self.model.razao_social,
            self.model.capital_social,
            NaturezaJuridica.descricao.label("natureza_juridica"),
            PorteEmpresa.descricao.label("porte_empresa"),
            cast(Simples.data_opcao, Date).label("data_entrou_simples"),
            cast(Simples.data_exclusao, Date).label("data_saiu_simples"),
        ).join(Estabelecimento, self.model.id == Estabelecimento.cnpj_base, isouter=True
               ).join(NaturezaJuridica, self.model.natureza_juridica == NaturezaJuridica.id, isouter=True
                      ).join(PorteEmpresa, self.model.porte_empresa == PorteEmpresa.id, isouter=True
                             ).join(Simples, self.model.id == Simples.id, isouter=True
                                    ).where(
            self.model.id.in_(selected_ids)
        ).distinct(self.model.id)

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_estabelecimentos_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            Estabelecimento.nome_fantasia,
            MatrizFilial.descricao.label("matriz_filial"),
            CNAE.descricao.label("cnae"),
            Estabelecimento.cnaes_secundarios,
            cast(Estabelecimento.data_inicio_atividade,
                 Date).label("data_inicio_atividade"),
            SituacaoCadastral.descricao.label("situacao_cadastral"),
            Motivo.descricao.label("motivo_situacao_cadastral"),
            cast(Estabelecimento.data_situacao_cadastral,
                 Date).label("data_situacao_cadastral"),
            Logradouro.cep.label("cep"),
            func.concat(
                Logradouro.tipo, " ", Logradouro.nome, ", ", Logradouro.numero, "/", Logradouro.complemento, " - ", Logradouro.bairro
            ).label("logradouro"),
            func.concat(Municipio.descricao, "/",
                        Logradouro.uf).label("municipio/estado"),
            func.concat(Logradouro.nome_cidade_exterior, "/",
                        Pais.descricao,).label("exterior"),
            Estabelecimento.situacao_especial,
            cast(Estabelecimento.data_situacao_especial,
                 Date).label("data_situacao_especial"),
        ).join(Estabelecimento, self.model.id == Estabelecimento.cnpj_base, isouter=True
               ).join(MatrizFilial, Estabelecimento.matriz_filial == MatrizFilial.id, isouter=True
                      ).join(SituacaoCadastral, Estabelecimento.situacao_cadastral == SituacaoCadastral.id, isouter=True
                             ).join(CNAE, Estabelecimento.cnae_principal == CNAE.id, isouter=True
                                    ).join(Motivo, Estabelecimento.motivo == Motivo.id, isouter=True
                                           ).join(Logradouro, Estabelecimento.logradouro == Logradouro.id, isouter=True
                                                  ).join(Pais, Logradouro.pais == Pais.id, isouter=True
                                                         ).join(Municipio, Logradouro.municipio == Municipio.id, isouter=True
                                                                ).where(
            self.model.id.in_(selected_ids)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_socios_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            Socio.nome,
            Socio.cpf_cnpj,
            Socio.pais,
            Qualificacao.descricao.label("qualificacao"),
            cast(Socio.data_entrada_sociedade, Date).label(
                "data_entrada_sociedade"),
            Socio.faixa_etaria,
            Representante.cpf.label("representante legal"),
        ).join(Socio, self.model.id == Socio.cnpj_base, isouter=True
               ).join(Qualificacao, self.model.qualificacao_responsavel == Qualificacao.id, isouter=True
                      ).join(Representante, Socio.representante_legal == Representante.id, isouter=True
                             ).where(
            self.model.id.in_(selected_ids) & (Socio.cpf_cnpj != None)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_contatos_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            Contato.tipo,
            Contato.descricao,
        ).join(Estabelecimento, self.model.id == Estabelecimento.cnpj_base, isouter=True
               ).join(Contato, Estabelecimento.id == Contato.estabelecimento, isouter=True
                      ).where(
            self.model.id.in_(selected_ids) & (Contato.tipo != None)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_fgts_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            TipoDevedor.descricao.label("tipo_devedor"),
            FGTS.uf_devedor,
            Unidade.descricao.label("unidade_responsavel"),
            EntidadeResponsavel.descricao.label("entidade_responsavel"),
            Unidade.descricao.label("unidade_inscricao"),
            FGTS.numero_inscricao,
            TipoSituacaoInscricao.descricao.label("tipo_situacao_inscricao"),
            SituacaoInscricao.descricao.label("situacao_inscricao"),
            ReceitaPrincipal.descricao.label("receita_principal"),
            cast(FGTS.data_inscricao, Date).label("data_inscricao"),
            FGTS.indicador_ajuizado,
            FGTS.valor_consolidado,
        ).join(FGTS, self.model.id == FGTS.cnpj_base, isouter=True
               ).join(EntidadeResponsavel, FGTS.entidade_responsavel == EntidadeResponsavel.id, isouter=True
                      ).join(ReceitaPrincipal, FGTS.receita_principal == ReceitaPrincipal.id, isouter=True
                             ).join(SituacaoInscricao, FGTS.situacao_inscricao == SituacaoInscricao.id, isouter=True
                                    ).join(TipoDevedor, FGTS.tipo_devedor == TipoDevedor.id, isouter=True
                                           ).join(TipoSituacaoInscricao, FGTS.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                                  ).join(Unidade, (FGTS.unidade_responsavel == Unidade.id) | (FGTS.unidade_inscricao == Unidade.id), isouter=True
                                                         ).where(
            FGTS.cnpj_base.in_(selected_ids)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_sida_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            TipoDevedor.descricao.label("tipo_devedor"),
            SIDA.uf_devedor,
            Unidade.descricao.label("unidade_responsavel"),
            SIDA.numero_inscricao,
            TipoSituacaoInscricao.descricao.label("tipo_situacao_inscricao"),
            SituacaoInscricao.descricao.label("situacao_inscricao"),
            ReceitaPrincipal.descricao.label("receita_principal"),
            cast(SIDA.data_inscricao, Date).label("data_inscricao"),
            SIDA.indicador_ajuizado,
            SIDA.valor_consolidado,
        ).join(SIDA, self.model.id == SIDA.cnpj_base, isouter=True
               ).join(ReceitaPrincipal, SIDA.receita_principal == ReceitaPrincipal.id, isouter=True
                      ).join(SituacaoInscricao, SIDA.situacao_inscricao == SituacaoInscricao.id, isouter=True
                             ).join(TipoDevedor, SIDA.tipo_devedor == TipoDevedor.id, isouter=True
                                    ).join(TipoSituacaoInscricao, SIDA.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                           ).join(Unidade, SIDA.unidade_responsavel == Unidade.id, isouter=True
                                                  ).where(
            SIDA.cnpj_base.in_(selected_ids)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def get_prev_by_selected_ids(self, selected_ids: List[str]):
        query = select(
            self.model.id,
            TipoDevedor.descricao.label("tipo_devedor"),
            Previdenciario.uf_devedor,
            Unidade.descricao.label("unidade_responsavel"),
            Previdenciario.numero_inscricao,
            TipoSituacaoInscricao.descricao.label("tipo_situacao_inscricao"),
            SituacaoInscricao.descricao.label("situacao_inscricao"),
            TipoCredito.descricao.label("tipo_credito"),
            cast(Previdenciario.data_inscricao, Date).label("data_inscricao"),
            Previdenciario.indicador_ajuizado,
            Previdenciario.valor_consolidado,
        ).join(Previdenciario, self.model.id == Previdenciario.cnpj_base, isouter=True
               ).join(SituacaoInscricao, Previdenciario.situacao_inscricao == SituacaoInscricao.id, isouter=True
                      ).join(TipoCredito, Previdenciario.tipo_credito == TipoCredito.id, isouter=True
                             ).join(TipoDevedor, Previdenciario.tipo_devedor == TipoDevedor.id, isouter=True
                                    ).join(TipoSituacaoInscricao, Previdenciario.tipo_situacao_inscricao == TipoSituacaoInscricao.id, isouter=True
                                           ).join(Unidade, Previdenciario.unidade_responsavel == Unidade.id, isouter=True
                                                  ).where(
            Previdenciario.cnpj_base.in_(selected_ids)
        )

        header = []
        results = []
        try:
            results = self.session.execute(query)
            header = results.keys()._keys
            results = results.all()
        except Exception as err:
            print(err)

        self.session.close()
        return results, header

    def write_rows(self, table_name, headers, rows, empresa, space, csvwriter):
        header = list(headers)
        header.pop(0)
        header.insert(0, table_name)
        csvwriter.writerow(header)

        for row in rows:
            if row[0] == empresa[0][:8]:
                row = list(row)
                row.pop(0)
                row.insert(0, space)
                csvwriter.writerow(row)
        csvwriter.writerow(space)

    def generate_csv(self, selected_ids: List[str]):
        empresas, empre_header = self.get_empresas_by_selected_ids(
            selected_ids)
        estabelecimentos, estab_header = self.get_estabelecimentos_by_selected_ids(
            selected_ids)
        socios, soc_header = self.get_socios_by_selected_ids(selected_ids)
        contatos, cont_header = self.get_contatos_by_selected_ids(selected_ids)

        fgts, fgts_header = self.get_fgts_by_selected_ids(selected_ids)
        sida, sida_header = self.get_sida_by_selected_ids(selected_ids)
        prev, prev_header = self.get_prev_by_selected_ids(selected_ids)

        file_path = "./exports/"
        file_name = datetime.now(
            timezone(-timedelta(hours=3))).strftime("%Y-%m-%d_%H-%M-%s")[:19] + ".csv"
        space = ""

        with open(file_path + file_name, "w", encoding="latin-1", newline="") as csvfile:
            csvwriter = csv.writer(
                csvfile,
                dialect="excel",
                delimiter=";",
            )

            csvwriter.writerow(empre_header)
            for empresa in empresas:
                csvwriter.writerow(empresa)

                if len(socios) > 0:
                    self.write_rows("socios", soc_header, socios,
                                    empresa, space, csvwriter)

                if len(estabelecimentos) > 0:
                    self.write_rows("estabelecimentos", estab_header,
                                    estabelecimentos, empresa, space, csvwriter)

                if len(contatos) > 0:
                    self.write_rows("contatos", cont_header,
                                    contatos, empresa, space, csvwriter)

                if len(fgts) > 0:
                    self.write_rows("fgts", fgts_header, fgts,
                                    empresa, space, csvwriter)

                if len(sida) > 0:
                    self.write_rows("sida", sida_header, sida,
                                    empresa, space, csvwriter)

                if len(prev) > 0:
                    self.write_rows("previdenciario", prev_header,
                                    prev, empresa, space, csvwriter)

        return file_path, file_name


def empresas_repo():
    return EmpresasRepo(Empresa)
