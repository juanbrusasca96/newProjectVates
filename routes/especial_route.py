from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.book import BookModel
from schemas.book import Book, BookCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserModel
from models.country import CountryModel

router_especial = APIRouter(
  prefix='/especial',
  tags=['especial'],
)

@router_especial.get('/get_users', status_code=200)
async def get_all_users(db: Session = Depends(get_db), country_name: str = None):
    query = db.query(UserModel)
    
    if country_name:
        query = query.join(CountryModel).filter(CountryModel.name == country_name)
    
    users = query.all()

    user_names = [user.name for user in users]

    cantidad_users = len(users)
    frase = f"En {country_name} hay {cantidad_users} usuario{'s' if cantidad_users != 1 else ''}: {', '.join(user_names)}"

    return frase

#hacer una segunda ruta que me traiga los libros por usuario, la respuesta 'rafa tiene 3 libros en la biblioteca: 'nombre1', 'nombre2', 'nombre3'. 2 de ellos estan prestados'
#posibles estados: prestado, devuelto
#necesito una relacion entr 3 tablas: users, books, states
#voy a necesitar una tabla intermedia, que se llene con sqlalchemycrudrouter