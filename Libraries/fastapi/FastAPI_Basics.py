# ============================================================
# FASTAPI BASICS
# ============================================================
# FastAPI is a modern, fast web framework for building APIs.
# It is built on standard Python type hints.
# 
# To run this file, you will need to install fastapi and uvicorn:
# pip install fastapi uvicorn
#
# Then run: uvicorn FastAPI_Basics:app --reload
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI app
app = FastAPI(title="My First API", description="Learning FastAPI Basics", version="1.0.0")

# ============================================================
# 1. BASIC ROUTING (GET)
# ============================================================

@app.get("/")
def read_root():
    """This is the root endpoint."""
    return {"message": "Welcome to the FastAPI Basics Tutorial!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    """Endpoint with a path parameter."""
    return {"message": f"Hello, {name}!"}

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    """Endpoint with query parameters."""
    return {"message": f"Returning items from {skip} to {skip + limit}"}


# ============================================================
# 2. PYDANTIC MODELS & POST REQUESTS
# ============================================================
# Pydantic is used for data validation and parsing

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# A mock database
fake_db = {}

@app.post("/items/")
def create_item(item: Item):
    """Endpoint to create an item using a POST request."""
    # We can access item attributes like a normal object
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    
    # "Save" to db
    fake_db[item.name] = item_dict
    return {"message": "Item created successfully", "item": item_dict}


# ============================================================
# 3. PUT AND DELETE REQUESTS
# ============================================================

@app.put("/items/{item_name}")
def update_item(item_name: str, item: Item):
    """Endpoint to update an item."""
    if item_name not in fake_db:
        # Returning a 404 error if item not found
        raise HTTPException(status_code=404, detail="Item not found")
        
    fake_db[item_name] = item.dict()
    return {"message": "Item updated successfully", "item": fake_db[item_name]}

@app.delete("/items/{item_name}")
def delete_item(item_name: str):
    """Endpoint to delete an item."""
    if item_name not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
        
    del fake_db[item_name]
    return {"message": f"Item {item_name} deleted successfully"}


# ============================================================
# 4. HOW TO TEST
# ============================================================
# When the server is running, FastAPI automatically generates 
# interactive API documentation.
# Go to your browser and visit:
# 1. http://127.0.0.1:8000/docs (Swagger UI)
# 2. http://127.0.0.1:8000/redoc (ReDoc)
