from fastapi import FastAPI
from mall.database import engine
from sqlmodel import SQLModel
from mall.routers import customer, user

app = FastAPI()
app.include_router(customer.router)
app.include_router(user.router)

# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)