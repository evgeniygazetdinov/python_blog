FROM registry.astralinux.ru/astra/ubi18-python311:latest
RUN groupadd -f ustor && useradd -g ustor -m -N ustor || true

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    python3-venv \
    python3-dev \
    postgresql-server-dev-all \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates

# Создание необходимых каталогов
RUN mkdir -p /app /opt/venv /certs /home/ustor/.local /home/ustor/.cache

# Создание venv и установка прав

WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH"

# Установка системных зависимостей
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install psycopg2-binary

COPY . .
RUN chown -R ustor:ustor /app /opt/venv

# Установка ustor-utils и ustor-auth
USER ustor
RUN cd /app/ustor-utils && pip install -e . && \
    cd /app/ustor-auth && pip install -e .

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

USER ustor
CMD ["uvicorn", "ustor_api.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
