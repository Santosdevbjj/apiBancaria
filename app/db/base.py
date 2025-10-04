# app/db/base.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

# Cria a classe Base que todos os modelos herdarão.
# AsyncAttrs é necessário para que as classes possam ter Mapped (Type Hints) e sejam compatíveis com o AsyncSession
class Base(AsyncAttrs, declarative_base()):
    """Classe base declarativa para os modelos do SQLAlchemy."""
    __abstract__ = True # Indica que esta classe não deve ser mapeada para uma tabela
    pass

# Importa todos os modelos para garantir que o Alembic os detecte (importante para migrations)
# from app.db.models import * # Descomentar se models for refatorado para ter apenas 1 arquivo
