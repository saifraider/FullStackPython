from database import Base, metadata
from sqlalchemy import Table


class Timepass(Base):
    __table__ = Table('timepass', metadata, autoload=True)