from fastapi import FastAPI
from inventory.inventory import app as inventory_app
from orders.orders import app as orders_app
from customers.customer import app as customers_app
from delivery.delivery import app as delivery_app


app = FastAPI(
    title="🌸 Gulara Flower Shop API",
    description="Complete flower shop management system",
    version="1.0.0"
)

# Mount sub-applications
app.mount("/inventory", inventory_app)
app.mount("/orders", orders_app)
app.mount("/customers", customers_app)
app.mount("/delivery", delivery_app)


@app.get("/")
def root():
    return { "message": "🌸 Welcome to Gulara Flower Shop API",
                "endpoints": {
                "inventory": "/inventory",
                "orders": "/orders",
                "customers": "/customers",
                "delivery": "/delivery",
                "analytics": "/analytics",
                "docs": "/docs"
                }
            }

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)