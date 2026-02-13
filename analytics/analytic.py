from utils.helper import load_data, save_data
from fastapi import FastAPI, HTTPException
from models.schemas import Analytics
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Analytics API"}
