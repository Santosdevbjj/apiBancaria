# app/schemas/account.py
from pydantic import BaseModel, Field

# Schema de saída da conta (output)
class AccountOut(BaseModel):
    """Schema para formatar os dados de saída da conta bancária."""
    id: int
    user_id: int
    # O saldo sempre deve ser >= 0
    balance: float = Field(..., ge=0)

    class Config:
        from_attributes = True
