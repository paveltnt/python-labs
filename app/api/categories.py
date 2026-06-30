from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.db import get_db
import app.db.crud as crud
import app.schemas as schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.post("/", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    crud.delete_category(db, category_id)
    return {"message": "Category deleted"}