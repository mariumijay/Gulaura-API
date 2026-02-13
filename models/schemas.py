from pydantic import BaseModel, Field
from typing import Optional,Annotated,Literal

class Customer(BaseModel):
    customer_id: str =  Field(..., description="The ID of the customer to create")
    name: str = Field(..., description="The name of the customer")
    contact: str = Field(..., description="The contact information of the customer")
    address: str = Field(..., description="The address of the customer")
    order_history: list = Field(..., description="The order history of the customer")

class UpdateCustomer(BaseModel):
    name: Optional[str] = Field(default=None, description="The name of the customer")
    contact: Optional[str] = Field(default=None, description="The contact information of the customer")
    address: Optional[str] = Field(default=None, description="The address of the customer")
    order_history: Optional[list] = Field(default=None, description="The order history of the customer")

class Delivery(BaseModel):
    delivery_id: int = Field(..., description="The ID of the delivery")
    order_id: int = Field(..., description="The ID of the order")
    customer_name: str = Field(..., description="The name of the customer")
    delivery_status: str = Field(..., description="The status of the delivery")
    expected_date: str = Field(..., description="The expected delivery date")
    delivered_date: str = Field(..., description="The actual delivery date")
    delivery_person: str = Field(..., description="The name of the delivery person")

class UpdateDelivery(BaseModel):
    order_id: Optional[int] = Field(default=None, description="The ID of the order")
    customer_name: Optional[str] = Field(default=None, description="The name of the customer")
    delivery_status: Optional[str] = Field(default=None, description="The status of the delivery")
    expected_date: Optional[str] = Field(default=None, description="The expected delivery date")
    delivered_date: Optional[str] = Field(default=None, description="The actual delivery date")
    delivery_person: Optional[str] = Field(default=None, description="The name of the delivery person")
 
class Flower(BaseModel):
    flower_id: str = Field(..., description="ID of the flower", example="R001")
    name: str = Field(..., description="Name of the flower", example="Rose")
    price: float = Field(..., ge=0, description="Price of the flower", example=10.99)
    stock: int = Field(..., ge=0,description="Stock quantity of the flower", example=100)
    color: str = Field(..., description="Color of the flower", example="Red")

class UpdateFlower(BaseModel):
     name: Annotated[str | None, Field(description="Name of the flower", example="Rose")]
     price: Annotated[float | None, Field(ge=0, description="Price of the flower", example=10.99)]
     stock: Annotated[int | None, Field(description="Stock quantity of the flower", example=100)]
     color: Annotated[str | None, Field(description="Color of the flower", example="Red")]

class Order(BaseModel):
       order_id: str = Field(..., description="ID of the order", example="O001")
       customer_name: str = Field(..., description="Name of the customer", example="John Doe")
       items: dict[str,str] = Field(..., description="List of items in the order", example={"R001": "Rose", "L001": "Lily"})
       total_price: float = Field(..., ge=0, description="Total price of the order", example=29.99)    
       order_date: str = Field(..., description="Date of the order", example="2024-06-01")  
       delivery_status: Literal["Pending","Delivered","Cancelled"] = Field(..., description="Delivery status of the order", example="Pending")    
       delivery_address: str = Field(..., description="Delivery address for the order", example="123 Main St, City, Country")   
       
class UpdateOrder(BaseModel):
        customer_name: Optional[str] = Field(default=None,description="Name of the customer", example="John Doe")
        items: Optional[dict[str,str]] = Field(default=None, description="List of items in the order", example={"R001": "Rose", "L001": "Lily"})
        total_price: Optional[float] = Field(default=None, ge=0, description="Total price of the order", example=29.99)    
        order_date: Optional[str] = Field(default=None, description="Date of the order", example="2024-06-01")  
        delivery_status: Optional[Literal["Pending","Delivered","Cancelled"]] = Field(default=None, description="Delivery status of the order", example="Pending")    
        delivery_address: Optional[str] = Field(default=None, description="Delivery address for the order", example="123 Main St, City, Country")
