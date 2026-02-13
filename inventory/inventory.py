from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import json
from typing import Annotated
from models.schemas import Flower, UpdateFlower
from utils.helper import load_data , save_data

data_file = "data/delivery.json"

app = FastAPI()

@app.get('/')
def home():
    return {'message' : 'Welcome to the Gulaura`s Inventory Management System'}

@app.get('/all')
def get_all_inventory():
     #load inventory data from the JSON file
    data = load_data(data_file)
    return data

@app.get('/inventory/{flower_id}')
def get_inventory(flower_id: str = Path(..., description="ID of the flower")):
    
    #load inventory data from the JSON file
    data = load_data(data_file)
    #check if flower with the given ID exists in the inventory
    if flower_id not in data:
        raise HTTPException(status_code=404, detail="Flower not found in inventory")

    return data[flower_id]

@app.post("/create")
def create_flower(flower: Flower):

    #load inventory data from the JSON file
    data = load_data()
    #check if flower with the given ID already exists in the inventory
    if flower.flower_id in data:
            raise HTTPException(status_code=400, detail="Flower with this ID already exists in inventory")
    # check stock availability (Stock Validation)
    if flower.stock < 0:
         raise HTTPException(status_code=400,detail="Stock can not be negative")
    #add the new flower to the inventory
    data[flower.flower_id] = flower.dict()
    #save the updated inventory back to the JSON file
    save_data(data_file,data)

    return JSONResponse(status_code=201, content={"message": "Flower created successfully", "flower_id": flower.flower_id})

@app.put("/update/{flower_id}")
def update_flower( flower_id: str, flowers : UpdateFlower):
     #load inventory data from the JSON file
    data = load_data(data_file)
    #check if flower with the given ID exists in the inventory
    if flower_id not in data:
         raise HTTPException(status_code=404, detail="Flower not found in inventory")
    #extract current flower data
    existing_flower_data = data[flower_id]
    #update pydantic model with existing data
    updated_flower_data = flowers.model_dump(exclude_unset=True)
    #Stock Validation
    if "stock" in updated_flower_data and updated_flower_data["stock"]:
         raise HTTPException(status_code=400, detail="Stock cannot be negative")
    #update the flower data in the inventory
    existing_flower_data.update(updated_flower_data)
    #save the updated inventory back to the JSON file
    save_data(data_file,data)

    return JSONResponse(status_code=200, content={"message": "Flower updated successfully", "flower_id": flower_id})

@app.delete("/delete/{flower_id}")
def delete_flower(flower_id: str):
    #load inventory data from the JSON file
    data = load_data(data_file)
    #check if flower with the given ID exists in the inventory
    if flower_id not in data:
         raise HTTPException(status_code=404, detail="Flower not found in inventory")
    #remove the flower from the inventory
    del data[flower_id]
    #save the updated inventory back to the JSON file
    save_data(data_file,data)

    return JSONResponse(status_code=200, content={"message": "Flower deleted successfully", "flower_id": flower_id})
