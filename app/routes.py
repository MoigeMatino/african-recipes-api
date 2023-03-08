from fastapi import FastAPI, Depends
from db import get_db
from models import Recipe
from utils import create_recipe, get_recipe, get_recipes, delete_recipe
from schemas import RecipeSerializer
from typing import List
from sqlalchemy.orm import Session

app=FastAPI()

@app.post('/recipes', response_model=RecipeSerializer)
def create_recipe(
    recipe: Recipe,
    db: Session=Depends(get_db),
):
    db_obj=create_recipe(db,recipe)
    return db_obj

@app.get('/recipes', response_model=List[RecipeSerializer])
def get_recipes(
    db: Session = Depends(get_db),
):
    return get_recipes(db)

@app.get('/recipe/{recipe_id}', response_model=RecipeSerializer)
def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    return get_recipe(db, recipe_id)

@app.delete('/recipe/{recipe_id}')
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db)
):
    return delete_recipe(db, recipe_id)