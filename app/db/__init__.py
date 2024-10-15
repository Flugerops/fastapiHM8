from sqlmodel import SQLModel, create_engine, Session


class AsyncDB:
    ENGINE = create_engine("sqlite:///mydb.db")
    SESSION = Session(bind=ENGINE)
    
    @classmethod
    def up(cls):
        SQLModel.metadata.create_all(cls.ENGINE)
    
    @classmethod
    def down(cls):
        SQLModel.metadata.drop_all(cls.ENGINE)
        
    @classmethod
    def migrate(cls):
        SQLModel.metadata.drop_all(cls.ENGINE)
        SQLModel.metadata.create_all(cls.ENGINE)
        
    @classmethod
    def get_session(cls):
        try:
            yield cls.SESSION
        finally:
            cls.SESSION.commit()
            cls.SESSION.close()
            
from .models import Movie