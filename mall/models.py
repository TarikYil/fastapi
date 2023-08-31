from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

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


class Advertising(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    TV: float
    Radio: float
    Newspaper: float
    prediction: float
    prediction_time: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    client_ip: str
    username: str


class AdvertisingInput(SQLModel):
    TV: float
    Radio: float
    Newspaper: float

    class Config:
        schema_extra = {
            "example": {
                "TV": 230.1,
                "Radio": 37.8,
                "Newspaper": 69.2,
            }
        }