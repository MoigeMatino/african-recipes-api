from typing import List

from pydantic import BaseModel


class RecipeCreateSerializer(BaseModel):
    id: str
    serving: int
    ingredients: List[str]
    instructions: str

    class Config:
        orm_mode = True


class RecipeSerializer(BaseModel):
    title: str
    serving: int
    ingredients: List[str]
    instructions: str

    # allows pydantic to create orm objects from pydantic objects
    class Config:
        orm_mode = True
