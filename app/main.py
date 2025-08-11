from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.core.settings import settings
from app.routes.lesson_routes import lessons_router
from app.routes.user_routes import users_router

app = FastAPI(
    title=settings.APP_NAME,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=settings.OPENAPI_URL,
)

app.include_router(lessons_router, prefix="/api")
app.include_router(users_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "mathquest API"}


@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        title=settings.APP_NAME,
        openapi_url=settings.OPENAPI_URL,
    )
