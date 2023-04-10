from sqlalchemy import Column, Integer, Float, ForeignKey, Text, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.mixin import Timestamp


class Ingredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, index=True)

    recipes = relationship("RecipeIngredient", back_populates="ingredient")




