from fastapi import FastAPI
from app.api import books, categories
from app.db.db import engine, Base

# Создаем таблицы в БД, если их еще нет
Base.metadata.create_all(bind=engine)

# Инициализируем FastAPI
app = FastAPI(title="Bookstore API")

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

# Проверочный эндпоинт
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running!"}