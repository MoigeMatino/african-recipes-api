from typing import Any, Dict, List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.serializers.recipe import RecipeCreateSerializer, RecipeSerializer
from app.utils import create_recipe, get_recipe, get_recipes, remove_recipe

app = FastAPI()


@app.post("/recipes", response_model=RecipeSerializer)
def create_recipes(
    recipe: RecipeCreateSerializer,
    db: Session = Depends(get_db),
) -> Any:
    db_obj = create_recipe(db, recipe)
    return db_obj


@app.get("/recipes", response_model=List[RecipeSerializer])
def read_recipes(
    db: Session = Depends(get_db),
) -> Any:
    return get_recipes(db)


@app.get("/recipe/{recipe_id}", response_model=RecipeSerializer)
def read_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
) -> Any:
    return get_recipe(db, recipe_id)


@app.delete("/recipe/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)) -> Dict:
    return remove_recipe(db, recipe_id)
