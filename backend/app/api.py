from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from pydantic import BaseModel
from typing import Optional

import app.connection
from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType, EmailType

from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Request,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.jwttoken import create_access_token
from app.hashing import Hash

from app.oauth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware


class User(BaseModel):
    email: str
    username: str
class Login(BaseModel):
	username: str
	password: str
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: Optional[str] = None

# An instance of class User
# newuser = User()

# funtion to create and assign values to the instanse of class User created
def create_user(email, username):
    newuser.user_id = ObjectId()
    newuser.email = email
    newuser.name = username
    return dict(newuser)

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


from pymongo import MongoClient
mongodb_uri = 'mongodb://localhost:27017/fastapi'
port = 8000
client = MongoClient(mongodb_uri, port)
db = client["User"]




# Our root endpoint
@app.get("/")
def read_root(current_user:User = Depends(get_current_user)):
	return {"data":"Hello OWrld"}


# Signup endpoint with the POST method
@app.post("/signup/google")
def signup( body: dict ) -> dict:
    profileObj = body['profileObj']
    tokenObj = body['tokenObj']
    email = profileObj['email']
    fullname = profileObj['name']
    token = tokenObj['access_token']
    user_exists = False
    data = dict()
    data['token'] = token
    data['email'] = email
    data['fullname'] = fullname
    jwtToken = create_access_token(data)
    return {"jwtToken": jwtToken }


@app.post('/register')
def create_user(request:User):
	hashed_pass = Hash.bcrypt(request.password)
	user_object = dict(request)
	user_object["password"] = hashed_pass
	user_id = db["users"].insert(user_object)
	# print(user)
	return {"res":"created"}

@app.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends()):
	user = db["users"].find_one({"username":request.username})
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
	if not Hash.verify(user["password"],request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
	access_token = create_access_token(data={"sub": user["username"] })
	return {"access_token": access_token, "token_type": "bearer"}
    
    # print(request)
    # data = create_user(email, username, password)

    # # Covert data to dict so it can be easily inserted to MongoDB
    # dict(data)

    # # Checks if an email exists from the collection of users
    # if connection.db.users.find(
    #     {'email': data['email']}
    #     ).count() > 0:
    #     user_exists = True
    #     print("USer Exists")
    #     return {"message":"User Exists"}
    # # If the email doesn't exist, create the user
    # elif user_exists == False:
    #     connection.db.users.insert_one(data)
    #     return {"message":"User Created","email": data['email'], "name": data['name'], "pass": data['password']}
