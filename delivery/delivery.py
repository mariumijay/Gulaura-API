from fastapi import FastAPI , Path
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from models.schemas import Delivery, UpdateDelivery
from utils.helper import load_data , save_data
import json

data_file = "data/delivery.json"

app = FastAPI()
   
@app.get("/")
def home():
    return {"message": "Welcome to the delivery service!"}

@app.get("/status/{delivery_id}")
def get_delivery_status(delivery_id: str = Path(..., description="The ID of the delivery to retrieve status for")):

    #load the delivery details from the database using delivery_id
    data = load_data(data_file)
    #check if the delivery_id exists in the data
    if delivery_id not in data:
        raise HTTPException(status_code=404, detail="Delivery not found")
    #retrieve the delivery status
    delivery_status = data[delivery_id].get("delivery_status")

    return delivery_status


@app.put("/update/{delivery_id}")
def update_delivery(delivery_id: str, update: UpdateDelivery):
    #load the delivery details from the database using delivery_id
    data = load_data(data_file)
    #check if the delivery_id exists in the data
    delivery_id = str(delivery_id)
    if delivery_id not in data:
        raise HTTPException(status_code=404, detail="Delivery not found")
    #existing delivery details
    delivery_details = data[delivery_id]
    #update the delivery status
    updates = update.model_dump(exclude_unset=True)
    delivery_details.update(updates)

    #save the updated delivery details back to the database
    save_data(data)


    # Here you would typically update the delivery status in your database
    return {
        "message": f"Delivery {delivery_id} status updated to {delivery_details.get('delivery_status','N/A')}",
        "updated_details": delivery_details
    }

@app.post("/create")
def create_delivery(delivery: Delivery):
    #load the delivery details from the database
    data = load_data(data_file)
    #check if the order_id exists in the data
    if delivery.delivery_id  in data:
        raise HTTPException(status_code=400, detail="Delivery with this ID already exists")
    #add the new delivery to the data
    data[delivery.delivery_id] = delivery.model_dump()
    #save the updated data back to the database
    save_data(data_file, data)

    return {"message": "Delivery created successfully"}