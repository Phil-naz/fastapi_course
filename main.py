from fastapi import FastAPI, Query, Path, Body

from schemas import *
from typing import List


#   Course: https://www.youtube.com/playlist?list=PLaED5GKTiQG8GW5Rv2hf3tRS-d9t9liUt
#   Start local sever, CMD: uvicorn main:app --reload
#   http://127.0.0.1:8000/docs
#   http://127.0.0.1:8000/redoc

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book_1')
def create_book_first(item: Book, author: Author, quantity: int = Body(...)):   # import 'Body', '...' = value required
    return {"item": item, "author": author, 'quantity': quantity}


# @app.post('/book', response_model=Book, response_model_exclude={'pages', 'date'})
# fields in 'response_model_exclude' won't be transferred from server
@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    return BookOut(**item.dict(), id=3)


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):   # '...' = value required
    return {"author": author}


@app.get('/book')
def get_book(q: List[str] = Query(..., min_length=2, max_length=6, description="Search book")):
                    # '...' = value required or type 'default value' here; import 'Query' | After ':' datatype; After '=' default value
                    # import List
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):   # import 'Path'
                    # 'gt' = min_length=2; 'le' = max_length
    return {"pk": pk, "pages": pages}