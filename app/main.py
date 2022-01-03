import io

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/random_cat")
def random_cat():
    cat_response = requests.get("https://aws.random.cat/meow")
    return StreamingResponse(io.BytesIO(cat_response.content), media_type="image/jpg")


@app.get("/random_dog")
def random_dog():
    dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
    return StreamingResponse(io.BytesIO(dog_response.content), media_type="image/jpg")
