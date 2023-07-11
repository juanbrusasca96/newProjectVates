from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.book import BookModel
from schemas.book import Book, BookCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserModel
from models.country import CountryModel

router_especial = APIRouter(
    prefix="/especial",
    tags=["especial"],
)


@router_especial.get("/get_users_by_country", status_code=200)
async def get_all_users(db: Session = Depends(get_db), country_name: str = None):
    query = db.query(UserModel)

    if country_name:
        query = query.join(CountryModel).filter(
            CountryModel.name == country_name)

    users = query.all()

    user_names = [user.name for user in users]

    cantidad_users = len(users)
    frase = f"En {country_name} hay {cantidad_users} usuario{'s' if cantidad_users != 1 else ''}: {', '.join(user_names)}"

    return frase


# @router_especial.get("/get_books_by_user", status_code=200)
# async def get_books(db: Session = Depends(get_db), user_name: str = None):
#     query = db.query(BookModel)
#     if user_name:
#         query = query.join(UserModel).filter(UserModel.name == user_name)
#     books = query.all()
#     books_names = [book.name for book in books]

#     cantidad_books = len(books)

#     frase = f"{user_name} tiene {cantidad_books} libro{'s' if cantidad_books != 1 else ''} en la biblioteca: {', '.join(books_names)}"
#     return frase


@router_especial.get("/get_books_by_user", status_code=200)
async def get_books(db: Session = Depends(get_db), user_name: str = None):
    query = db.query(BookModel)
    if user_name:
        query = query.join(UserModel).filter(UserModel.name == user_name)
    books = query.all()

    books_by_state = {}
    for book in books:
        state_name = book.state.name
        books_by_state.setdefault(state_name, []).append(book)

    cantidad_books = len(books)

    sentence = f"{user_name} tiene {cantidad_books} libro{'s' if cantidad_books != 1 else ''} en la biblioteca: {', '.join([book.name for book in books])}"
    sentences = [sentence]

    sentences.extend([f". {len(state_books)} {'está' if len(state_books) == 1 else 'están'} en el estado '{state_name}'." for state_name, state_books in books_by_state.items()])

    return " ".join(sentences)







# async def get_books(db: Session = Depends(get_db), user_name: str = None):
#     query = db.query(BookModel)
#     if user_name:
#         query = query.join(UserModel).filter(UserModel.name == user_name)
#     books = query.all()

#     books_by_state = {}
#     for book in books:
#         state_name = book.state.name
#         if state_name not in books_by_state:
#             books_by_state[state_name] = []
#         books_by_state[state_name].append(book)

#     book_names = [book.name for book in books]

#     cantidad_books = len(books)

#     sentences = []
#     sentence = f"{user_name} tiene {cantidad_books} libro{'s' if cantidad_books != 1 else ''} en la biblioteca: {', '.join(book_names)}"
#     sentences.append(sentence)

#     for state_name, state_books in books_by_state.items():
#         cantidad_books_by_state = len(state_books)
#         sentence = f". {cantidad_books_by_state} {'está' if cantidad_books_by_state == 1 else 'están'} en el estado '{state_name}'."
#         sentences.append(sentence)

#     return " ".join(sentences)





# hacer una segunda ruta que me traiga los libros por usuario, la respuesta 'rafa tiene 3 libros en la biblioteca: 'nombre1', 'nombre2', 'nombre3'. 2 de ellos estan prestados'
# posibles estados: prestado, devuelto
# necesito una relacion entr 3 tablas: users, books, states
# voy a necesitar una tabla intermedia, que se llene con sqlalchemycrudrouter
