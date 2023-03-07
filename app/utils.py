from sqlalchemy.orm import Session
from schemas import RecipeSerializer
from models import Recipe

def create_recipe(db: Session,recipe: RecipeSerializer):
    db_obj = Recipe(**recipe.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj