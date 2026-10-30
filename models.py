from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from database import Base



# class Book(Base):
#     __tablename__ = "book_lending"

#     id = Column(Integer, primary_key = True, nullable = False)
#     title = Column(String, nullable = False)
#     author = Column(String, nullable = False)
#     genre = Column(String, nullable = False)
#     is_available = Column(Boolean, server_default = text('True'), default = True, nullable = False)
#     created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text("now()"))


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    author = Column(String, nullable = False)
    genre = Column(String, nullable = False)
    is_available = Column (Boolean, default = True, nullable = False, server_default = text('true'))
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text("now()"))
    