from sqlmodel import table
from .basemodel import BaseModel


class Movie(BaseModel, table=True):
    # __tablename__ = "movies"
    name: str
    description: str