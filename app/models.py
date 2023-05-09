import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    title = Column(
        String(length=255),
        nullable=False,
        index=True
    )
    serving = Column(Integer)
    ingredients = Column(ARRAY(String), nullable=False)
    instructions = Column(String, nullable=False)
    calories = Column(Float, default=0.0)
    image_file_path = Column(String, nullable=True)
    #history
class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    recipes = relationship("Recipe", back_populates="user")

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    prep_time = Column(Integer, nullable=False)
    cook_time = Column(Integer, nullable=False)
    total_time = Column(Integer, nullable=False)
    servings = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="recipes")
    recipe_tags = relationship("RecipeTag", back_populates="recipe")
    nutritional_info = relationship("NutritionalInfo", back_populates="recipe")
    recipe_ingredients = relationship("RecipeIngredient", back_populates="recipe")
    ratings = relationship("Rating", back_populates="recipe")
    comments = relationship("Comment", back_populates="recipe")

class RecipeTag(Base):
    __tablename__ = 'recipe_tags'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)

    recipe = relationship("Recipe", back_populates="recipe_tags")
    tag = relationship("Tag", back_populates="recipe_tags")

class NutritionalInfo(Base):
    __tablename__ = 'nutritional_info'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    calories = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    fiber = Column(Float, nullable=False)
    sugar = Column(Float, nullable=False)
    sodium = Column(Float, nullable=False)

    recipe = relationship("Recipe", back_populates="nutritional_info")

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    quantity = Column(String, nullable=False)

    recipe = relationship("Recipe", back_populates="recipe_ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients")

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    recipe_ingredients = relationship("RecipeIngredient", back_populates="ingredient")

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    