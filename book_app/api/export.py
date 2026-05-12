from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse, JSONResponse
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.services.import_export_service import (
    export_books_json,
    export_books_csv
)

router = APIRouter(prefix="/export", tags=["Export"])


@router.get("/books/json")
def export_json(db: Session = Depends(get_db)):
    data = export_books_json(db)
    return JSONResponse(content=data)


@router.get("/books/csv")
def export_csv(db: Session = Depends(get_db)):
    csv_data = export_books_csv(db)

    return StreamingResponse(
        iter([csv_data]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=books.csv"}
    )
