# ### Built-in deps
from typing import Any, Dict, List, Optional, Union

# ### Third-party deps
from pydantic import BaseSettings, PostgresDsn, validator

# ### Local deps


class Settings(BaseSettings):
    # ENVIRONMENT
    APP_NAME: str
    ENV: str

    # SERVER
    HOST: str
    PORT: int
    RELOAD: bool
    ROOT_PATH: Optional[str] = None
    N_WORKERS: int
    BACKEND_CORS_ORIGINS: List[str]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, value: Union[str, List[str]]
    ) -> Union[List[str], str]:

        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]

        elif isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    # DATABASE
    SQLALCHEMY_AUTOINIT: bool

    POSTGRES_SCHEME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_URI: Optional[PostgresDsn] = None

    @validator("POSTGRES_URI", pre=True)
    def assemble_db_connection(
        cls, value: Optional[str], values: Dict[str, Any]
    ) -> Any:

        if isinstance(value, str):
            return value

        return str(
            PostgresDsn.build(
                scheme=values.get("POSTGRES_SCHEME"),
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_HOST"),
                port=values.get("POSTGRES_PORT"),
                path=f"/{values.get('POSTGRES_DB') or ''}",
            )
        )

    # STORAGE
    RECEITA_FEDERAL_DATA_MAIN_URL: str
    RECEITA_FEDERAL_MAIN_UPDATE_FIELD: str
    RECEITA_FEDERAL_DATA_REPOSITORY_URL: str
    RECEITA_FEDERAL_DATA_TRIB_URL: str

    DOWNLOADS_FOLDER_PATH: str
    EXTRACTS_FOLDER_PATH: str
    SELECTS_FOLDER_PATH: str
    TRANSFORMS_FOLDER_PATH: str
    AUX_FILES_PATH: str
    FILES_TO_FILTER_CONFIG_PATH: str
    FILES_TO_DOWNLOAD_CONFIG_PATH: str

    TABLES_CHUNKSIZE: int = 8192
    FORCE_DOWNLOAD: bool = False
    EXTRACT_DATA: bool = False
    FILTER_DATA: bool = False
    TRANSFORM_DATA: bool = False
    POPULATE_DB: bool = False
    RESET_DB: bool = False

    # SECURITY
    X_KEY: str

    # LOGGING
    LOGGER_NAME: str
    LOG_DIR: str
    LOG_LEVEL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_app_config():
    return Settings()
