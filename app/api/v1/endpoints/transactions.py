from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_current_user
from app.db.models import User
from app.core.database import get_db
from app.crud.transaction import transaction_crud
from app.schemas.transaction import TransactionOut, Statement
from typing import List

router = APIRouter()

@router.get(
    "/statement",
    response_model=Statement, # Retorna o saldo e a lista de transações
    status_code=status.HTTP_200_OK,
    summary="Extrato da Conta",
    description="Exibe o saldo atual e todas as transações realizadas pelo usuário autenticado."
)
async def get_statement(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user) # Requisito de Autenticação JWT
):
    """
    Retorna o extrato completo de uma conta.
    """
    # 1. Recupera a conta do usuário
    account = current_user.account
    if not account:
        raise HTTPException(status_code=404, detail="Conta não vinculada ao usuário.")

    # 2. Busca todas as transações da conta
    transactions = await transaction_crud.get_transactions_by_account_id(db, account_id=account.id)
    
    # 3. Cria o objeto de resposta (Statement Schema)
    return Statement(
        account_id=account.id,
        current_balance=account.balance,
        transactions=transactions
    )
