# app/crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User, Account
from app.schemas.user import UserCreate
from app.crud.base import CRUDBase
from app.core import security # Para hash de senha
from fastapi import HTTPException

class CRUDUser(CRUDBase[User]):
    """
    Operações CRUD específicas para o modelo User.
    """
    async def get_user_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """Busca um usuário pelo nome (email)."""
        result = await db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()

    async def create_user_with_account(self, db: AsyncSession, user_in: UserCreate) -> User:
        """
        Cria um novo usuário e automaticamente cria uma conta bancária
        vinculada a ele (Princípio de POO/Lógica de Negócio).
        """
        # 1. Checa se o usuário já existe
        if await self.get_user_by_username(db, user_in.username):
            raise HTTPException(status_code=400, detail="Nome de usuário já registrado.")

        # 2. Hash da senha (segurança)
        hashed_password = security.get_password_hash(user_in.password)
        
        # 3. Cria o objeto User no DB
        db_user = User(
            username=user_in.username,
            hashed_password=hashed_password,
        )
        db.add(db_user)
        
        # 4. Cria a Conta Corrente (saldo inicial 0.0)
        await db.flush() # Força o DB a obter o ID do novo usuário (db_user.id)
        db_account = Account(user_id=db_user.id, balance=0.0)
        db.add(db_account)

        await db.commit()
        await db.refresh(db_user)
        # O db_user agora terá o relacionamento 'account' preenchido
        return db_user

user_crud = CRUDUser(User)
