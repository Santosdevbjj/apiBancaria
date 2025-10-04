from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import security
from app.core.database import get_db
from app.crud.user import user_crud
from app.db.models import User

# Esquema de autenticação OAuth2 (Bearer Token)
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/v1/users/login" # Rota de login
)

# Dependência que decodifica o JWT e recupera o usuário
async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> User:
    try:
        # 1. Decodifica o token para obter o 'sub' (ID do usuário)
        payload = security.decode_token(token=token)
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autenticação inválido",
            )
            
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Busca o usuário no banco
    user = await user_crud.get_user_by_id(db, user_id=int(user_id))
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    if not user.is_active:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário inativo")
         
    return user
