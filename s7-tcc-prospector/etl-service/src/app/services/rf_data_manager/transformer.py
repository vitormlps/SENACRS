# ### Built-in deps
from typing import List
from datetime import datetime
from time import sleep
from uuid import uuid4

# ### Third-party deps
import pandas as pd

# ### Local deps
from app.helpers import Logger
from app.utils.files_manip import (
    save_result_file,
    get_csv_reader,
    create_subfolder,
    get_files_names,
    get_dirs_names,
)


class DataTransformer:
    def __init__(self, tables_chunksize: int) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing DataTransformer")

        base_table = pd.DataFrame({
            "id": [],
            "descricao": [],
            "created_at": [],
            "updated_at": [],
        })
        self.logradouros = pd.DataFrame({
            "id": [],
            "tipo": [],
            "nome": [],
            "numero": [],
            "complemento": [],
            "bairro": [],
            "cep": [],
            "municipio": [],
            "uf": [],
            "nome_cidade_exterior": [],
            "pais": [],
            "created_at": [],
            "updated_at": [],
        })
        self.contatos = pd.DataFrame({
            "id": [],
            "tipo": [],
            "descricao": [],
            "estabelecimento": [],
            "created_at": [],
            "updated_at": [],
        })
        self.representantes = pd.DataFrame({
            "id": [],
            "cpf": [],
            "nome": [],
            "qualificacao": [],
            "created_at": [],
            "updated_at": [],
        })
        self.tipos_devedor = base_table.copy()
        self.entidades_responsaveis = base_table.copy()
        self.unidades = base_table.copy()
        self.tipos_situacao_inscricao = base_table.copy()
        self.situacoes_inscricao = base_table.copy()
        self.receitas_principais = base_table.copy()
        self.tipos_credito = base_table.copy()
        self.table_chunk_size = tables_chunksize

    def base_transform(self, row):
        now = datetime.now()

        row.loc["created_at"] = now
        row.loc["updated_at"] = now

        return row

    def transform_empresas(self, row):
        row.loc["capital_social"] = float(
            row.loc["capital_social"].split(",")[0])

        if str(row.loc["qualificacao_responsavel"]) == "36":
            row.loc["qualificacao_responsavel"] = "16"

        row = self.base_transform(row)
        return row

    def transform_estabelecimentos(self, row):
        row = self.base_transform(row)

        row.loc["cnpj_base"] = row.loc["id"]
        row.loc["id"] = str(uuid4())

        temp_created_at = row.loc["created_at"]
        temp_updated_at = row.loc["updated_at"]

        row.loc["matriz_filial"] = "0" + row.loc["matriz_filial"]

        temp = row.loc["data_situacao_cadastral"]
        row.loc["data_situacao_cadastral"] = temp if len(
            temp) >= 8 else '19700101'

        temp = row.loc["data_inicio_atividade"]
        row.loc["data_inicio_atividade"] = temp if len(
            temp) >= 8 else '19700101'

        temp = row.loc["data_situacao_especial"]
        row.loc["data_situacao_especial"] = temp if len(temp) >= 8 else None

        logradouro_id = str(uuid4())
        logradouro = pd.DataFrame({
            "id": [logradouro_id],
            "tipo": [row.loc["tipo_logradouro"]],
            "nome": [row.loc["logradouro"]],
            "numero": [row.loc["numero"]],
            "complemento": [row.loc["complemento"]],
            "bairro": [row.loc["bairro"]],
            "cep": [row.loc["cep"]],
            "municipio": [row.loc["municipio"]],
            "uf": [row.loc["estado_uf"]],
            "nome_cidade_exterior": [row.loc["nome_cidade_exterior"]],
            "pais": [row.loc["pais"]],
            "created_at": [temp_created_at],
            "updated_at": [temp_updated_at],
        })
        self.logradouros = pd.concat([logradouro.copy(), self.logradouros])
        row.loc["logradouro"] = logradouro_id

        fone = row.loc['telefone_1']
        if fone:
            ddd = row.loc['ddd_1']
            contato = pd.DataFrame({
                "id": [str(uuid4())],
                "tipo": ["Celular" if fone[0] == "9" else "Telefone"],
                "descricao": [f"({ddd}){fone}"],
                "estabelecimento": [row.loc["id"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.contatos = pd.concat([contato.copy(), self.contatos])

        fone = row.loc['telefone_2']
        if fone:
            ddd = row.loc['ddd_2']
            contato = pd.DataFrame({
                "id": [str(uuid4())],
                "tipo": ["Celular" if fone[0] == "9" else "Telefone"],
                "descricao": [f"({ddd}){fone}"],
                "estabelecimento": [row.loc["id"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.contatos = pd.concat([contato.copy(), self.contatos])

        email = row.loc['email']
        if email:
            contato = pd.DataFrame({
                "id": [str(uuid4())],
                "tipo": ["E-mail"],
                "descricao": [email],
                "estabelecimento": [row.loc["id"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.contatos = pd.concat([contato.copy(), self.contatos])

        return row

    def transform_logradouros(self, transforms_path: str, table_name: str, count: int):
        save_result_file(
            transforms_path + "/" + table_name + "/" + table_name + str(count),
            self.logradouros
        )
        self.logradouros = pd.DataFrame(columns=self.logradouros.columns)

    def transform_contatos(self, transforms_path: str, table_name: str, count: int):
        save_result_file(
            transforms_path + "/" + table_name + "/" + table_name + str(count),
            self.contatos
        )
        self.contatos = pd.DataFrame(columns=self.contatos.columns)

    def transform_socios(self, row):
        row = self.base_transform(row)

        row.loc["cnpj_base"] = row.loc["id"]
        row.loc["id"] = str(uuid4())

        temp = row.loc["data_entrada_sociedade"]
        row.loc["data_entrada_sociedade"] = temp if len(
            temp) >= 8 else '19700101'

        if row.loc["pais"] == '':
            row.loc["pais"] = None

        representante = str(row.loc["representante_legal"]).strip()
        if representante == "***000000**":
            row.loc["representante_legal"] = None
        else:
            representante = pd.DataFrame({
                "id": [str(uuid4())],
                "cpf": [representante],
                "nome": [row.loc["nome_representante"]],
                "qualificacao": [row.loc["qualificacao_representante"]],
                "created_at": [row.loc["created_at"]],
                "updated_at": [row.loc["updated_at"]],
            })
            self.representantes = pd.concat(
                [representante.copy(), self.representantes])

        faixa_etaria = str(row.loc["faixa_etaria"]).strip()
        if faixa_etaria == "0":
            row.loc["faixa_etaria"] = None

        return row

    def transform_representantes(self, transforms_path: str, table_name: str, count: int):
        save_result_file(
            transforms_path + "/" + table_name + "/" + table_name + str(count),
            self.representantes
        )
        self.representantes = pd.DataFrame(columns=self.representantes.columns)

    def transform_simples(self, row):
        temp = "00000000"

        if temp in str(row.loc["data_opcao"]).strip():
            row.loc["data_opcao"] = None

        if temp in str(row.loc["data_exclusao"]).strip():
            row.loc["data_exclusao"] = None

        row = self.base_transform(row)
        return row

    def transform_fgts(self, row):
        row = self.base_transform(row)

        row.loc["cnpj_base"] = row.loc["id"]
        row.loc["id"] = str(uuid4())

        temp_created_at = row.loc["created_at"]
        temp_updated_at = row.loc["updated_at"]

        temp = self.tipos_devedor.loc[self.tipos_devedor["descricao"]
                                      == row.loc["tipo_devedor"]]
        if temp.empty is False:
            row.loc["tipo_devedor"] = temp['id'][0]
        else:
            tipo_devedor_id = str(uuid4())
            tipo_devedor = pd.DataFrame({
                "id": [tipo_devedor_id],
                "descricao": [row.loc["tipo_devedor"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_devedor = pd.concat(
                [tipo_devedor.copy(), self.tipos_devedor])
            row.loc["tipo_devedor"] = tipo_devedor_id

        temp = self.entidades_responsaveis.loc[self.entidades_responsaveis["descricao"]
                                               == row.loc["entidade_responsavel"]]
        if temp.empty is False:
            row.loc["entidade_responsavel"] = temp['id'][0]
        else:
            entidade_responsavel_id = str(uuid4())
            entidade_responsavel = pd.DataFrame({
                "id": [entidade_responsavel_id],
                "descricao": [row.loc["entidade_responsavel"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.entidades_responsaveis = pd.concat(
                [entidade_responsavel.copy(), self.entidades_responsaveis])
            row.loc["entidade_responsavel"] = entidade_responsavel_id

        temp = self.unidades.loc[self.unidades["descricao"]
                                 == row.loc["unidade_responsavel"]]
        if temp.empty is False:
            row.loc["unidade_responsavel"] = temp['id'][0]
        else:
            unidade_responsavel_id = str(uuid4())
            unidades = pd.DataFrame({
                "id": [unidade_responsavel_id],
                "descricao": [row.loc["unidade_responsavel"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.unidades = pd.concat([unidades.copy(), self.unidades])
            row.loc["unidade_responsavel"] = unidade_responsavel_id

        temp = self.unidades.loc[self.unidades["descricao"]
                                 == row.loc["unidade_inscricao"]]
        if temp.empty is False:
            row.loc["unidade_inscricao"] = temp['id'][0]
        else:
            unidade_inscricao_id = str(uuid4())
            unidades = pd.DataFrame({
                "id": [unidade_inscricao_id],
                "descricao": [row.loc["unidade_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.unidades = pd.concat([unidades.copy(), self.unidades])
            row.loc["unidade_inscricao"] = unidade_inscricao_id

        temp = self.tipos_situacao_inscricao.loc[self.tipos_situacao_inscricao["descricao"]
                                                 == row.loc["tipo_situacao_inscricao"]]
        if temp.empty is False:
            row.loc["tipo_situacao_inscricao"] = temp['id'][0]
        else:
            tipo_situacao_inscricao_id = str(uuid4())
            tipo_situacao_inscricao = pd.DataFrame({
                "id": [tipo_situacao_inscricao_id],
                "descricao": [row.loc["tipo_situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_situacao_inscricao = pd.concat(
                [tipo_situacao_inscricao.copy(), self.tipos_situacao_inscricao])
            row.loc["tipo_situacao_inscricao"] = tipo_situacao_inscricao_id

        temp = self.situacoes_inscricao.loc[self.situacoes_inscricao["descricao"]
                                            == row.loc["situacao_inscricao"]]
        if temp.empty is False:
            row.loc["situacao_inscricao"] = temp['id'][0]
        else:
            situacao_inscricao_id = str(uuid4())
            situacao_inscricao = pd.DataFrame({
                "id": [situacao_inscricao_id],
                "descricao": [row.loc["situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.situacoes_inscricao = pd.concat(
                [situacao_inscricao.copy(), self.situacoes_inscricao])
            row.loc["situacao_inscricao"] = situacao_inscricao_id

        temp = self.receitas_principais.loc[self.receitas_principais["descricao"]
                                            == row.loc["receita_principal"]]
        if temp.empty is False:
            row.loc["receita_principal"] = temp['id'][0]
        else:
            receita_principal_id = str(uuid4())
            receita_principal = pd.DataFrame({
                "id": [receita_principal_id],
                "descricao": [row.loc["receita_principal"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.receitas_principais = pd.concat(
                [receita_principal.copy(), self.receitas_principais])
            row.loc["receita_principal"] = receita_principal_id

        row.loc["indicador_ajuizado"] = True if row.loc["indicador_ajuizado"] == 'SIM' else False
        row.loc["valor_consolidado"] = float(row.loc["valor_consolidado"])

        data_inscricao = row.loc["data_inscricao"]
        if data_inscricao == '01/01/1000':
            row.loc["data_inscricao"] = '01/07/1994'
        else:
            date = row.loc["data_inscricao"].split("/")
            row.loc["data_inscricao"] = f"{date[2]}-{date[1]}-{date[0]}"

        return row

    def transform_sida(self, row):
        row = self.base_transform(row)

        row.loc["cnpj_base"] = row.loc["id"]
        row.loc["id"] = str(uuid4())

        temp_created_at = row.loc["created_at"]
        temp_updated_at = row.loc["updated_at"]

        temp = self.tipos_devedor.loc[self.tipos_devedor["descricao"]
                                      == row.loc["tipo_devedor"]]
        if temp.empty is False:
            row.loc["tipo_devedor"] = temp['id'][0]
        else:
            tipo_devedor_id = str(uuid4())
            tipo_devedor = pd.DataFrame({
                "id": [tipo_devedor_id],
                "descricao": [row.loc["tipo_devedor"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_devedor = pd.concat(
                [tipo_devedor.copy(), self.tipos_devedor])
            row.loc["tipo_devedor"] = tipo_devedor_id

        temp = self.unidades.loc[self.unidades["descricao"]
                                 == row.loc["unidade_responsavel"]]
        if temp.empty is False:
            row.loc["unidade_responsavel"] = temp['id'][0]
        else:
            unidade_responsavel_id = str(uuid4())
            unidades = pd.DataFrame({
                "id": [unidade_responsavel_id],
                "descricao": [row.loc["unidade_responsavel"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.unidades = pd.concat([unidades.copy(), self.unidades])
            row.loc["unidade_responsavel"] = unidade_responsavel_id

        temp = self.tipos_situacao_inscricao.loc[self.tipos_situacao_inscricao["descricao"]
                                                 == row.loc["tipo_situacao_inscricao"]]
        if temp.empty is False:
            row.loc["tipo_situacao_inscricao"] = temp['id'][0]
        else:
            tipo_situacao_inscricao_id = str(uuid4())
            tipo_situacao_inscricao = pd.DataFrame({
                "id": [tipo_situacao_inscricao_id],
                "descricao": [row.loc["tipo_situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_situacao_inscricao = pd.concat(
                [tipo_situacao_inscricao.copy(), self.tipos_situacao_inscricao])
            row.loc["tipo_situacao_inscricao"] = tipo_situacao_inscricao_id

        temp = self.situacoes_inscricao.loc[self.situacoes_inscricao["descricao"]
                                            == row.loc["situacao_inscricao"]]
        if temp.empty is False:
            row.loc["situacao_inscricao"] = temp['id'][0]
        else:
            situacao_inscricao_id = str(uuid4())
            situacao_inscricao = pd.DataFrame({
                "id": [situacao_inscricao_id],
                "descricao": [row.loc["situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.situacoes_inscricao = pd.concat(
                [situacao_inscricao.copy(), self.situacoes_inscricao])
            row.loc["situacao_inscricao"] = situacao_inscricao_id

        temp = self.receitas_principais.loc[self.receitas_principais["descricao"]
                                            == row.loc["receita_principal"]]
        if temp.empty is False:
            row.loc["receita_principal"] = temp['id'][0]
        else:
            receita_principal_id = str(uuid4())
            receita_principal = pd.DataFrame({
                "id": [receita_principal_id],
                "descricao": [row.loc["receita_principal"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.receitas_principais = pd.concat(
                [receita_principal.copy(), self.receitas_principais])
            row.loc["receita_principal"] = receita_principal_id

        row.loc["indicador_ajuizado"] = True if row.loc["indicador_ajuizado"] == 'SIM' else False
        row.loc["valor_consolidado"] = float(row.loc["valor_consolidado"])

        data_inscricao = row.loc["data_inscricao"]
        if data_inscricao == '01/01/1000':
            row.loc["data_inscricao"] = '01/07/1994'
        else:
            date = row.loc["data_inscricao"].split("/")
            row.loc["data_inscricao"] = f"{date[2]}-{date[1]}-{date[0]}"

        return row

    def transform_prev(self, row):
        row = self.base_transform(row)

        row.loc["cnpj_base"] = row.loc["id"]
        row.loc["id"] = str(uuid4())

        temp_created_at = row.loc["created_at"]
        temp_updated_at = row.loc["updated_at"]

        temp = self.tipos_devedor.loc[self.tipos_devedor["descricao"]
                                      == row.loc["tipo_devedor"]]
        if temp.empty is False:
            row.loc["tipo_devedor"] = temp['id'][0]
        else:
            tipo_devedor_id = str(uuid4())
            tipo_devedor = pd.DataFrame({
                "id": [tipo_devedor_id],
                "descricao": [row.loc["tipo_devedor"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_devedor = pd.concat(
                [tipo_devedor.copy(), self.tipos_devedor])
            row.loc["tipo_devedor"] = tipo_devedor_id

        temp = self.unidades.loc[self.unidades["descricao"]
                                 == row.loc["unidade_responsavel"]]
        if temp.empty is False:
            row.loc["unidade_responsavel"] = temp['id'][0]
        else:
            unidade_responsavel_id = str(uuid4())
            unidades = pd.DataFrame({
                "id": [unidade_responsavel_id],
                "descricao": [row.loc["unidade_responsavel"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.unidades = pd.concat([unidades.copy(), self.unidades])
            row.loc["unidade_responsavel"] = unidade_responsavel_id

        temp = self.tipos_situacao_inscricao.loc[self.tipos_situacao_inscricao["descricao"]
                                                 == row.loc["tipo_situacao_inscricao"]]
        if temp.empty is False:
            row.loc["tipo_situacao_inscricao"] = temp['id'][0]
        else:
            tipo_situacao_inscricao_id = str(uuid4())
            tipo_situacao_inscricao = pd.DataFrame({
                "id": [tipo_situacao_inscricao_id],
                "descricao": [row.loc["tipo_situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_situacao_inscricao = pd.concat(
                [tipo_situacao_inscricao.copy(), self.tipos_situacao_inscricao])
            row.loc["tipo_situacao_inscricao"] = tipo_situacao_inscricao_id

        temp = self.situacoes_inscricao.loc[self.situacoes_inscricao["descricao"]
                                            == row.loc["situacao_inscricao"]]
        if temp.empty is False:
            row.loc["situacao_inscricao"] = temp['id'][0]
        else:
            situacao_inscricao_id = str(uuid4())
            situacao_inscricao = pd.DataFrame({
                "id": [situacao_inscricao_id],
                "descricao": [row.loc["situacao_inscricao"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.situacoes_inscricao = pd.concat(
                [situacao_inscricao.copy(), self.situacoes_inscricao])
            row.loc["situacao_inscricao"] = situacao_inscricao_id

        temp = self.tipos_credito.loc[self.tipos_credito["descricao"]
                                      == row.loc["tipo_credito"]]
        if temp.empty is False:
            row.loc["tipo_credito"] = temp['id'][0]
        else:
            tipo_credito_id = str(uuid4())
            tipo_credito = pd.DataFrame({
                "id": [tipo_credito_id],
                "descricao": [row.loc["tipo_credito"]],
                "created_at": [temp_created_at],
                "updated_at": [temp_updated_at],
            })
            self.tipos_credito = pd.concat(
                [tipo_credito.copy(), self.tipos_credito])
            row.loc["tipo_credito"] = tipo_credito_id

        row.loc["indicador_ajuizado"] = True if row.loc["indicador_ajuizado"] == 'SIM' else False
        row.loc["valor_consolidado"] = float(row.loc["valor_consolidado"])

        data_inscricao = row.loc["data_inscricao"]
        if data_inscricao == '01/01/1000':
            row.loc["data_inscricao"] = '01/07/1994'
        else:
            date = row.loc["data_inscricao"].split("/")
            row.loc["data_inscricao"] = f"{date[2]}-{date[1]}-{date[0]}"

        return row

    def transform_aux_trib_data(self, transforms_path: str, folder_name: str):
        self._logger.debug("Transfering aux trib data")

        folder_path = transforms_path + "/" + folder_name
        create_subfolder(folder_path)

        subset = "descricao"
        in_place = True

        self.tipos_devedor.drop_duplicates(subset=subset, inplace=in_place)
        self.entidades_responsaveis.drop_duplicates(
            subset=subset, inplace=in_place)
        self.unidades.drop_duplicates(subset=subset, inplace=in_place)
        self.tipos_situacao_inscricao.drop_duplicates(
            subset=subset, inplace=in_place)
        self.situacoes_inscricao.drop_duplicates(
            subset=subset, inplace=in_place)
        self.receitas_principais.drop_duplicates(
            subset=subset, inplace=in_place)
        self.tipos_credito.drop_duplicates(subset=subset, inplace=in_place)

        aux_names = [
            "tipo_devedor",
            "entidade_responsavel",
            "unidade",
            "tipo_situacao_inscricao",
            "situacao_inscricao",
            "receita_principal",
            "tipo_credito",
        ]
        attr_names = [
            "tipos_devedor",
            "entidades_responsaveis",
            "unidades",
            "tipos_situacao_inscricao",
            "situacoes_inscricao",
            "receitas_principais",
            "tipos_credito",
        ]
        for index in range(len(aux_names)):
            save_result_file(
                folder_path + "/" + aux_names[index],
                getattr(self, attr_names[index])
            )

    def transform_raw_data(self, selects_path: str, transforms_path: str, selected_dirs_names: List[str]):
        for table_name in selected_dirs_names:
            self._logger.info(f"Transforming {table_name} raw data")

            selected_files_names = []
            get_files_names(selects_path + "/" + table_name,
                            selected_files_names)

            match table_name:
                case "empre":
                    table_full_name = "empresa"
                    create_subfolder(transforms_path + "/" + table_full_name)

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk.drop(['ente_federativo'],
                                       axis=1, inplace=True)
                            chunk = chunk.apply(
                                func=self.transform_empresas, axis=1)

                            save_result_file(
                                transforms_path + "/" + table_full_name +
                                "/" + table_name + str(count),
                                chunk
                            )

                case "estabele":
                    table_full_name = "estabelecimento"
                    create_subfolder(transforms_path + "/" + table_full_name)
                    create_subfolder(transforms_path + "/" + "logradouro")
                    create_subfolder(transforms_path + "/" + "contato")

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk = chunk.apply(
                                func=self.transform_estabelecimentos, axis=1)
                            chunk.drop([
                                "nome_cidade_exterior",
                                "pais",
                                "tipo_logradouro",
                                "numero",
                                "complemento",
                                "bairro",
                                "cep",
                                "estado_uf",
                                "municipio",
                                "ddd_1",
                                "telefone_1",
                                "ddd_2",
                                "telefone_2",
                                "ddd_fax",
                                "fax",
                                "email",
                            ], axis=1, inplace=True)

                            save_result_file(
                                transforms_path + "/" + table_full_name +
                                "/" + table_full_name + str(count),
                                chunk
                            )
                            self.transform_logradouros(
                                transforms_path, "logradouro", count)
                            self.transform_contatos(
                                transforms_path, "contato", count)

                case "socio":
                    create_subfolder(transforms_path + "/" + table_name)
                    create_subfolder(transforms_path + "/" + "representante")

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk = chunk.apply(
                                func=self.transform_socios, axis=1)
                            chunk.drop([
                                'identificador',
                                'qualificacao_representante',
                                'nome_representante'
                            ], axis=1, inplace=True)

                            save_result_file(
                                transforms_path + "/" + table_name +
                                "/" + table_name + str(count),
                                chunk
                            )
                            self.transform_representantes(
                                transforms_path, "representante", count)

                case "simples":
                    create_subfolder(transforms_path + "/" + table_name)

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk.drop([
                                'opcao_simples',
                                'opcao_mei',
                                'data_opcao_mei',
                                'data_exclusao_mei',
                            ], axis=1, inplace=True)
                            chunk = chunk.apply(
                                func=self.transform_simples, axis=1)

                            save_result_file(
                                transforms_path + "/" + table_name +
                                "/" + table_name + str(count),
                                chunk
                            )

                case "fgts":
                    create_subfolder(transforms_path + "/" + table_name)

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk.drop(
                                ['tipo_pessoa', 'nome_devedor'], axis=1, inplace=True)
                            chunk = chunk.apply(
                                func=self.transform_fgts, axis=1)

                            save_result_file(
                                transforms_path + "/" + table_name +
                                "/" + table_name + str(count),
                                chunk
                            )

                case "prev":
                    table_full_name = "previdenciario"
                    create_subfolder(transforms_path + "/" + table_full_name)

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk.drop(
                                ['tipo_pessoa', 'nome_devedor'], axis=1, inplace=True)
                            chunk = chunk.apply(
                                func=self.transform_prev, axis=1)

                            save_result_file(
                                transforms_path + "/" + table_full_name +
                                "/" + table_full_name + str(count),
                                chunk
                            )

                case "sida":
                    create_subfolder(transforms_path + "/" + table_name)

                    count = 0
                    for file_name in selected_files_names:
                        file_full_path = selects_path + "/" + table_name + "/" + file_name
                        table_reader = get_csv_reader(
                            file_full_path,
                            self.table_chunk_size
                        )
                        for chunk in table_reader:
                            count += 1

                            chunk.drop(
                                ['tipo_pessoa', 'nome_devedor'], axis=1, inplace=True)
                            chunk = chunk.apply(
                                func=self.transform_sida, axis=1)

                            save_result_file(
                                transforms_path + "/" + table_name +
                                "/" + table_name + str(count),
                                chunk
                            )

                case _:
                    continue

        self.transform_aux_trib_data(transforms_path, "aux_trib")

    def start(self, selects_path: str, transforms_path: str):
        self._logger.debug("Starting DataTransformer")

        selected_dirs_names = []
        count = 0
        while True:
            if count > 2:
                self._logger.debug(f"Breaking loop. Count: {count}")
                break

            get_dirs_names(selects_path, selected_dirs_names)

            if len(selected_dirs_names) == 0:
                count += 1
                sleep(5)
            else:
                self._logger.debug(
                    f"Selected dirs names: {selected_dirs_names}")
                create_subfolder(transforms_path)
                self.transform_raw_data(
                    selects_path, transforms_path, selected_dirs_names)
                break

        self._logger.debug("Terminating DataTransformer")
