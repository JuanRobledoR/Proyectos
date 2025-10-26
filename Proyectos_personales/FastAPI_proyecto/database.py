from sqlalchemy import create_engine
from sqlalchgemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL para la conexión con la BD al programa
SQLALCHEMY_DATABASE_URL = "postgresql://juan:juanito123@localhost:5432/prueba1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

