# ### Built-in deps
from typing import Any, Dict, Set, List
import warnings
from time import sleep

# ### Third-party deps
import pandas as pd

# ### Local deps
from app.helpers import Logger
from app.utils.files_manip import (
    save_result_file,
    get_csv_reader,
    create_subfolder,
    get_files_names,
    delete_file
)

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(
    action='ignore', category=pd.errors.SettingWithCopyWarning)
pd.set_option('display.max_columns', None)


class DataSelector:
    def __init__(
        self,
        filter_parameters: Dict[str, Any],
        aux_files: Dict[str, Any],
        tables_chunksize: int
    ) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing DataSelector")

        self.table_chunk_size = tables_chunksize
        self.filter_parameters = filter_parameters
        self.last_files_index = {}
        self.aux_files = aux_files
        self.aux_table = pd.DataFrame()
        self.aux_name: str = ""
        self.simples_cnpjs = set()

    def get_dirs_names(self, path: str, list_to_populate: List[str]):
        list_to_populate.extend(
            ["estabele", "simples", "empre", "prev", "fgts", "sida", "socio"])

    def normalize_id(self, row):
        row.loc["id"] = str(row.loc["id"]).split("/")[0].replace(".", "")
        return row

    def select_by_query(self, table: pd.DataFrame, to_save: Dict):
        query_str = ""
        for key, values in to_save.items():
            if len(values) == 0:
                continue

            words = ""
            for word in values:
                words += f"'{word}', "

            if len(values) != 1:
                query_str += f"{key} in ({words[:-2]}) & "
            else:
                query_str += f"{key} == {words[:-2]} & "

        if len(query_str) > 0:
            table = table.query(query_str[:-2])

        return table

    def filter_data_by_parameters(self, table_name: str, table: pd.DataFrame, cnpjs: Set):
        to_save = self.filter_parameters.get(table_name)

        match table_name:
            case "estabele":
                table.drop(table.loc[table["municipio"]
                           == "7107"].index, inplace=True)
                table.drop(table.loc[table["municipio"]
                           == "6001"].index, inplace=True)

                table = self.select_by_query(table, to_save)
                cnpjs.update(table["id"].unique())

            case "empre":
                table = table.merge(pd.DataFrame(
                    cnpjs, columns=["id"]), on=["id"])
                table = self.select_by_query(table, to_save)

            case "socio":
                table = table.merge(pd.DataFrame(
                    cnpjs, columns=["id"]), on=["id"])
                table = self.select_by_query(table, to_save)

            case "simples":
                table = table.merge(pd.DataFrame(
                    cnpjs, columns=["id"]), on=["id"])
                table = self.select_by_query(table, to_save)

                self.simples_cnpjs.update(table["id"].unique())

            case _:
                table.drop(table.loc[table["id"].str.contains(
                    "XXX")].index, inplace=True)
                table = table.apply(func=self.normalize_id, axis=1)
                table = table.merge(pd.DataFrame(
                    cnpjs, columns=["id"]), on=["id"])
                table = self.select_by_query(table, to_save)

        return table

    def select_raw_data(self, extracts_path: str, selects_path: str, extracted_dirs_names: List[str], cnpjs: Set):
        for table_name in extracted_dirs_names:
            self._logger.info(f"Selecting {table_name} raw data")
            create_subfolder(selects_path + "/" + table_name)

            last_index = self.last_files_index.get(table_name)
            if last_index is None:
                self.last_files_index[table_name] = 0

            if self.aux_name == "":
                self.aux_name = table_name

            if self.aux_name != table_name:
                self.last_files_index[self.aux_name] += 1
                if len(self.aux_table) > 0:
                    save_result_file(
                        selects_path + "/" + self.aux_name + "/" + self.aux_name +
                        str(self.last_files_index[self.aux_name]),
                        self.aux_table
                    )
                self.aux_name = table_name
                self.aux_table = pd.DataFrame()

            extracted_files_names = []
            get_files_names(extracts_path + "/" + table_name,
                            extracted_files_names)

            for file_name in extracted_files_names:
                file_full_path = extracts_path + "/" + table_name + "/" + file_name

                table_reader = get_csv_reader(
                    file_full_path, self.table_chunk_size)

                for chunk in table_reader:
                    filtered_table = self.filter_data_by_parameters(
                        table_name, chunk, cnpjs)
                    self.aux_table = pd.concat(
                        [filtered_table, self.aux_table])

                    if len(self.aux_table) >= self.table_chunk_size:
                        self.last_files_index[table_name] += 1

                        save_result_file(
                            selects_path + "/" + table_name + "/" + table_name +
                            str(self.last_files_index[table_name]),
                            self.aux_table
                        )
                        self.aux_table = pd.DataFrame()

            if table_name == "simples":
                self._logger.debug(
                    f"Cleaning estabele | simples cnpj len: {len(self.simples_cnpjs)} | cnpjs len {len(cnpjs)}")

                self.last_files_index["estabele"] = 0
                temp_estabele = pd.DataFrame()

                cnpjs.intersection_update(self.simples_cnpjs)
                self.simples_cnpjs.clear()

                estabele_files_names = []
                path = selects_path + "/estabele"
                get_files_names(path, estabele_files_names)

                for file_name in estabele_files_names:
                    table_reader = get_csv_reader(
                        path + "/" + file_name,
                        self.table_chunk_size
                    )
                    for chunk in table_reader:
                        filtered_table = chunk.merge(
                            pd.DataFrame(cnpjs, columns=["id"]), on=["id"])
                        temp_estabele = pd.concat(
                            [filtered_table, temp_estabele])

                        if len(temp_estabele) >= self.table_chunk_size:
                            self.last_files_index["estabele"] += 1
                            save_result_file(
                                path + "/estabele" +
                                str(self.last_files_index["estabele"]),
                                temp_estabele
                            )
                            temp_estabele = pd.DataFrame()

                if len(temp_estabele) > 0:
                    self.last_files_index["estabele"] += 1
                    save_result_file(
                        path + "/estabele" +
                        str(self.last_files_index["estabele"]),
                        temp_estabele
                    )

                for index in range(len(estabele_files_names) + self.last_files_index['estabele']):
                    if index > self.last_files_index["estabele"]:
                        self._logger.debug(f"Deleting file estabele{index}")
                        delete_file(path + "/estabele" + str(index))

                self._logger.debug(f"New cnpjs len {len(cnpjs)}")

        if len(self.aux_table) > 0:
            self.last_files_index[self.aux_name] += 1
            save_result_file(
                selects_path + "/" + self.aux_name + "/" + self.aux_name +
                str(self.last_files_index[self.aux_name]),
                self.aux_table
            )

    def start(self, extracts_path: str, selects_path: str, cnpjs: Set):
        self._logger.debug("Starting DataSelector")

        extracted_dirs_names = []
        count = 0
        while True:
            if count > 2:
                self._logger.debug(f"Breaking loop. Count: {count}")
                break

            self.get_dirs_names(extracts_path, extracted_dirs_names)

            if len(extracted_dirs_names) == 0:
                count += 1
                sleep(5)
            else:
                self._logger.debug(
                    f"Extracted dirs names: {extracted_dirs_names}")
                create_subfolder(selects_path)
                self.select_raw_data(
                    extracts_path, selects_path, extracted_dirs_names, cnpjs)
                break

        self._logger.debug("Terminating DataSelector")
