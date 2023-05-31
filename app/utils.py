from sqlalchemy.orm import Session

from app.models import Recipe
from app.serializers.schemas import RecipeCreateSerializer


def create_recipe(db: Session, recipe: RecipeCreateSerializer):
    db_obj = Recipe(**recipe.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def get_recipe(db: Session, recipe_id: int):
    recipe = db.query(Recipe).where(Recipe.id == recipe_id).first()
    return recipe


def get_recipes(db: Session):
    recipes = db.query(Recipe).all()
    return recipes


def remove_recipe(db: Session, recipe_id: int):
    db_obj = db.query(Recipe).where(Recipe.id == recipe_id).first()
    db.delete(db_obj)
    db.commit()
    return {"message": "Recipe deleted"}
