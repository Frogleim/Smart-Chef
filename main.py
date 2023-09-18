from fastapi import FastAPI, HTTPException
from core import recieps_recomenadations, get_images
import urllib.parse
from pydantic import BaseModel


class UrlInput(BaseModel):
    recipes_url: str


app = FastAPI()


@app.get('/get_recipes/{ingredients}')
def get_recipes(ingredients: str):
    recipes = recieps_recomenadations.RecSys(ingredients)
    return {'Message': "Success", "Data": recipes}


@app.post("/get_recipes_details")
def get_details(url_input: UrlInput):
    if url_input.recipes_url is None:
        return HTTPException(status_code=404, detail="Not found")
    details = get_images.get_rec_description(url_input.recipes_url)
    return {"Message": "Success", "Data": details}