from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.country import CountryModel
from schemas.country import Country, CountryCreate

router_country=SQLAlchemyCRUDRouter(
    schema=Country,
    create_schema=CountryCreate,
    db_model=CountryModel,
    db=get_db,
    prefix='/country'
)