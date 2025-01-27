from sqlalchemy.orm import declarative_base
from db.connection import Connection

Base = declarative_base(Connection.connection)