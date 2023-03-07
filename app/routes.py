from fastapi import FastAPI, Depends
from db import get_db
from models import Recipe
from schemas import RecipeSerializer
from typing import List
from sqlalchemy.orm import Session

app=FastAPI()

@app.post('/recipes', response_model=RecipeSerializer)
def create_recipe(
    recipe: Recipe,
    db: Session=Depends(get_db),
):
    db_obj=Recipe(**recipe.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

@app.get('/recipes', response_model=List[RecipeSerializer])
def get_recipes(
    db: Session = Depends(get_db),
):
    recipes = db.query(Recipe).all()
    return recipes

@app.get('/recipe/{recipe_id}', response_model=RecipeSerializer)
def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe=db.query(Recipe).where(id==recipe_id).first()
    return recipe

@app.delete('/recipe/{recipe_id}')
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db)
):
    db_obj=db.query(Recipe).where(id==recipe_id).first()
    db.delete(db_obj)
    db.commit()
    return {'message':'Recipe deleted'}