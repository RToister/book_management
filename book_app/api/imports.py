from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.services.import_export_service import (
    import_books_from_json,
    import_books_from_csv
)

router = APIRouter(prefix="/import", tags=["Import"])


@router.post("/books")
async def import_books(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    content = await file.read()

    if file.filename.endswith(".json"):
        count = import_books_from_json(db, content)

    elif file.filename.endswith(".csv"):
        count = import_books_from_csv(db, content)

    else:
        raise HTTPException(
            status_code=400,
            detail="Only CSV or JSON allowed"
        )

    return {
        "message": "import completed",
        "books_added": count
    }
