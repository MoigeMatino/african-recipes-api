from typing import List, Optional

from pydantic import BaseModel


class RecipeCreateSerializer(BaseModel):
    id: str
    title: str
    description: str
    instructions: str
    prep_time: int
    cooking_time: int
    serving: int
    image_url: str
    ingredients: List[str]# TODO: amend the type with the ingredients serializer
    tags: Optional[List[str]]
    

    class Config:
        orm_mode = True


class RecipeSerializer(BaseModel):
    title: str
    description: str
    instructions: str
    prep_time: int
    cooking_time: int
    serving: int
    image_url: str
    ingredients: List[str]# TODO: amend the type with the ingredients serializer
    tags: Optional[List[str]]
    comments: List[str] # TODO: amend the type with the comment serializer

    # allows pydantic to create orm objects from pydantic objects
    class Config:
        orm_mode = True
