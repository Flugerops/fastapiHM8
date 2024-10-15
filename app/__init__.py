import uvicorn
from fastapi import FastAPI
from .db import AsyncDB


app = FastAPI(debug=True)

from . import routes


def main():
    AsyncDB.migrate()
    uvicorn.run(app)
    