from typing import List
import uuid
from app.constants import Role
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, Text, TIMESTAMP, text, Column, UUID
from app.db.base_class import Base, generate_fake_email


class User(Base):
    __tablename__ = "user"

    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True)
    email = mapped_column(String, unique=True, index=True, default=generate_fake_email, nullable=True)
    password_hash = mapped_column(String, nullable=False)
    role = mapped_column(String, nullable=False, default=Role.USER.value,
                         server_default=Role.USER.value
                         )
    recipes: Mapped[List["Recipe"]] = relationship(back_populates="user")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    rating: Mapped[List["Rating"]] = relationship(back_populates="user")

    photo_id = Column(UUID, ForeignKey("images.id"))
    photo = relationship("Image", back_populates="images")


class Recipe(Base):
    __tablename__ = "recipes"

    title: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    instructions = mapped_column(Text, nullable=False)
    prep_time: Mapped[int] = mapped_column(Integer)
    cooking_time: Mapped[int] = mapped_column(Integer)
    servings: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="recipes")
    tags: Mapped[List["RecipeTags"]] = relationship(back_populates="recipes")
    ingredients: Mapped[List["RecipeIngredients"]] = relationship(back_populates="recipes")
    comments: Mapped[List["Comment"]] = relationship(back_populates="recipe")
    rating: Mapped["Rating"] = relationship(back_populates="recipe")
    nutritional_info = relationship("NutritionalInfo", uselist=False, back_populates="recipe")


class Tag(Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    recipes: Mapped[List["RecipeTags"]] = relationship("Recipe", back_populates="tags")


class RecipeTags(Base):
    __tablename__ = "recipe_tags"

    recipe_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("recipes.id"), primary_key=True)
    tag_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("tags.id"), primary_key=True)

    tags: Mapped["Tag"] = relationship(back_populates="recipes")
    recipes: Mapped["Recipe"] = relationship(back_populates="tags")


class Ingredients(Base):
    __tablename__ = "ingredients"

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    recipes: Mapped["RecipeIngredients"] = relationship(back_populates="ingredients")


class RecipeIngredients(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("ingredients.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)

    ingredients: Mapped["Ingredients"] = relationship(back_populates="recipes")
    recipes: Mapped["Recipe"] = relationship(back_populates="ingredients")


class Comment(Base):
    __tablename__ = "comments"

    comment: Mapped[str] = mapped_column(String, nullable=True)
    recipe_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("recipes.id"), nullable=False)
    recipe: Mapped["Recipe"] = relationship(back_populates="comments")
    user_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="comments")


class Rating(Base):
    __tablename__ = "ratings"

    recipe_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("recipes.id"), nullable=False)
    recipe: Mapped["Recipe"] = relationship(back_populates="rating")
    user_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="rating")


class NutritionalInfo(Base):
    __tablename__ = "nutritional_info"

    calories: Mapped[float] = mapped_column(Float)
    carbohydrates: Mapped[float] = mapped_column(Float)
    fat: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float)
    fiber: Mapped[float] = mapped_column(Float)
    sugar: Mapped[float] = mapped_column(Float)
    sodium: Mapped[float] = mapped_column(Float)

    recipe_id: Mapped[uuid.UUID] = mapped_column(String, ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", back_populates="nutritional_info")


class Image(Base):
    __tablename__ = "images"

    url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), nullable=False,
                                                  server_default=text("now()"))
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), nullable=False,
                                                  server_default=text("now()"))
