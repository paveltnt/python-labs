from sqlalchemy.orm import Session
from .models import Category, Book

def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    db_book = Book(
        title=title, 
        description=description, 
        price=price, 
        category_id=category_id, 
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_categories(db: Session):
    return db.query(Category).all()

def get_books(db: Session):
    return db.query(Book).all()