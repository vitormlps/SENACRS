# ### Built-in deps
from typing import List
import os

# ### Third-party deps
import pandas as pd

# ### Local deps


def save_result_file(table_name: str, table: pd.DataFrame):
    return table.to_csv(
        path_or_buf=table_name,
        sep=";",
        index=False,
        encoding="latin-1",
    )


def get_csv_reader(file_path: str, chunksize: int = 8192):
    return pd.read_csv(
        filepath_or_buffer=file_path,
        sep=";",
        header=0,
        keep_default_na=False,
        dtype='object',
        chunksize=chunksize,
        encoding="latin-1",
        engine="c"
    )


def create_subfolder(path: str):
    os.makedirs(path, exist_ok=True)


def clean_folder(path: str):
    with os.scandir(path) as files:
        for temp_file in files:
            os.remove(temp_file.path)


def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)


def get_files_names(path: str, list_to_populate: List[str]):
    with os.scandir(path) as files:
        for temp_file in files:
            list_to_populate.append(temp_file.name)


def get_dirs_names(path: str, list_to_populate: List[str]):
    return get_files_names(path, list_to_populate)
