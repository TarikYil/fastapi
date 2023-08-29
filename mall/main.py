from fastapi import FastAPI, status, Depends
from mall.models import Customer, CreateUpdateCustomer
from mall.database import get_db, engine
from sqlmodel import Session, SQLModel, select

app = FastAPI()


# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Get customer
@app.get("/customers/{id}")
async def get_by_id(id: int, session: Session = Depends(get_db)):
    with session:
        customer_here = session.get(Customer, id)
        if not customer_here:
            return f"Customer with id: {id} has not found."
        return customer_here


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

# Delete customer
@app.delete("/customers/{id}")
async def delete_customer(id: int, session: Session= Depends(get_db)):
    with session:
        customer_new1= session.get(Customer, id)
        if not customer_new1:
            return f"Customer {id} fatal error"
        session.delete(customer_new1)
        session.commit()
        return {"delete": True}


# Update customer
@app.put("/customers/{id}")
async def update_customer(id: int, request: CreateUpdateCustomer, session: Session= Depends(get_db)):
    with session:
        customer_up= session.get(Customer, id)
        if not customer_up:
            return f"Customer {id} fatal error"
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(customer_up, key, value)
        session.add(customer_up)
        session.commit()
        session.refresh(customer_up)
        return customer_up