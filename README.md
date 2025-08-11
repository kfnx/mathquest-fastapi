# Mathquest Fastapi

# Prerequisite

- uv
- docker compose


# Development

```
# fill data
cp .env.example .env
docker compose -f docker-compose.dev.yml up -d
uv sync
make seed
make dev
```