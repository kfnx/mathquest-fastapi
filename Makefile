lint:
	uv run ruff format .
	uv run ruff check . --fix
	
dev:
	uv run uvicorn app.main:app --reload

seed:
	uv run seed.py