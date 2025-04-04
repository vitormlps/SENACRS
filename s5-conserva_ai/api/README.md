# Conserva.ai Back-End

API de serviços e comunicação para a plataforma web.

# Instalação

## Variáveis de Ambiente

Primeiro, ajuste as variáveis de ambiente.

PROJECT_NAME: nome do projeto
VERSION: versão do projeto

ENV: tipo do ambiente (desenvolvimento ou produção)
PORT: porta de acesso
HOST: IP de acesso
NETWORK: rede na qual a api está conectado
DEBUG: se está em teste ou não (verdadeiro ou falso)

DB_USER: username do banco de dados
DB_PASSWORD: senha do banco de dados
DB_HOST: nome do servidor do banco de dados
DB_PORT: porta de acesso ao banco de dados
DB_NAME: nome do banco de dados
DATABASE_URI: URI de acesso ao banco de dados

## Docker

Caso tenha docker instalado localmente, basta executar o comando abaixo para rodar o projeto.

```bash
docker compose up
```

Caso o contrário, siga as instruções abaixo.

## Rodando localmente

Primeiro, execute o comando abaixo para instalar as dependências do projeto.

```bash
npm install -f
```

Após, execute o comando abaixo para rodar o projeto.

```bash
npm start
```

## Stack utilizada

**Back-end:** JavaScript

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
