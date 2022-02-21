from operator import mod
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.jwttoken import create_access_token
from app.hashing import Hash
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.database import add_user
from app.database import retrieve_user
from app.hashing import Hash
from fastapi import Depends, FastAPI, HTTPException

# SQL Connection
import app.schema as schema
import app.model as model
import app.curd as curd
from app.database import SessionLocal, engine
import app.model as model
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Request


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# SQL Operation
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Our root endpoint
@app.get("/")
def read_root():
	return {"data":"Hello OWrld"}

# Signup endpoint with the POST method in MongoDB
@app.post("/signup/google")
async def signup( body: dict ) -> dict:
    profileObj = body['profileObj']
    email = profileObj['email']
    fullname = profileObj['name']
    
    hashfunc = Hash()
    password = hashfunc.bcrypt('123456789')
    # tokenObj = body['tokenObj']
    # token = tokenObj['access_token']

    exist = await retrieve_user(email=email)
    if exist:
        pass
    else:
        user = dict()
        user['email'] = email
        user['fullname'] = fullname
        user['password'] = password

        newUser = jsonable_encoder(user)
        await add_user(newUser)

    data = dict()
    data['email'] = email
    data['fullname'] = fullname
    jwtToken = create_access_token(data)
    return {"jwtToken": jwtToken }



# Signup endpoint with the POST method in SQL
# @app.post("/signup/google")
# async def signup( body: dict, db: Session = Depends(get_db) ):
#     profileObj = body['profileObj']
#     email = profileObj['email']
#     fullname = profileObj['name']
#     hashfunc = Hash()
#     password = hashfunc.bcrypt('123456789')
#     # # tokenObj = body['tokenObj']
#     # # token = tokenObj['access_token']

#     user = dict()
#     user['email'] = email
#     user['fullname'] = fullname
#     user['password'] = password
#     newUser = jsonable_encoder(user)

#     exist = curd.get_user_by_email(db, email=newUser['email'])
#     if exist:
#         pass
#     else:
#         curd.create_user(db=db, user=newUser)
#     data = dict()
#     data['email'] = email
#     data['fullname'] = fullname
#     jwtToken = create_access_token(data)
#     return {"jwtToken": jwtToken }
