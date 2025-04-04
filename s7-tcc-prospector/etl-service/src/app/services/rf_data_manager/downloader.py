# ### Built-in deps
from typing import Any, Dict, List
from io import BytesIO
from datetime import datetime

# ### Third-party deps
import requests

# ### Local deps
from app.helpers import Logger
from app.utils.files_manip import create_subfolder


class DataDownloader:
    def __init__(self, files_to_download: Dict[str, Any]) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing DataDownloader")

        self._files_names: List[str] = files_to_download['files']

        self._logger.debug(f"Files to download: {self._files_names}")

    def find_last_upload_directory(self, rf_data_url: str, base_year: str, substr_len: int):
        self._logger.debug(
            f"Searching for last upload directory at {rf_data_url}")

        count = 0
        response = None

        while count != 3:
            self._logger.debug(f"Search attempt {count + 1}")

            try:
                response = requests.get(
                    rf_data_url,
                    headers={
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
                    }
                )
            except Exception as err:
                self._logger.warning(
                    f"Last upload directory not found: {rf_data_url}")
                self._logger.debug(f"Error: {err}")

            if response and response.ok:
                break

            count += 1

        if count == 3:
            return None

        lines = response.text.split('<a href="')
        lines.reverse()

        for line in lines:
            full_date = line[:substr_len]
            if base_year in full_date:
                self._logger.debug(f"Last upload directory: {full_date}/")
                return full_date

    def download_file(self, rf_data_url: str, file_name: str):
        self._logger.info(f"Downloading file {file_name}")

        file_url = rf_data_url + '/' + file_name
        self._logger.debug(file_url)

        count = 0
        response = None

        while count != 3:
            self._logger.debug(f"Download attempt {count + 1}")

            try:
                response = requests.get(
                    file_url,
                    headers={
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
                    }
                )
            except Exception as err:
                self._logger.warning(
                    f"Failed download attempt with {file_url}")
                self._logger.debug(f"Error while download attempt: {err}")

            if response and response.ok:
                break

            count += 1

        if count == 3:
            self._logger.warning(f"Couldn't download {file_name}")
            return None

        self._logger.debug(f"{file_name} downloaded")
        return BytesIO(response.content)

    def save_file(self, downloads_path: str, file: BytesIO, file_name: str):
        with open(downloads_path + '/' + file_name, "wb") as file_to_save:
            file_to_save.write(file.read())

    def start(self, rf_data_repo_url: str, rf_trib_repo_url: str, downloads_path: str):
        self._logger.info("Starting DataDownloader")

        this_year = datetime.now().year
        last_upload_dir_name = self.find_last_upload_directory(
            rf_data_repo_url + "/", str(this_year), 7)

        last_tri_dir_name = self.find_last_upload_directory(
            rf_trib_repo_url, str(this_year) + '_trimestre_', 17)
        if last_tri_dir_name is None:
            last_tri_dir_name = self.find_last_upload_directory(
                rf_trib_repo_url, str(this_year - 1) + '_trimestre_', 17)

        file_extension = "zip"

        for file_name in self._files_names:
            downloaded_file = None
            temp_file_name = file_name + '.' + file_extension

            if 'Dados' not in file_name and last_upload_dir_name:
                temp_url = rf_data_repo_url + "/" + last_upload_dir_name

            elif last_tri_dir_name:
                temp_url = rf_trib_repo_url + "/" + last_tri_dir_name
            else:
                continue

            downloaded_file = self.download_file(temp_url, temp_file_name)

            if downloaded_file:
                create_subfolder(downloads_path)
                self.save_file(downloads_path, downloaded_file, temp_file_name)

        if last_upload_dir_name is None and last_tri_dir_name is None:
            self._logger.warning("Could not download receita federal data")

        self._logger.info("Terminating DataDownloader")
