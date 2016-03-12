from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base


def get_engine(db=None):
    db = db or 'sqlite://'  # use in-memory db if None

    # Define what db backend to use
    engine = create_engine('{}'.format(db), echo=True)

    return engine


def create_db(engine):
    # Creates the db tables
    Base.metadata.create_all(engine)


def create_session(db=None):
    engine = get_engine(db)
    create_db(engine)

    # Initialize db session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add(session, instance):
    session.add(instance)
    session.commit()
    return instance


def update(session, instance):
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
