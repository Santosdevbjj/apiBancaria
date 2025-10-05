# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Schema base para criação de usuário (input)
class UserCreate(BaseModel):
    """Schema para validação dos dados de entrada ao criar um novo usuário."""
    # EmailStr garante que o formato do username seja de email
    username: EmailStr = Field(..., example="usuario@banco.com")
    # A senha deve ser obrigatória
    password: str = Field(..., min_length=8, example="senhaSegura123")

# Schema de saída do usuário (output)
class UserOut(BaseModel):
    """Schema para formatar os dados de saída do usuário."""
    id: int
    username: EmailStr
    is_active: bool

    class Config:
        # Permite que o Pydantic mapeie o ORM (SQLAlchemy) para o Schema
        from_attributes = True

# Schemas de Autenticação JWT
class Token(BaseModel):
    """Schema para o token de acesso retornado após o login."""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Schema para os dados contidos dentro do token JWT."""
    username: Optional[str] = None
