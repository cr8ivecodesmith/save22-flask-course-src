from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

def create_session():
    engine = create_engine('sqlite://', echo=True)  # In-memory DB
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def play():
    import pdb
    from models import Location, User, VisitLog
    session = create_session()
    pdb.set_trace()
