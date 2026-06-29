from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init_database():
    # Создание таблиц
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Проверка на наличие данных, чтобы не дублировать
        if not crud.get_categories(db):
            cat1 = crud.create_category(db, title="Фантастика")
            cat2 = crud.create_category(db, title="Программирование")

            crud.create_book(db, title="Дюна", description="Классика фантастики", price=1200.0, category_id=cat1.id)
            crud.create_book(db, title="Нейромант", description="Киберпанк", price=950.0, category_id=cat1.id)
            
            crud.create_book(db, title="Чистый Python", description="Лучшие практики", price=1500.0, category_id=cat2.id)
            crud.create_book(db, title="Изучаем SQL", description="Основы баз данных", price=1100.0, category_id=cat2.id)
            
            print("БД успешно инициализирована и заполнена данными!")
        else:
            print("В БД уже есть данные.")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()