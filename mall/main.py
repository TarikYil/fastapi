from fastapi import FastAPI, status, Depends
from mall.models import Customer, CreateUpdateCustomer
from mall.database import get_db, engine
from sqlmodel import Session, SQLModel

app = FastAPI()


# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Create new customer
@app.post("/customers")
async def create_customer(request: CreateUpdateCustomer, session: Session = Depends(get_db)):
    new_customer = Customer(
        Gender=request.Gender,
        Age=request.Age,
        AnnualIncome=request.AnnualIncome,
        SpendingScore=request.SpendingScore
    )
    with session:
        session.add(new_customer)
        session.commit()
        session.refresh(new_customer)
        return new_customer