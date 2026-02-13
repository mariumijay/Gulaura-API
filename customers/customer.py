from fastapi import FastAPI, HTTPException, Path , Query
from models.schemas import Customer, UpdateCustomer
from utils.helper import load_data, save_data
import json

data_file = "data/delivery.json"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Customer API"}

@app.get("/customer_list")
def get_customer_list():
    #load the data
    data = load_data(data_file)
    return data

@app.get("/customer/{customer_id}")
def get_customer(customer_id : str):

    #load the data
    data = load_data(data_file)
    #check if the customer_id exists in the data
    if customer_id not in data:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return data[customer_id]

@app.get("/customershistory/{customer_id}")
def get_customer_history(customer_id : str = Path(..., description="The ID of the customer")):
    #load the data
    data = load_data(data_file)
    #check if the customer_id exists in the data
    if customer_id not in data:
        raise HTTPException(status_code=404, detail="Customer not found")
    #return the order history of the customer
    return data[customer_id]["order_history"]

@app.post("/create")
def create_customer(customer: UpdateCustomer):

    #load the data
    data = load_data(data_file)
    #check if the customer_id already exists in the data
    if customer.customer_id in data:
        raise HTTPException(status_code=400, detail="Customer ID already exists")
    
    #add the new customer to the data
    data[customer.customer_id] = customer.model_dump()

    #save the updated data to the file
    save_data(data)

    return {"message": "Customer created successfully"}

@app.put("/update/{customer_id}")
def update_customer(customer_id: str, customer: UpdateCustomer):

    #load the data
    data = load_data(data_file)
    #check if the customer_id exists in the data
    if customer_id not in data:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    #update the customer information in the data
    data[customer_id] = customer.model_dump()

    #save the updated data to the file
    save_data("data/customer.json")

    return {"message": "Customer updated successfully"}
