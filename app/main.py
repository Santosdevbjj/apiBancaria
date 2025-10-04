# app/main.py

from fastapi import FastAPI
from app.api.v1.api import api_router # Importa o router principal da v1

# Configurações do projeto
from app.core.config import settings

# Inicialização da aplicação FastAPI
# O título e a descrição são cruciais para a documentação automática (Swagger UI/OpenAPI)
app = FastAPI(
    title="API Bancária Assíncrona com FastAPI",
    description="API RESTful para gerenciar operações bancárias de depósitos e saques, utilizando PostgreSQL e autenticação JWT.",
    version="1.0.0",
    openapi_url="/openapi.json", # URL onde a especificação OpenAPI JSON será servida
    docs_url="/docs", # URL para a interface Swagger UI
    redoc_url="/redoc", # URL para a interface ReDoc
)

# Inclui o router principal da API (Versão 1)
# Todos os endpoints da v1 começarão com /api/v1
app.include_router(api_router, prefix=settings.API_V1_STR)

# Definindo um endpoint raiz para verificar o status da API
@app.get("/", tags=["status"])
async def read_root():
    """Retorna uma mensagem de status para indicar que a API está rodando."""
    return {"message": "API Bancária Online! Acesse /docs para a documentação."}

