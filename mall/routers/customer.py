from typing import List
from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, select
from mall.models import Advertising, AdvertisingInput
from mall.database import get_db
import joblib
from mall.routers.user import auth_handler


router = APIRouter()

estimator_rf_model_loaded = joblib.load("mall/saved_models/pipline_model.pkl")


# prediction function
def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]


def insert_advertising(request, prediction, client_ip,username, db):
    new_advertising = Advertising(
        TV=request["TV"],
        Radio=request['Radio'],
        Newspaper=request['Newspaper'],
        prediction=prediction,
        client_ip=client_ip,
        username=username
    )

    with db as session:
        session.add(new_advertising)
        session.commit()
        session.refresh(new_advertising)

    return new_advertising

#Predictions create
@router.post('/protected/advertising_pred')
async def predict_advertising(request: AdvertisingInput, fastapi_req: Request,
                              username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    prediction = make_advertising_prediction(estimator_rf_model_loaded, request.dict())
    db_insert_record = insert_advertising(request=request.dict(), prediction=prediction,
                                          client_ip=fastapi_req.client.host,username=username,
                                          db=db)
    return {"prediction": prediction, "db_record": db_insert_record, "username": username}

#Username get
@router.get("/advertising/{username}")
async def get_by_username(username: str, session: Session = Depends(get_db), auth=Depends(auth_handler.auth_wrapper)):
    with session:
        if not auth:
            return f"not found"
        customer_here = session.query(Advertising).filter(Advertising.username == username).first()
        if not customer_here:
            return f"Customer with username: {username} was not found."
        return customer_here

#All username
@router.get("/advertising")
async def get_customer(session: Session = Depends(get_db),username=Depends(auth_handler.auth_wrapper)):
    with session:
        if not username:
            return f"not found"
        customer_all = session.exec(select(Advertising)).all()
        return customer_all


# Delete username
@router.delete("/advertising/{username}")
async def delete_customer(username: str, session: Session = Depends(get_db), auth=Depends(auth_handler.auth_wrapper)):
    with session:
        if not auth:
            return f"not found"
        customer_new1 = session.query(Advertising).filter(Advertising.username == username).first()
        if not customer_new1:
            return f"Customer {username} fatal error"
        session.delete(customer_new1)
        session.commit()
        return {"delete": True}


