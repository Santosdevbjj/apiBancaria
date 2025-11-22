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

Este projeto implementa uma **API RESTful** para gerenciamento de **operações bancárias** (depósito, saque e extratos), desenvolvida em **Python** com o framework assíncrono **FastAPI** e banco de dados **PostgreSQL**.  
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
```



2️⃣ **Inicializar com Docker Compose**

Na raiz do projeto, execute:

docker-compose up --build -d

O Compose irá:

Construir a imagem da API

Subir o container do PostgreSQL

Executar as migrações Alembic (alembic upgrade head)

Iniciar o servidor Uvicorn/FastAPI



---

3️⃣ **Acessar a API**

Após alguns segundos, a API estará disponível:

Recurso	URL	Descrição

🌐 Raiz	http://localhost:8000/	Confirma se a API está online
📘 Swagger UI	http://localhost:8000/docs	Interface interativa para testar endpoints
📕 ReDoc	http://localhost:8000/redoc	Documentação alternativa estilizada



---

4️⃣ **Primeiros Passos (Testes Rápidos)**

1. **Registrar Usuário**
POST /api/v1/users/register


2. **Login**
POST /api/v1/users/login → retorna access_token


3. **Depósito ou Saque**
POST /api/v1/transactions/process
Headers:

Authorization: Bearer <access_token>


4. **Extrato Bancário**
GET /api/v1/transactions/statement




---

5️⃣ **Parar os Serviços**

Para encerrar e remover os contêineres:

docker-compose down

Para remover também o volume de dados:

docker-compose down -v


---

🧪 **Tecnologias Utilizadas**

**FastAPI** — Framework web moderno e assíncrono para APIs em Python

**PostgreSQL** — Banco de dados relacional robusto

**SQLAlchemy Async** — ORM para acesso ao banco assíncrono

**Alembic** — Migrações de banco de dados

**Docker** — Contêineres para ambiente consistente

**JWT** — Autenticação segura via tokens



---

📜 **Licença**

Este projeto está licenciado sob a MIT License.


---

🤝 **Contribuição**

Sinta-se à vontade para abrir Issues e enviar Pull Requests.
Contribuições são bem-vindas para evoluir esta API!


---

👨‍💻 **Autor**

Sérgio Santos
Profissional de TI com expertise em desenvolvimento de sistemas, infraestrutura e segurança.



---

> 💡 Este repositório serve como base para estudos avançados de desenvolvimento backend com Python, arquitetura limpa e práticas modernas de API.

---

**Contato:**


[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 

---

