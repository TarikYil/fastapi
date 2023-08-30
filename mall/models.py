from sqlmodel import SQLModel, Field
from typing import Optional


class Customer(SQLModel, table=True):
    CustomerID: Optional[int] = Field(default=None, primary_key=True)
    Gender: str
    Age: Optional[int] = Field(default=None)
    AnnualIncome: float
    SpendingScore: int


class CreateUpdateCustomer(SQLModel):
    Gender: Optional[str]
    Age: Optional[int]
    AnnualIncome: Optional[float]
    SpendingScore: Optional[int]


class ShowCustomer(SQLModel):
    CustomerID: int
    Gender: str
    Age: Optional[int]


class Login(SQLModel):
    username: str
    password: str


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    email: str
    password: str


class CreateUpdateUser(SQLModel):
    name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Mesut KOCAMAN",
                "username": "mlops1",
                "email": "mlops1@vbo.local",
                "password": "strongPassword"
            }
        }


class ShowUser(SQLModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Mesut KOCAMAN",
                "email": "mlops1@vbo.local"
            }
        }