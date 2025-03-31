# Stage 1: Base build stage
FROM python:3.13-slim-bookworm AS base

FROM base AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set enviromentals
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONDONTWRITEBYTECORE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy project dependencies
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Stage 2: Production stage
FROM base

# Set enviromentals variables to optimize Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Add User to prevent root privileges
RUN useradd -m -r appuser && \
    chown -R appuser /app &&\
    mkdir -p /vol/web/static &&\
    chown -R appuser /vol


# Copy the Python dependencies from the builder stage
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

RUN chmod +x /app/scripts/django_entrypoint.sh
