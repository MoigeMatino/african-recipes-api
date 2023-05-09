from typing import List

from constants import Role
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text
from db.base_class import Base, generate_fake_email


class User(Base):
    __tablename__ = "user"

    first_name : Mapped[str] = mapped_column(String, nullable=False)
    last_name : Mapped[str] = mapped_column(String, nullable=False)
    username : Mapped[str] = mapped_column(String, unique=True)
    email = mapped_column(String, unique=True, index=True, default=generate_fake_email, nullable=True
    )
    password_hash = mapped_column(String, nullable=False)
    role = mapped_column(String, nullable=False, default=Role.USER.value,
        server_default=Role.USER.value
    )
    recipes: Mapped[List["Recipe"]] = relationship(back_populates="user")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    rating: Mapped[List["Rating"]] = relationship(back_populates="user")


class Recipe(Base):
    __tablename__ = "recipes"

    title: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    instructions = mapped_column(Text, nullable=False)
    prep_time: Mapped[int] = mapped_column(Integer)
    cooking_time: Mapped[int] = mapped_column(Integer)
    servings: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    user_id = mapped_column(String, ForeignKey("user.id"), nullable=False)
    user : Mapped["User"] = relationship("User", back_populates="recipes")
    tags: Mapped[List["Recipe_Tags"]] = relationship(back_populates="recipes")
    ingredients: Mapped[List["Recipe_Ingredients"]] = relationship(back_populates="recipes")
    comments: Mapped[List["Comment"]] = relationship(back_populates="recipe")
    rating: Mapped["Rating"] = relationship(back_populates="recipe")
    nutritional_info = relationship("Nutritional_Info", uselist=False, back_populates="recipe")

class Tag(Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    recipes: Mapped[List["Recipe_Tags"]] = relationship("Recipe", back_populates="tags")

class Recipe_Tags(Base):
    __tablename__ = "recipe_tags"

    recipe_id = mapped_column(String, ForeignKey("recipes.id"), primary_key=True)
    tag_id = mapped_column(String, ForeignKey("tags.id"), primary_key=True)

    tags : Mapped["Tag"] = relationship(back_populates="recipes")
    recipes : Mapped["Recipe"] = relationship(back_populates="tags")

class Ingredients(Base):
    __tablename__ = "ingredients"

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    recipes: Mapped["Recipe_Ingredients"] = relationship(back_populates="ingredients")

class Recipe_Ingredients(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id = mapped_column(String, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = mapped_column(String, ForeignKey("ingredients.id"), primary_key=True)

    ingredients: Mapped["Ingredients"] = relationship(back_populates="recipes")
    recipes: Mapped["Recipe"] = relationship(back_populates="ingredients")

class Comment(Base):
    __tablename__ = "comments"

    comment: Mapped[str] = mapped_column(String, nullable=True)
    recipe_id = mapped_column(ForeignKey("recipes.id"), nullable=False)
    recipe: Mapped["Recipe"] = relationship(back_populates="comments")
    user_id = mapped_column(String, ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="comments")

class Rating(Base):
    __tablename__ = "ratings"

    recipe_id = mapped_column(String, ForeignKey("recipes.id"), nullable=False)
    recipe: Mapped["Recipe"] = relationship(back_populates="rating")
    user_id = mapped_column(String, ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="rating")

class Nutritional_Info(Base):
    __tablename__ = "nutritional_info"

    calories: Mapped[float] = mapped_column(Float)
    carbohydrates: Mapped[float] = mapped_column(Float)
    fat: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float)
    fiber: Mapped[float] = mapped_column(Float)
    sugar: Mapped[float] = mapped_column(Float)
    sodium: Mapped[float] = mapped_column(Float)

    recipe_id = mapped_column(String, ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", back_populates="nutritional_info")