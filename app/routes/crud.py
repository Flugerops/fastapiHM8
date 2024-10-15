from typing import List
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from ..db import AsyncDB, Movie
from .. import app


@app.get("/movies", response_model=List[Movie])
async def get_all_movies(session: Session = Depends(AsyncDB.get_session)):
    movies = session.scalars(select(Movie)).all()
    movies = [Movie.model_validate(movie) for movie in movies]
    return movies

@app.post("/movies", response_model=Movie, status_code=201)
async def create_movie(data: Movie, session: Session = Depends(AsyncDB.get_session)):
    movie = Movie(**data.model_dump())
    session.add(movie)
    return movie

@app.get("/movie/{id}", response_model=Movie)
async def get_movie(id: int, session: Session = Depends(AsyncDB.get_session)):
    movie = session.scalar(select(Movie).where(Movie.id == id))
    return movie

@app.delete("/movie/{id}", response_model=Movie)
async def delete_movie(id: int, session: Session = Depends(AsyncDB.get_session)):
    movie = session.scalar(select(Movie).where(Movie.id == id))
    if movie:
        session.delete(movie)
    else:
        raise HTTPException(status_code=404)
    return movie