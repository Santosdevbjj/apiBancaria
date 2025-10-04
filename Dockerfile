# Usa uma imagem oficial do Python 3.11 Slim
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY ./app /app/app

# Comando de inicialização: Executa as migrações e depois inicia o Uvicorn
# Usar um script de entrada para gerenciar isso seria uma boa prática
CMD ["/bin/bash", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
