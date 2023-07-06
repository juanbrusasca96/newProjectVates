from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.state import StateModel
from schemas.state import State, StateCreate

router_state=SQLAlchemyCRUDRouter(
    schema=State,
    create_schema=StateCreate,
    db_model=StateModel,
    db=get_db,
    prefix='/state'
)