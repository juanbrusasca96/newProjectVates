from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.book import BookModel
from schemas.book import Book, BookCreate

router_book=SQLAlchemyCRUDRouter(
    schema=Book,
    create_schema=BookCreate,
    db_model=BookModel,
    db=get_db,
    prefix='/book'
)