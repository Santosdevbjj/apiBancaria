# app/core/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from typing import AsyncGenerator

# URL de conexão assíncrona obtida das configurações
DATABASE_URL = settings.get_database_url()

# Cria o engine assíncrono. echo=True para debug (opcional)
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Cria a SessionMaker assíncrona
# expire_on_commit=False é crucial para evitar erros ao acessar objetos após o commit
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# Função de injeção de dependência para obter a sessão do banco de dados
# Utilizada nas rotas (endpoints) do FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Fornece uma sessão assíncrona do banco de dados para a injeção de dependência do FastAPI.
    A sessão é fechada automaticamente ao final do escopo.
    """
    async with AsyncSessionLocal() as session:
        yield session

