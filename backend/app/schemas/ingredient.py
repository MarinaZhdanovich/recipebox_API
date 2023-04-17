from typing import Optional, List

from pydantic import BaseModel, Field
from .recipe import RecipeModel


class IngredientBaseModel(BaseModel):
    name: str
    units: Optional[str]


class IngredientCreateModel(IngredientBaseModel):
    pass


class IngredientUpdateModel(IngredientBaseModel):
    pass


class IngredientModel(IngredientBaseModel):
    id: int = Field(alias='ingredient_id')
    name: str = Field(alias='ingredient_name')
    units: str = Field(alias='ingredient_units')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientSchemaModel(IngredientModel):
    recipes: List[RecipeModel]


