# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.crud.user import user_crud
from app.core import security
from app.schemas.user import UserCreate, UserOut, Token

router = APIRouter()

@router.post(
    "/register", 
    response_model=UserOut, 
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar Novo Usuário",
    description="Cria um novo usuário e automaticamente uma conta bancária vinculada."
)
async def register_user(
    user_in: UserCreate, 
    db: AsyncSession = Depends(get_db)
):
    """Permite o cadastro de um novo usuário."""
    # A validação de usuário existente é feita dentro do CRUD
    new_user = await user_crud.create_user_with_account(db, user_in)
    return new_user

@router.post(
    "/login", 
    response_model=Token,
    summary="Login e Geração de JWT",
    description="Autentica o usuário e retorna um JSON Web Token (JWT) para acesso seguro."
)
async def login_for_access_token(
    db: AsyncSession = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Endpoint para login, retorna o JWT."""
    user = await user_crud.get_user_by_username(db, username=form_data.username)
    
    # 1. Validação de credenciais
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome de usuário ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Criação do Token JWT
    access_token = security.create_access_token(subject=str(user.id))
    
    return {"access_token": access_token, "token_type": "bearer"}
