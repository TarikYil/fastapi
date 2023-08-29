from fastapi import FastAPI, status, Depends
from mall.models import Customer, CreateUpdateCustomer
from mall.database import get_db, engine
from sqlmodel import Session, SQLModel, select

app = FastAPI()


# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.get("/customers/{id}")
async def get_by_id(id: int, session: Session = Depends(get_db)):
    with session:
        customer_here = session.get(Customer, id)
        if not customer_here:
            return f"Customer with id: {id} has not found."
        return customer_here

@app.get("/customer/{id}")
async  def get_by_id(id: int, sessions: Session=Depends(get_db)):
    with sessions

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