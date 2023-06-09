import logging
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient

logger = logging.getLogger("recipebox")


def create_init_ingredient(db: Session, ingredient: Ingredient) -> Ingredient:
    db_ingredient = Ingredient(
        name=ingredient.name,
        units=ingredient.units
    )
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    logger.info(f'Created ingredient {db_ingredient}')
    return db_ingredient


def get_ingredient_by_id(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()


def get_ingredient_list(db: Session) -> List[Ingredient]:
    return db.query(Ingredient).all()