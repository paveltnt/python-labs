from sqlalchemy.orm import Session
from app.db.models import Category, Book
import app.schemas as schemas

# --- Категории ---
def get_categories(db: Session):
    return db.query(Category).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = Category(title=category.title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# --- Книги ---
def get_books(db: Session, category_id: int = None):
    query = db.query(Book)
    if category_id:
        query = query.filter(Book.category_id == category_id) # Фильтрация по категории
    return query.all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book