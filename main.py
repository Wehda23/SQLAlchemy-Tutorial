from sqlalchemy import  create_engine
from model import Base



# Create the engine
engine = create_engine("sqlite+pysqlite:///database.db", echo = True) # Naming the database and database type SQLite..



# Initiating the database schema
Base.metadata.create_all(engine)