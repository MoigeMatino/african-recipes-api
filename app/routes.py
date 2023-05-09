from fastapi import FastAPI, Depends
from db.db import get_db
from models import Recipe
from utils import create_recipe, get_recipe, get_recipes, delete_recipe
from schemas import RecipeSerializer, RecipeCreateSerializer
from typing import List, Any, Dict
from sqlalchemy.orm import Session

app=FastAPI()

@app.post('/recipes', response_model=RecipeSerializer)
def create_recipes(
    recipe: RecipeCreateSerializer,
    db: Session=Depends(get_db),
) -> Any:
    db_obj=create_recipe(db,recipe)
    return db_obj

@app.get('/recipes', response_model=List[RecipeSerializer])
def read_recipes(
    db: Session = Depends(get_db),
) -> Any:
    return get_recipes(db)

@app.get('/recipe/{recipe_id}', response_model=RecipeSerializer)
def read_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
) -> Any:
    return get_recipe(db, recipe_id)

@app.delete('/recipe/{recipe_id}')
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db)
) -> Dict:
    return delete_recipe(db, recipe_id)