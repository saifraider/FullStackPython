from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

Base = declarative_base()
session = None
metadata = None
Session = None


def init_db(uri):
    global session
    global metadata
    global Session
    engine = create_engine(uri)
    metadata = MetaData(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    from project.models.users import User, Timepass

    Base.metadata.create_all(bind=engine)

    return session




