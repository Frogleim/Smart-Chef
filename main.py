from fastapi import FastAPI
from pydantic import BaseModel
from core import recieps_recomenadations


app = FastAPI()


@app.get('/get_recipes/{ingredients}')
def get_recipes(ingredients: str):
    recipes = recieps_recomenadations.RecSys(ingredients)
    return {'Message': "Success", "Data": recipes}

