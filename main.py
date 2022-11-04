from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut

from typing import List

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

# uvicorn main:app --reload
# uvicorn main:app --reload --port 8080

app = FastAPI()

@app.get('/')
def home():
    return {"key": "Hello11111"}

@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    return item

# @app.post('/book', response_model=BookOut, response_model_exclude={'pages','date'}, response_model_exclude_unset=True)  # все свойства по умолчанию должный быть исключены
# def create_book(item: Book):
#     return item

# @app.post('/book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {'item': item, "author": author, "quantity": quantity}

@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}

# @app.get('/book')
# def get_book(q: str = Query(..., description='book', regex='')): # must have value
#     return q

@app.get('/book')
def get_book(q: List[str] = Query(["test","test2"], description='book', regex='', deprecated=True)):
    return q

# проверки путей
@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=1, le=20)):
    return {'pk': pk}
