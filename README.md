# Book Lending API

A RESTful Book Lending API built with FastAPI and PostgreSQL.

## Features

- Create and add books to the library.
- Retrieve all books.
- Retrieve a single book by ID.
- Update book information.
- Delete books.
- Borrow available books.
- Return borrowed books.
- Track book availability.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Running the Project

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Configure your PostgreSQL database connection.
5. Start the server:

   `uvicorn tryout:app --reload`

6. Visit `http://127.0.0.1:8000/docs` to explore the API.

## Author

Atinuke Mary Towoju