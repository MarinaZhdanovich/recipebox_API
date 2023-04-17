from typing import List

from pydantic import BaseModel, Field
from .ingredient import IngredientModel

class RecipeBaseModel(BaseModel):
    name: str
    description: str
    difficulty: int
    instructions: str
    user_id: str


class RecipeCreateModel(RecipeBaseModel):
    pass


class RecipeUpdateModel(RecipeBaseModel):
    pass


class RecipeModel(RecipeBaseModel):
    id: int = Field(alias='recipe_id')
    name: str = Field(alias='recipe_name')
    description: str = Field(alias='recipe_description')
    difficulty: int = Field(..., exclude=True, alias='recipe_difficulty')
    instructions: str = Field(alias='recipe_instructions')
    user_id: str = Field(alias='recipe_user_id')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RecipeSchemaModel(RecipeModel):
    ingredients: List[IngredientModel]
