from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

def get_engine():
    engine = create_engine('sqlite:///app.sqlite3', echo=True)  # In-memory DB
    return engine


def create_db(engine):
    Base.metadata.create_all(engine)


def create_session():
    engine = get_engine()
    create_db(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add(session, instance):
    session.add(instance)
    session.commit()
    return instance

def edit(session, instance):
    session.commit()
    return instance

def delete(session, instance):
    session.delete(instance)
    session.commit()


def play():
    import pdb
    from models import Location, User, VisitLog
    session = create_session()
    pdb.set_trace()
