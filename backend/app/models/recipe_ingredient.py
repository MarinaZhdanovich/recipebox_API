from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.db.base_class import Base
from app.models.mixin import Timestamp
from sqlalchemy.orm import relationship
from .recipe import Recipe
from .ingredient import Ingredient
from sqlalchemy.ext.associationproxy import association_proxy


class RecipeIngredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"))
    quantity = Column(Float, nullable=False)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")

    recipe_name = association_proxy(target_collection='recipe', attr='name')
    recipe_description = association_proxy(target_collection='recipe', attr='description')
    recipe_difficulty = association_proxy(target_collection='recipe', attr='difficulty')
    recipe_instructions = association_proxy(target_collection='recipe', attr='instructions')
    recipe_user_id = association_proxy(target_collection='recipe', attr='user_id')

    ingredient_name = association_proxy(target_collection='ingredient', attr='name')
    ingredient_units = association_proxy(target_collection='ingredient', attr=' units')

