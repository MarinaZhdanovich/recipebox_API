import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.ingredient import IngredientModel
from app.models.ingredient import Ingredient
from app.crud.ingredient import get_ingredient_by_id, get_ingredient_list

ingredient_router = APIRouter()
logger = logging.getLogger('recipebox')


@ingredient_router.get('/ingredient/{ingredient_id}', response_model=IngredientModel)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)) -> Ingredient:
    if db_ingredient := get_ingredient_by_id(db, ingredient_id):
        logger.info(msg=f"Get ingredient {db_ingredient.name}")
        return db_ingredient
    else:
        logger.error(f"Ingredient does\'t with id={ingredient_id} exist")
        raise HTTPException(status_code=404, detail=f"Ingredient does\'t with id={ingredient_id} exist")



