from fastapi import FastAPI

from book_app.api.authors import router as authors_router

app = FastAPI(title="Book Management System")

app.include_router(authors_router)


@app.get("/")
def root():
    return {"message": "API is running"}
