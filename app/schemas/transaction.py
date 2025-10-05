# app/schemas/transaction.py
from pydantic import BaseModel, Field, condecimal
from typing import List
from datetime import datetime

# Schema de entrada para Depósito/Saque
class TransactionCreate(BaseModel):
    """Schema para validação dos dados de entrada ao realizar um Depósito ou Saque."""
    # O valor deve ser um decimal positivo (será validado na lógica CRUD)
    amount: condecimal(max_digits=10, decimal_places=2) = Field(..., gt=0, example=100.50)
    # Garante que o tipo seja "DEPOSIT" ou "WITHDRAW"
    type: str = Field(..., pattern="^(DEPOSIT|WITHDRAW)$", example="DEPOSIT")

# Schema de saída para uma transação individual
class TransactionOut(BaseModel):
    """Schema para formatar os dados de saída de uma transação."""
    id: int
    account_id: int
    # O valor salvo no DB será positivo para depósito e negativo para saque
    amount: float
    type: str
    timestamp: datetime

    class Config:
        from_attributes = True

# Schema de Extrato (Statement)
class Statement(BaseModel):
    """Schema para formatar a resposta do extrato (saldo + histórico de transações)."""
    account_id: int
    current_balance: float
    transactions: List[TransactionOut]
