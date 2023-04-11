import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.recipe_ingredient import RecipeIngredient


logger = logging.getLogger("recipebox")


def create_init_recipe_ingredient(db: Session, recipe_ingredient: RecipeIngredient) -> RecipeIngredient:
    db_recipe_ingredient = RecipeIngredient(
        recipe_id=recipe_ingredient.recipe_id,
        ingredient_id=recipe_ingredient.ingredient_id,
        quantity=recipe_ingredient.quantity
    )
    db.add(db_recipe_ingredient)
    db.commit()
    db.refresh(db_recipe_ingredient)
    logger.info(f'Created recipe_ingredient {db_recipe_ingredient}')
    return db_recipe_ingredient




