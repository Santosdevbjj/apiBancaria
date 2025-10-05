## Criando sua API Bancária Assíncrona com FastAPI

![PythonDeveloper](https://github.com/user-attachments/assets/e5aca747-cdd0-49cb-9b55-4790d5e605ef)


**Formação Python Backend Developer.**


---

# 🏦 API Bancária Assíncrona com FastAPI e PostgreSQL

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-important)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Este projeto implementa uma **API RESTful de nível sênior** para gerenciamento de **operações bancárias** (depósito, saque e extratos), desenvolvida em **Python** com o framework assíncrono **FastAPI** e banco de dados **PostgreSQL**.  
A autenticação é baseada em **JWT (JSON Web Token)**, garantindo segurança no acesso aos endpoints protegidos.

---

## 🚀 Funcionalidades Principais

- 🔐 **Autenticação Segura**  
  - Cadastro de usuários e login via JWT.  
- 💰 **Transações Bancárias**  
  - Endpoints para **depósitos** e **saques** em contas correntes.  
- ✅ **Validação de Negócios**  
  - Bloqueio de saques por **saldo insuficiente** e rejeição de valores negativos.  
- 📊 **Extrato Completo**  
  - Consulta de **histórico de transações** e **saldo atual**.

---

## 🛠️ Requisitos de Hardware e Software

Para executar localmente com Docker:

### 🧰 Software

| Software         | Versão Mínima | Propósito                                               |
|------------------|---------------|----------------------------------------------------------|
| Docker           | 20.10+        | Empacotamento da aplicação e do banco de dados          |
| Docker Compose   | 2.0+          | Orquestração dos contêineres (API + DB)                 |
| Python           | 3.11+         | Linguagem usada dentro do contêiner                     |
| Acesso à Internet| N/A          | Download de imagens Docker e dependências               |

### 🖥️ Hardware

| Componente   | Requisito Mínimo                          |
|-------------|--------------------------------------------|
| CPU         | Dual-core                                 |
| RAM         | 4 GB (8 GB recomendado para uso com Docker)|
| Disco       | 500 MB livres                             |

---

## 📂 Estrutura do Projeto

A arquitetura segue o princípio de **Separação de Responsabilidades (SOC)**, com camadas bem definidas:

| Caminho | Camada | Descrição |
|---------|--------|-----------|
| `app/main.py` | Entrypoint | Inicializa a aplicação FastAPI e registra o roteador principal. |
| `requirements.txt` | Configuração | Dependências Python (FastAPI, SQLAlchemy, Alembic, etc.). |
| `Dockerfile` | Deploy | Define a imagem da API (Python 3.11 + dependências). |
| `docker-compose.yml` | Deploy | Orquestra API + PostgreSQL. |
| `alembic.ini` | Configuração | Gerenciamento de migrações com Alembic. |
| `app/core/config.py` | Core | Carrega variáveis de ambiente e chaves JWT. |
| `app/core/database.py` | Core | Configura conexão assíncrona com PostgreSQL (SQLAlchemy). |
| `app/core/security.py` | Core | Hash de senhas (bcrypt) e manipulação de JWT. |
| `app/db/base.py` | DB ORM | Base declarativa do SQLAlchemy. |
| `app/db/models.py` | DB ORM | Modelos: User, Account, Transaction. |
| `app/schemas/*.py` | Schemas | Schemas Pydantic de entrada/saída e validações. |
| `app/crud/*.py` | CRUD | Regras de negócio e acesso ao banco. |
| `app/api/v1/api.py` | Rotas | Router principal da API v1. |
| `app/api/v1/endpoints/*.py` | Endpoints | Usuários, Transações e Extrato. |

---

## ⚙️ Guia de Deploy e Execução

### 1️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo (exemplo para desenvolvimento):

```env
# Banco de Dados
POSTGRES_USER=appuser
POSTGRES_PASSWORD=securepassword
POSTGRES_DB=bancodb
POSTGRES_HOST=db

# Segurança JWT
SECRET_KEY="SUA_CHAVE_SECRETA_MUITO_LONGA_E_ALEATORIA"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

---

