from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Literal,Optional
from models.schemas import Order, UpdateOrder
from utils.helper import load_data , save_data
import json

data_file = "data/orders.json"

app =FastAPI()

@app.get("/home")
def home():
        return {'message' : 'Welcome to the Gulaura`s Order Management System'}

@app.get("/order_list")
def get_order_list():
        #load order data from the JSON file
        data = load_data(data_file)
        return data

@app.get('/order/{order_id}')
def get_order(order_id: str = Path(..., description="ID of the order")):

        #load order data from the JSON file
        data = load_data(data_file)
        #check if order with the given ID not exists in the orders
        if order_id not in data:
                raise HTTPException(status_code=404, detail="Order not found")
        #check if order with the given ID exists in the orders
        if order_id in data:
                return data[order_id]
        
        return JSONResponse(status_code=200, content={"order_id": order_id, "status": "Order details would be here"})

@app.get("/sort")
def  sort_orders(sortby: str = Query(..., description="Field to sort orders by")):

        #load data from the JSON file
        data = load_data(data_file)
        #fields
        fields = ["order_id","delivery_status","order_date","total_price"]
        #check if sort_by is a valid field in the order data
        if sortby not in fields:
                raise HTTPException(status_code=400, detail="Invalid sort field")
        #sort the orders based on the specified field
        if sortby =="order_date":
                sorted_orders = dict(sorted(data.items(), key=lambda x: x[1][sortby]))
        elif sortby =="total_price":
                sorted_orders = dict(sorted(data.items(), key=lambda x: x[1][sortby], reverse=True))
        elif sortby =="delivery_status":
                delivery_status_order = {"Pending": 1, "Delivered": 2, "In Transit": 3}
                sorted_orders = dict(sorted(data.items(), key=lambda x: delivery_status_order.get(x[1][sortby], 4)))
        elif sortby =="order_id":
                #sorted_orders = dict(sorted(data.items(), key=lambda x: x[1][sortby]))
                sorted_orders = dict(sorted(data.items(), key=lambda x: x[1].get(sortby, "")))
        else:
                sorted_orders = dict(sorted(data.items(), key=lambda x: x[1][sortby].lower()))

        return sorted_orders
        

@app.post("/create")
def create_order(order: Order):

        #load order data from the JSON file
        data = load_data(data_file)
        #check if order with the given ID already exists in the orders
        if order.order_id in data:
                raise HTTPException(status_code=400, detail="Order with this ID already exists")
        #add the new order to the orders
        data[order.order_id] = order.model_dump()
        #save the updated orders back to the JSON file
        save_data(data_file,data)

        return JSONResponse(status_code=201, content={"message": "Order created successfully", "order_id": order.order_id})

@app.put('/update/{order_id}')
def update_order(order_id: str, updateorder: UpdateOrder):

        #load order from the JSON file
        data = load_data(data_file) 
        #check if order with the given ID exists in the orders
        if order_id not in data:
                raise HTTPException(status_code=404, detail="Order not found")
        #extract the existing order details
        existing_order = data[order_id]
        #update the order details with the new data
        updated_order = updateorder.model_dump(exclude_unset=True)
        #update the order details in the orders
        existing_order.update(updated_order)
        #save the updated orders back to the JSON file
        save_data(data_file,data)

        return JSONResponse(status_code=200, content={"message": "Order updated successfully", "order_id": order_id})

@app.delete('/delete/{order_id}')
def delete_order(order_id: str):

        #load order from the JSON file
        data = load_data(data_file)
        #check if order with the given ID exists in the orders
        if order_id not in data:
                raise HTTPException(status_code=404, detail="Order not found")
        #remove the order from the orders
        del data[order_id]
        #save the updated orders back to the JSON file
        save_data(data_file,data)

        return JSONResponse(status_code=200, content={"message": "Order deleted successfully", "order_id": order_id})