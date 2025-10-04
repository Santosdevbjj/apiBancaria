from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from .base import Base # Supondo que Base é a classe base declarativa

# Classe que representa um Usuário
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String, nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=True)
    
    # Relacionamento 1:1 com Account
    account: Mapped["Account"] = relationship("Account", back_populates="user", uselist=False)

# Classe que representa a Conta Corrente
class Account(Base):
    __tablename__ = "accounts"
    
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    balance: Mapped[float] = Column(Float, default=0.0)
    
    # Relacionamento 1:1 com User
    user: Mapped["User"] = relationship("User", back_populates="account")
    # Relacionamento 1:N com Transaction
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="account")

# Classe que representa uma Transação (Depósito/Saque)
class Transaction(Base):
    __tablename__ = "transactions"
    
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    account_id: Mapped[int] = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount: Mapped[float] = Column(Float, nullable=False) # Valor positivo (depósito) ou negativo (saque)
    type: Mapped[str] = Column(String, nullable=False) # "DEPOSIT" ou "WITHDRAW"
    timestamp: Mapped[DateTime] = Column(DateTime, default=func.now())
    
    # Relacionamento N:1 com Account
    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
