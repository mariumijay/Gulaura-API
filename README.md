# 🌸 Gulara Flower Shop API

A modular FastAPI backend system for managing flower inventory, customer orders, delivery tracking, and sales analytics.  
Built using RESTful architecture, Pydantic validation, and a structured project design suitable for real world backend and ML API workflows.

---

## 🎯 Project Overview

Gulara Flower Shop API is a complete backend solution designed to handle:

- 🌹 Flower inventory with categories and pricing
- 📦 Order creation and tracking
- 👥 Customer management
- 🚚 Delivery status updates
- 💐 Bouquet and arrangement management
- 📊 Sales analytics and reporting

---

## 🛠 Tech Stack

- FastAPI
- Python
- Uvicorn
- Pydantic
- REST API Design
- JSON Data Storage
- Type Hinting

---

## ⚙️ Features

- RESTful CRUD operations
- Modular architecture with separated modules
- Path and query parameters for filtering
- Input and output validation using Pydantic
- Proper HTTP status codes
- Error handling using HTTPException
- Partial updates for orders and deliveries
- Clean and scalable backend structure
  
## 📁 Project Structure
---
GULARA-FLOWER-SHOP/
│
├── inventory/
├── orders/
├── customers/
├── delivery/
├── analytics/
├── data/
├── models/
├── utils/
│
├── main.py
├── .env
└── README.md

---

---

## 📡 API Endpoints & Screenshots

### 🌹 Inventory Endpoints

![Inventory](screenshots/inventory.png)

**GET /inventory**  
_List all flowers in inventory_  
![GET Inventory](screenshots/get_inventory.png)

**POST /inventory/create**  
_Add a new flower_  
![POST Inventory](screenshots/post_inventory.png)

**PUT /inventory/update/{flower_id}**  
_Update existing flower_  
![PUT Inventory](screenshots/put_inventory.png)

**DELETE /inventory/delete/{flower_id}**  
_Delete a flower_  
![DELETE Inventory](screenshots/delete_inventory.png)

---

### 📦 Orders Endpoints

![Orders](screenshots/orders.png)

**GET /orders**  
_List all orders_  
![GET Orders](screenshots/get_orders.png)

**POST /orders/create**  
_Create a new order_  
![POST Orders](screenshots/post_orders.png)

**PUT /orders/update/{order_id}**  
_Update an existing order_  
![PUT Orders](screenshots/put_orders.png)

**DELETE /orders/delete/{order_id}**  
_Delete an order_  
![DELETE Orders](screenshots/delete_orders.png)

---

### 👥 Customers Endpoints

**GET /customers**  
_List all customers_  
![GET_Customers](screenshots/get_customers.png)


---

### 🚚 Delivery Endpoints

**GET /delivery**  
_List all deliveries_  
![Delivery](screenshots/delivery.png)

**POST /delivery/create**  
_Add a new delivery_  
![POST Delivery](screenshots/post_delivery.png)

**PUT /delivery/update/{delivery_id}**  
_Update delivery status_  
![PUT Delivery](screenshots/put_delivery.png)

---

## 🚀 Installation

### 1. Clone the repository
> git clone https://github.com/mariumijay/Gulaura-API.git

> cd Gulaura-API

### 2. Create virtual environment
> python -m venv venv

### 3. Activate environment
Windows:
> venv\Scripts\activate


Mac/Linux:
> source venv/bin/activate


### 4. Install dependencies
> pip install fastapi uvicorn


---

## ▶️ Run the Server
> http://127.0.0.1:8000

Swagger Docs:
> http://127.0.0.1:8000/docs


---

## 📡 Example API Endpoints

- GET /flowers
- POST /orders
- GET /customers
- PUT /delivery/{id}
- GET /analytics/report

---

## 📌 Future Improvements

- Database integration (PostgreSQL or SQLite)
- Authentication and authorization
- Image upload for bouquets
- Machine learning based recommendations
- Async processing
- Logging and middleware

---

## 👩‍💻 Author

Marium  
BS Computer Science | Backend and AI Enthusiast

---

## 📄 License

This project is for educational and portfolio purposes.

