#python

#fastapi
from fastapi import APIRouter,status

#Models
from config.db import conn
from schema.userSchema import user
from models.user import User

router = APIRouter()

@router.get("/users/getuser",tags = ['Users'])
def get_user():
    return conn.execute(user.select()).fetchall()

@router.post(
    path='/users/create',
    status_code=status.HTTP_201_CREATED,
    tags= ['Users'])
def create_user(user:User):
    new_user = user.dict()
    print (new_user)
    return {"ok":'ok'}




# @router.post(
#     path =('/Tweets/create'),
#     response_model=Tweet,
#     status_code=status.HTTP_201_CREATED,
#     summary='Create a new tweet',
#     
# )