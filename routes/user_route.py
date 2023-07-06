from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.user import UserModel
from schemas.user import User, UserCreate

router_user=SQLAlchemyCRUDRouter(
    schema=User,
    create_schema=UserCreate,
    db_model=UserModel,
    db=get_db,
    prefix='/user'
)