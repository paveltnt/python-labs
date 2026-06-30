from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.db import get_db
import app.db.crud as crud
import app.schemas as schemas
from app.db.models import Category

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.Book])
def read_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    # category_id передается как ?category_id=1 в URL
    return crud.get_books(db, category_id=category_id)

@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Валидация: существует ли такая категория?
    db_category = db.query(Category).filter(Category.id == book.category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db=db, book=book)