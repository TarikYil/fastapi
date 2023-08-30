from fastapi import FastAPI
from mall.database import engine
from sqlmodel import SQLModel
from mall.routers import customer

app = FastAPI()
app.include_router(customer.router)

# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

