from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.jwttoken import create_access_token
from app.hashing import Hash
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.database import add_user
from app.database import retrieve_user
from app.hashing import Hash

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


# Our root endpoint
@app.get("/")
def read_root():
	return {"data":"Hello OWrld"}

# Signup endpoint with the POST method
@app.post("/signup/google")
async def signup( body: dict ) -> dict:
    profileObj = body['profileObj']
    email = profileObj['email']
    fullname = profileObj['name']

    # tokenObj = body['tokenObj']
    # token = tokenObj['access_token']

    exist = await retrieve_user(email=email)
    if exist:
        pass
    else:
        user = dict()
        user['email'] = email
        user['fullname'] = fullname

        hashfunc = Hash()
        user['password'] = hashfunc.bcrypt('123456789')

        newUser = jsonable_encoder(user)
        await add_user(newUser)

    data = dict()
    data['email'] = email
    data['fullname'] = fullname
    jwtToken = create_access_token(data)
    return {"jwtToken": jwtToken }