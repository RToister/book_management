from fastapi import FastAPI

from book_app.core.database import Base, engine

from book_app.api.auth import router as auth_router
from book_app.api.books import router as books_router
from book_app.api.authors import router as authors_router
from book_app.api.export import router as export_router
from book_app.api.imports import router as import_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(books_router)
app.include_router(authors_router)
app.include_router(export_router)
app.include_router(import_router)
