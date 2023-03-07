from pydantic import BaseModel
from typing import List

class Recipe(BaseModel):
    title: str
    serving:int
    ingredients:List[str]
    instructions:str
    
    #allows pydantic to create orm objects from pydantic objects
    class Config:
        orm_mode=True