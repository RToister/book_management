from fastapi import FastAPI

app = FastAPI(
    title="Book Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Book Management API is running"}
