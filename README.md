# fastapi-example 

A simple backend example of using Fast API in Python.
To be used with 
- https://github.com/sroy-eq/mfe-host-container
- https://github.com/sroy-eq/mfe-remote-cats
- https://github.com/sroy-eq/mfe-remote-dogs

## Preconditions:

- Python 3

## Clone the project

```
git clone https://github.com/octavian-negru/mfe-fastapi-backend-example.git
```

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```
