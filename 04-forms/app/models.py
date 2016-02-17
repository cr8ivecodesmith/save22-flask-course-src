from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return '<{self.__class__.__name__}: {self.id}>'.format(self=self)


class Location(BaseModel):
    __tablename__ = 'location'
    name = Column(String(128), nullable=False)


class User(BaseModel):
    __tablename__ = 'user'
    username = Column(String(128), nullable=False, unique=True)
    first_name = Column(String(128))
    last_name = Column(String(128))


class VisitLog(BaseModel):
    __tablename__ = 'visitlog'
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship('Location')
    message = Column(Text)


if __name__ == '__main__':
    from sql_play import play
    play()
