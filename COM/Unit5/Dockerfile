# Stage 1: build
FROM python:3.11-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Install build deps if needed (keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY . .

# Create non-root user
RUN groupadd --gid 1000 appuser \
 && useradd -m --uid 1000 --gid 1000 appuser \
 && chown -R appuser:appuser /app

USER appuser
EXPOSE 8080

# Fallback: use python -m gunicorn to avoid PATH issues
CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers=2", "--worker-class=gthread"]
