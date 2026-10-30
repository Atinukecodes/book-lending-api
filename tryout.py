from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import models
from database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)


app = FastAPI()


class Book(BaseModel):
    title: str
    genre: str
    author: str
    is_available: bool = True



# Create a book
@app.post("/books", status_code = status.HTTP_201_CREATED)
def create_book(book: Book, db: Session = Depends(get_db)):
    new_book = models.Book(**book.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return{"data": new_book}

#Get all books
@app.get("/books", status_code = status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    all_books = db.query(models.Book).all()

    return{"data": all_books}

#Get a book
@app.get("/books/{id}", status_code = status.HTTP_200_OK)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id==id).first()

    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = "book is Non-existent")
    
    return{"data": book}

#Update a book
@app.put("/books/{id}")
def update_book(id: int, book: Book, db: Session= Depends(get_db)):

    existing_book = db.query(models.Book).filter(models.Book.id==id).first()

    if existing_book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Book does not exist"
        )

    existing_book.title = book.title
    existing_book.genre = book.genre
    existing_book.is_available = book.is_available

    db.commit()
    db.refresh(existing_book)

#Borrow a book
@app.post("/borrow/{id}/book")
def borrow_book(id: int, db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id==id).first()
    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
        detail = "No such book exist")

    if book.is_available is False:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
        detail = "Book is unavailable")

    book.is_available = False
    db.commit()
    db.refresh(book)

    return {"data": "Book successfully borrowed"}

#Return a book
@app.post("/return/{id}/book")
def return_book(id: int, db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()

    if book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "Book does not exist"
        )

    book.is_available is True

    db.commit()
    db.refresh(book)

    return {"data": "Book is successfully returned"}

@app.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)): 
    book = db.query(models.Book).filter(models.Book.id == id).first()

    if book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Book does not exist"
        )

    db.delete(book)
    db.commit()

    return{"data": "Book successfully deleted"}

