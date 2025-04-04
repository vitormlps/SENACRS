# ### Built-in deps
from typing import List
from io import BytesIO
from time import sleep

# ### Third-party deps
import zipfile
from pandas import read_csv, DataFrame

# ### Local deps
from app.helpers import Logger
from app.utils.files_manip import (
    save_result_file,
    create_subfolder,
    get_files_names,
)


class DataExtractor:
    def __init__(self, tables_chunksize: int) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing DataExtractor")

        self.last_files_index = {}
        self.table_chunk_size = tables_chunksize

    def organize_data(self, table_name: str, table: DataFrame):
        match table_name:
            case "empre":
                return table.rename(columns={
                    0: "id",
                    1: "razao_social",
                    2: "natureza_juridica",
                    3: "qualificacao_responsavel",
                    4: "capital_social",
                    5: "porte_empresa",
                    6: "ente_federativo",
                })
            case "estabele":
                return table.rename(columns={
                    0: "id",
                    1: "cnpj_ordem",
                    2: "cnpj_digit_verif",
                    3: "matriz_filial",
                    4: "nome_fantasia",
                    5: "situacao_cadastral",
                    6: "data_situacao_cadastral",
                    7: "motivo",
                    8: "nome_cidade_exterior",
                    9: "pais",
                    10: "data_inicio_atividade",
                    11: "cnae_principal",
                    12: "cnaes_secundarios",
                    13: "tipo_logradouro",
                    14: "logradouro",
                    15: "numero",
                    16: "complemento",
                    17: "bairro",
                    18: "cep",
                    19: "estado_uf",
                    20: "municipio",
                    21: "ddd_1",
                    22: "telefone_1",
                    23: "ddd_2",
                    24: "telefone_2",
                    25: "ddd_fax",
                    26: "fax",
                    27: "email",
                    28: "situacao_especial",
                    29: "data_situacao_especial",
                    30: "cnpj_base"
                })
            case "socio":
                return table.rename(columns={
                    0: "id",
                    1: "identificador",
                    2: "nome",
                    3: "cpf_cnpj",
                    4: "qualificacao",
                    5: "data_entrada_sociedade",
                    6: "pais",
                    7: "representante_legal",
                    8: "nome_representante",
                    9: "qualificacao_representante",
                    10: "faixa_etaria",
                    11: "cnpj_base"
                })
            case "simples":
                return table.rename(columns={
                    0: "id",
                    1: "opcao_simples",
                    2: "data_opcao",
                    3: "data_exclusao",
                    4: "opcao_mei",
                    5: "data_opcao_mei",
                    6: "data_exclusao_mei",
                })
            case "fgts":
                return table.rename(columns={
                    0: "id",
                    1: "tipo_pessoa",
                    2: "tipo_devedor",
                    3: "nome_devedor",
                    4: "uf_devedor",
                    5: "unidade_responsavel",
                    6: "entidade_responsavel",
                    7: "unidade_inscricao",
                    8: "numero_inscricao",
                    9: "tipo_situacao_inscricao",
                    10: "situacao_inscricao",
                    11: "receita_principal",
                    12: "data_inscricao",
                    13: "indicador_ajuizado",
                    14: "valor_consolidado",
                    15: "cnpj_base"
                })
            case "sida":
                return table.rename(columns={
                    0: "id",
                    1: "tipo_pessoa",
                    2: "tipo_devedor",
                    3: "nome_devedor",
                    4: "uf_devedor",
                    5: "unidade_responsavel",
                    6: "numero_inscricao",
                    7: "tipo_situacao_inscricao",
                    8: "situacao_inscricao",
                    9: "receita_principal",
                    10: "data_inscricao",
                    11: "indicador_ajuizado",
                    12: "valor_consolidado",
                    13: "cnpj_base"
                })
            case "prev":
                return table.rename(columns={
                    0: "id",
                    1: "tipo_pessoa",
                    2: "tipo_devedor",
                    3: "nome_devedor",
                    4: "uf_devedor",
                    5: "unidade_responsavel",
                    6: "numero_inscricao",
                    7: "tipo_situacao_inscricao",
                    8: "situacao_inscricao",
                    9: "tipo_credito",
                    10: "data_inscricao",
                    11: "indicador_ajuizado",
                    12: "valor_consolidado",
                    13: "cnpj_base"
                })
            case _:
                return table.rename(columns={
                    0: "id",
                    1: "descricao",
                })

    def get_csv_reader(self, file: BytesIO, skiprows: int = 0, chunksize: int = 8192):
        self._logger.debug("Opening unzipped file")

        return read_csv(
            filepath_or_buffer=file,
            sep=";",
            skiprows=skiprows,
            header=None,
            keep_default_na=False,
            dtype='object',
            chunksize=chunksize,
            encoding="latin-1",
            engine="c"
        )

    def unzip_file(self, file: BytesIO):
        self._logger.debug("Uzipping loaded file")
        result_file = None

        try:
            result_file = zipfile.ZipFile(file, 'r')
        except Exception as err:
            self._logger.warning("Error unzipping file")
            self._logger.debug(err)

        return result_file

    def load_file(self, path: str, file_name: str):
        self._logger.debug("Loading file to extract")
        result_file = None

        try:
            with open(path + '/' + file_name, "rb") as file:
                result_file = BytesIO(file.read())

        except Exception as err:
            self._logger.warning("Error loading file")
            self._logger.debug(err)

        return result_file

    def extract_files(self, downloads_path: str, extracts_path: str, downloaded_files_names: List):
        for file_name in downloaded_files_names:
            self._logger.debug(f"Extracting {file_name} downloaded file")

            loaded_file = self.load_file(downloads_path, file_name)
            if loaded_file is None:
                continue

            zip_ref = self.unzip_file(loaded_file)
            if zip_ref is None:
                continue

            table_reader = None

            for file in zip_ref.filelist:
                file_to_read = zip_ref.open(file)

                if "arquivo_lai" in file.filename:
                    name_parts = file.filename.split("_")
                    table_name = name_parts[2].lower()
                    skiprows = 1

                else:
                    name_parts = file.filename.split(".")
                    if "SIMPLES" in name_parts:
                        temp_name = name_parts[2]
                    else:
                        temp_name = name_parts[-1]

                    table_name = temp_name.replace("CSV", "").lower()
                    skiprows = 0

                table_reader = self.get_csv_reader(
                    file_to_read, skiprows, self.table_chunk_size)

                create_subfolder(extracts_path + "/" + table_name)
                last_index = self.last_files_index.get(table_name)
                if last_index is None:
                    self.last_files_index[table_name] = 0

                self._logger.info(f"Extracting {table_name} file")
                for chunk in table_reader:
                    table_chunk = self.organize_data(table_name, chunk)

                    self.last_files_index[table_name] += 1
                    save_result_file(
                        extracts_path + "/" + table_name + "/" + table_name +
                        str(self.last_files_index[table_name]),
                        table_chunk
                    )

    def start(self, downloads_path: str, extracts_path: str):
        self._logger.info("Starting DataExtractor")

        downloaded_files_names = []
        count = 0
        while True:
            if count > 2:
                self._logger.debug(f"Breaking loop. Count: {count}")
                break

            get_files_names(downloads_path, downloaded_files_names)

            if len(downloaded_files_names) == 0:
                count += 1
                sleep(5)
            else:
                create_subfolder(extracts_path)
                self.extract_files(
                    downloads_path, extracts_path, downloaded_files_names)
                break

        self._logger.info("Terminating DataExtractor")
