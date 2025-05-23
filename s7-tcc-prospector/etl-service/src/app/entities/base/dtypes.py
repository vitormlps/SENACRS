# ### Built-in deps
# ### Third-party deps
from sqlalchemy import String, DateTime, Float, Boolean

# ### Local deps


dtypes = {
    "empresa": {
        "sql": {
            "id": String,
            "razao_social": String,
            "natureza_juridica": String,
            "qualificacao_responsavel": String,
            "capital_social": Float,
            "porte_empresa": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "razao_social": str,
            "natureza_juridica": str,
            "qualificacao_responsavel": str,
            "capital_social": float,
            "porte_empresa": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        },
    },

    "estabelecimento": {
        "sql": {
            "id": String,
            "cnpj_base": String,
            "cnpj_ordem": String,
            "cnpj_digit_verif": String,
            "matriz_filial": String,
            "nome_fantasia": String,
            "situacao_cadastral": String,
            "data_situacao_cadastral": DateTime,
            "motivo": String,
            "data_inicio_atividade": DateTime,
            "cnae_principal": String,
            "cnaes_secundarios": String,
            "logradouro": String,
            "situacao_especial": String,
            "data_situacao_especial": DateTime,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cnpj_base": str,
            "cnpj_ordem": str,
            "cnpj_digit_verif": str,
            "matriz_filial": str,
            "nome_fantasia": str,
            "situacao_cadastral": str,
            "data_situacao_cadastral": 'datetime64[ns]',
            "motivo": str,
            "data_inicio_atividade": 'datetime64[ns]',
            "cnae_principal": str,
            "cnaes_secundarios": str,
            "logradouro": str,
            "situacao_especial": str,
            "data_situacao_especial": 'datetime64[ns]',
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "logradouro": {
        "sql": {
            "id": String,
            "tipo": String,
            "nome": String,
            "numero": String,
            "complemento": String,
            "bairro": String,
            "cep": String,
            "municipio": String,
            "uf": String,
            "nome_cidade_exterior": String,
            "pais": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "tipo": str,
            "nome": str,
            "numero": str,
            "complemento": str,
            "bairro": str,
            "cep": str,
            "municipio": str,
            "uf": str,
            "nome_cidade_exterior": str,
            "pais": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "contato": {
        "sql": {
            "id": String,
            "tipo": String,
            "descricao": String,
            "estabelecimento": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "tipo": str,
            "descricao": str,
            "estabelecimento": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "socio": {
        "sql": {
            "id": String,
            "cnpj_base": String,
            "nome": String,
            "cpf_cnpj": String,
            "qualificacao": String,
            "data_entrada_sociedade": DateTime,
            'representante_legal': String,
            "pais": String,
            "faixa_etaria": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cnpj_base": str,
            "nome": str,
            "cpf_cnpj": str,
            "qualificacao": str,
            "data_entrada_sociedade": 'datetime64[ns]',
            'representante_legal': str,
            "pais": str,
            "faixa_etaria": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "representante": {
        "sql": {
            "id": String,
            "cpf": String,
            "nome": String,
            "qualificacao": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cpf": str,
            "nome": str,
            "qualificacao": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "simples": {
        "sql": {
            "id": String,
            "data_opcao": DateTime,
            "data_exclusao": DateTime,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "data_opcao": 'datetime64[ns]',
            "data_exclusao": 'datetime64[ns]',
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "fgts": {
        "sql": {
            "id": String,
            "cnpj_base": String,
            "tipo_devedor": String,
            "uf_devedor": String,
            "unidade_responsavel": String,
            "entidade_responsavel": String,
            "unidade_inscricao": String,
            "numero_inscricao": String,
            "tipo_situacao_inscricao": String,
            "situacao_inscricao": String,
            "receita_principal": String,
            "data_inscricao": DateTime,
            "indicador_ajuizado": Boolean,
            "valor_consolidado": Float,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cnpj_base": str,
            "tipo_devedor": str,
            "uf_devedor": str,
            "unidade_responsavel": str,
            "entidade_responsavel": str,
            "unidade_inscricao": str,
            "numero_inscricao": str,
            "tipo_situacao_inscricao": str,
            "situacao_inscricao": str,
            "receita_principal": str,
            "data_inscricao": 'datetime64[ns]',
            "indicador_ajuizado": bool,
            "valor_consolidado": float,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "previdenciario": {
        "sql": {
            "id": String,
            "cnpj_base": String,
            "tipo_devedor": String,
            "uf_devedor": String,
            "unidade_responsavel": String,
            "numero_inscricao": String,
            "tipo_situacao_inscricao": String,
            "situacao_inscricao": String,
            "tipo_credito": String,
            "data_inscricao": DateTime,
            "indicador_ajuizado": Boolean,
            "valor_consolidado": Float,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cnpj_base": str,
            "tipo_devedor": str,
            "uf_devedor": str,
            "unidade_responsavel": str,
            "numero_inscricao": str,
            "tipo_situacao_inscricao": str,
            "situacao_inscricao": str,
            "tipo_credito": str,
            "data_inscricao": 'datetime64[ns]',
            "indicador_ajuizado": bool,
            "valor_consolidado": float,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "sida": {
        "sql": {
            "id": String,
            "cnpj_base": String,
            "tipo_devedor": String,
            "uf_devedor": String,
            "unidade_responsavel": String,
            "numero_inscricao": String,
            "tipo_situacao_inscricao": String,
            "situacao_inscricao": String,
            "receita_principal": String,
            "data_inscricao": DateTime,
            "indicador_ajuizado": Boolean,
            "valor_consolidado": Float,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "cnpj_base": str,
            "tipo_devedor": str,
            "uf_devedor": str,
            "unidade_responsavel": str,
            "numero_inscricao": str,
            "tipo_situacao_inscricao": str,
            "situacao_inscricao": str,
            "receita_principal": str,
            "data_inscricao": 'datetime64[ns]',
            "indicador_ajuizado": bool,
            "valor_consolidado": float,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
    "aux_tables": {
        "sql": {
            "id": String,
            "descricao": String,
            "created_at": DateTime,
            "updated_at": DateTime,
        },
        "pd": {
            "id": str,
            "descricao": str,
            "created_at": 'datetime64[ns]',
            "updated_at": 'datetime64[ns]',
        }
    },
}
