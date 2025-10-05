# app/api/v1/endpoints/transactions.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_current_user
from app.db.models import User
from app.core.database import get_db
from app.crud.transaction import transaction_crud
from app.schemas.transaction import TransactionCreate, TransactionOut, Statement

router = APIRouter()

@router.post(
    "/process", 
    response_model=TransactionOut, 
    status_code=status.HTTP_201_CREATED,
    summary="Processar Transação (Depósito/Saque)",
    description="Realiza um depósito ou saque. Requer autenticação JWT."
)
async def process_transaction(
    transaction_in: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    # Dependência que injeta o usuário autenticado. Garante a segurança.
    current_user: User = Depends(get_current_user) 
):
    """
    Executa a lógica de Depósito ou Saque, incluindo validações de valor negativo
    e saldo insuficiente.
    """
    account = current_user.account
    if not account:
        raise HTTPException(status_code=404, detail="Conta bancária não encontrada para este usuário.")

    # A lógica de validação de saldo e valor negativo é encapsulada no CRUD
    db_transaction = await transaction_crud.create_transaction(
        db, 
        transaction_in=transaction_in, 
        account_id=account.id
    )
    return db_transaction

# O endpoint GET /statement (Extrato) foi detalhado na primeira resposta e continua válido.
# ... (Código do endpoint get_statement)
