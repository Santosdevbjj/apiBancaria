# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

# Definindo a string de prefixo para a versão da API (Boa Prática)
API_V1_STR: str = "/api/v1"

class Settings(BaseSettings):
    """
    Classe de configurações da aplicação, carregando variáveis do ambiente
    ou do arquivo .env.
    """
    # Configuração Pydantic para carregar do arquivo .env
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    
    # ----------------------------------------------------
    # Configurações de Banco de Dados (PostgreSQL)
    # ----------------------------------------------------
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    # O host padrão 'db' é crucial para o Docker Compose
    POSTGRES_HOST: str = "db"
    # A URL completa pode ser opcionalmente fornecida
    DATABASE_URL: Optional[str] = None 

    # ----------------------------------------------------
    # Configurações de Segurança e JWT
    # ----------------------------------------------------
    SECRET_KEY: str = "seu-super-segredo-jwt-aqui-trocar-em-producao" # Chave secreta para assinatura do JWT
    ALGORITHM: str = "HS256" # Algoritmo de criptografia
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Tempo de expiração do token em minutos

    # ----------------------------------------------------
    # Métodos de Ajuda (Princípio POO)
    # ----------------------------------------------------

    def get_database_url(self) -> str:
        """
        Constrói a URL de conexão do PostgreSQL (formato asyncpg) 
        usando as variáveis de ambiente.
        """
        # Se DATABASE_URL já estiver definida (e.g., em um ambiente de produção), use-a
        if self.DATABASE_URL:
            return self.DATABASE_URL
        
        # Caso contrário, constrói a URL padrão para uso com asyncpg
        # O driver '+asyncpg' é obrigatório para o SQLAlchemy assíncrono
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB}"
        )
    
    @property
    def API_V1_STR(self) -> str:
        """Retorna o prefixo da API para uso no main.py."""
        return API_V1_STR

# Instancia a classe Settings. Isso carrega as variáveis de ambiente
# e valida seus tipos imediatamente ao iniciar o app.
settings = Settings()
