from app.db.db import SessionLocal
from app.db import crud

def main():
    # Тот самый код из прошлой лабы
    print("Hello, World!")
    
    # Чтение данных из БД
    db = SessionLocal()
    try:
        books = crud.get_books(db)
        print("\n=== СПИСОК КНИГ ИЗ БАЗЫ ДАННЫХ ===")
        for book in books:
            print(f"Категория: {book.category.title}")
            print(f"Название: {book.title}")
            print(f"Цена: {book.price} руб.")
            print(f"Описание: {book.description}")
            print("-" * 30)
    finally:
        db.close()

if __name__ == "__main__":
    main()