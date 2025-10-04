# app/api/v1/api.py

from fastapi import APIRouter
from app.api.v1.endpoints import users
from app.api.v1.endpoints import accounts
from app.api.v1.endpoints import transactions

# Cria o roteador principal para a versão 1
api_router = APIRouter()

# Inclui os roteadores específicos
# Rotas de Usuário (e autenticação/login)
api_router.include_router(users.router, prefix="/users", tags=["Usuários e Autenticação"])

# Rotas de Contas (criação e informações da conta)
api_router.include_router(accounts.router, prefix="/accounts", tags=["Contas Bancárias"])

# Rotas de Transações (depósito, saque, extrato)
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transações"])

