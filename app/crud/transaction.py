from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.db.models import Account, Transaction
from app.schemas.transaction import TransactionCreate

# ... (Outras importações)

class CRUDTransaction:
    # Cria uma transação, atualiza o saldo e aplica validações
    async def create_transaction(self, db: AsyncSession, transaction_in: TransactionCreate, account_id: int):
        
        # 1. Recupera a conta
        result = await db.execute(select(Account).where(Account.id == account_id))
        account = result.scalar_one_or_none()
        if not account:
            raise HTTPException(status_code=404, detail="Conta não encontrada.")

        amount = transaction_in.amount
        
        # 2. Validação: Não permitir valores negativos
        if amount <= 0:
            raise HTTPException(status_code=400, detail="O valor da transação deve ser positivo.")
            
        # 3. Lógica de Saque (WITHDRAW) e validação de Saldo
        if transaction_in.type.upper() == "WITHDRAW":
            if account.balance < amount:
                # Validação: Saldo Insuficiente
                raise HTTPException(status_code=400, detail="Saldo insuficiente para realizar o saque.")
            
            # Atualiza o saldo para saque
            account.balance -= amount
            amount_to_save = -amount # Salva o valor como negativo para extrato
            
        # 4. Lógica de Depósito (DEPOSIT)
        elif transaction_in.type.upper() == "DEPOSIT":
            account.balance += amount
            amount_to_save = amount # Salva o valor como positivo
        
        else:
             raise HTTPException(status_code=400, detail="Tipo de transação inválido. Use 'DEPOSIT' ou 'WITHDRAW'.")

        # 5. Cria a entrada da transação no BD
        db_transaction = Transaction(
            account_id=account_id,
            amount=amount_to_save,
            type=transaction_in.type.upper()
        )
        
        db.add(db_transaction)
        db.add(account) # Adiciona a conta atualizada
        await db.commit()
        await db.refresh(db_transaction)
        return db_transaction

transaction_crud = CRUDTransaction()
