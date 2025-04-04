# ### Built-in deps
from typing import Dict, List
from datetime import datetime
from time import sleep

# ### Third-party deps
import pandas as pd

# ### Local deps
from app.helpers import Logger
from app.database.connection import get_db_local_session, get_db_engine
from app.entities.cnaes.repository import cnaes_repo
from app.entities.motivos.repository import motivos_repo
from app.entities.municipios.repository import municipios_repo
from app.entities.paises.repository import paises_repo
from app.entities.naturezas_juridicas.repository import naturezas_juridicas_repo
from app.entities.qualificacoes.repository import qualificacoes_repo
from app.entities.matrizes_filiais.repository import matrizes_filiais_repo
from app.entities.portes_empresas.repository import portes_empresas_repo
from app.entities.faixas_etarias.repository import faixas_etarias_repo
from app.entities.situacoes_cadastrais.repository import situacoes_cadastrais_repo
from app.entities.base.dtypes import dtypes
from app.utils.files_manip import get_files_names, get_dirs_names


pd.set_option('display.max_columns', None)


class DBPopulator:
    def __init__(self, aux_files_path: str, tables_chunksize: int) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing DBPopulate")

        self.aux_files_path = aux_files_path
        self.table_chunk_size = tables_chunksize

    def to_sql(self, table_name: str, table: pd.DataFrame, dtypes: Dict, connection):
        try:
            table.to_sql(
                con=connection,
                name=table_name,
                dtype=dtypes,
                index=False,
                if_exists="append",
                method="multi",
            )
        except Exception as err:
            self._logger.debug(str(err)[:400])
            self._logger.error(f"Couldn't insert {table_name}")
            self._logger.debug(f"\n{table}")

    def get_csv_reader(self, file_path: str, chunksize: int = 8192):
        return pd.read_csv(
            filepath_or_buffer=file_path,
            sep=";",
            header=0,
            dtype='object',
            na_filter=False,
            chunksize=chunksize,
            encoding="latin-1",
            engine="c"
        )

    def _close_session(self):
        self._logger.debug("Closing session")

        session = get_db_local_session()
        session.close()

    def _insert_matrizes_filiais(self):
        table = [
            ["01", "Matriz"],
            ["02", "Filial"],
        ]
        repo = matrizes_filiais_repo()

        count = repo.count()
        if count != len(table):
            for row in table:
                repo.create(
                    {
                        "id": row[0],
                        "descricao": row[1],
                    }
                )

    def _insert_situacoes_cadastrais(self):
        table = [
            ["01", "Nula"],
            ["02", "Ativa"],
            ["03", "Suspensa"],
            ["04", "Inapta"],
            ["05", "-"],
            ["06", "-"],
            ["07", "-"],
            ["08", "Baixada"],
        ]
        repo = situacoes_cadastrais_repo()

        count = repo.count()
        if count != len(table):
            for row in table:
                repo.create(
                    {
                        "id": row[0],
                        "descricao": row[1],
                    }
                )

    def _insert_portes_empresas(self):
        table = [
            ["01", "Não informado"],
            ["02", "Micro Empresa"],
            ["03", "Empresa de Pequeno Porte"],
            ["04", "-"],
            ["05", "Demais"],
        ]
        repo = portes_empresas_repo()

        count = repo.count()
        if count != len(table):
            for row in table:
                repo.create(
                    {
                        "id": row[0],
                        "descricao": row[1],
                    }
                )

    def _insert_faixas_etarias(self):
        table = [
            ["01", "0 a 12"],
            ["02", "13 a 20"],
            ["03", "21 a 30"],
            ["04", "31 a 40"],
            ["05", "41 a 50"],
            ["06", "51 a 60"],
            ["07", "61 a 70"],
            ["08", "71 a 80"],
            ["09", "81+"],
        ]
        repo = faixas_etarias_repo()

        count = repo.count()
        if count != len(table):
            for row in table:
                repo.create(
                    {
                        "id": row[0],
                        "descricao": row[1],
                    }
                )

    def get_base_columns(self, row):
        now = datetime.now()

        row.loc["created_at"] = now
        row.loc["updated_at"] = now

        return row

    def get_structure_with_descricao(self, table: pd.DataFrame):
        table = table.rename(columns={
            0: "id",
            1: "descricao",
            2: "created_at",
            3: "updated_at"
        })
        table = table.apply(func=self.get_base_columns, axis=1)
        return table, dtypes["aux_tables"]["sql"]

    def _insert_cnae(self, table_name, table: pd.DataFrame, db_engine):
        repo = cnaes_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def _insert_motivo(self, table_name, table: pd.DataFrame, db_engine):
        repo = motivos_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def _insert_natureza_juridica(self, table_name, table: pd.DataFrame, db_engine):
        repo = naturezas_juridicas_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def _insert_qualificacao(self, table_name, table: pd.DataFrame, db_engine):
        repo = qualificacoes_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def _insert_pais(self, table_name, table: pd.DataFrame, db_engine):
        repo = paises_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def _insert_municipio(self, table_name, table: pd.DataFrame, db_engine):
        repo = municipios_repo()
        count = repo.count()

        if count != len(table):
            table, dtypes = self.get_structure_with_descricao(table)
            self.to_sql(table_name, table, dtypes, db_engine)

    def insert_aux_tables(self, db_engine):
        aux_tables = [
            "cnae",
            "motivo",
            "natureza_juridica",
            "qualificacao",
            "pais",
            "municipio",
        ]
        for table_name in aux_tables:
            self._logger.debug(f"Inserting {table_name}")

            table = pd.read_csv(
                filepath_or_buffer=self.aux_files_path + "/" + table_name + ".csv",
                sep=";",
                skiprows=0,
                header=None,
                keep_default_na=False,
                dtype='object',
                encoding="latin-1",
                engine="c"
            )
            insert_method = self.__getattribute__(f"_insert_{table_name}")
            insert_method(table_name, table, db_engine)

    def insert_aux_trib_tables(self, transforms_path: str, db_engine):
        folder_path = transforms_path + "/aux_trib"
        aux_trib_files_names = []
        get_files_names(folder_path, aux_trib_files_names)

        for file_name in aux_trib_files_names:
            self._logger.debug(f"Inserting {file_name}")

            table_reader = self.get_csv_reader(
                folder_path + "/" + file_name,
                self.table_chunk_size
            )

            for chunk in table_reader:
                self.to_sql(file_name, chunk,
                            dtypes["aux_tables"]["sql"], db_engine)

    def insert_extra_tables(self):
        extra_tables = [
            "matrizes_filiais",
            "situacoes_cadastrais",
            "portes_empresas",
            "faixas_etarias",
        ]
        for table_name in extra_tables:
            self._logger.debug(f"Inserting {table_name}")

            insert_method = self.__getattribute__(f"_insert_{table_name}")
            insert_method()

    def insert_data(self, transforms_path: str, transformed_dirs_names: List[str], db_engine):
        for table_name in transformed_dirs_names:
            self._logger.debug(f"Inserting {table_name} data into database")

            table_dtypes = dtypes[table_name]
            transformed_files_names = []
            get_files_names(transforms_path + "/" + table_name,
                            transformed_files_names)

            self._logger.debug(transformed_files_names)

            for file_name in transformed_files_names:
                self._logger.debug(f"Inserting {file_name}")

                table_reader = self.get_csv_reader(
                    transforms_path + "/" + table_name + "/" + file_name,
                    self.table_chunk_size
                )

                for chunk in table_reader:
                    chunk = chunk.astype(table_dtypes["pd"])
                    self.to_sql(table_name, chunk,
                                table_dtypes["sql"], db_engine)

        self._close_session()

    def start(self, transforms_path: str):
        self._logger.debug("Starting DBPopulator")

        db_engine = get_db_engine()
        self.insert_extra_tables()
        self.insert_aux_tables(db_engine)
        self.insert_aux_trib_tables(transforms_path, db_engine)

        transformed_dirs_names = []
        count = 0
        while True:
            if count > 2:
                self._logger.debug(f"Breaking loop. Count: {count}")
                break

            get_dirs_names(transforms_path, transformed_dirs_names)
            transformed_dirs_names.remove("aux_trib")

            if len(transformed_dirs_names) == 0:
                count += 1
                sleep(5)
            else:
                self._logger.debug(
                    f"Transformed dirs names: {transformed_dirs_names}")
                self.insert_data(
                    transforms_path, transformed_dirs_names, db_engine)
                break

        self._logger.debug("Terminating DBPopulator")
