# app/crud/base.py
from typing import Any, Generic, TypeVar, Type, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.base import Base # Importa a base declarativa do modelo

# Define os tipos genéricos (ModelType é a classe do modelo, e.g., User)
ModelType = TypeVar("ModelType", bound=Base)

class CRUDBase(Generic[ModelType]):
    """
    Classe base para todas as operações CRUD.
    Implementa as funcionalidades básicas de forma genérica.
    """
    def __init__(self, model: Type[ModelType]):
        """
        :param model: A classe do modelo SQLAlchemy (e.g., User, Account).
        """
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        """Busca um objeto pelo ID."""
        # Uso do 'select' assíncrono
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Busca múltiplos objetos (com paginação)."""
        result = await db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()
