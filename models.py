from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = MetaData()


class User(Base):
    __tablename__ = "user"
    metadata = metadata
    id = Column(Integer, primary_key=True, nullable=False) # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    user_sname = Column(String(255))
    password = Column(String(255), nullable=False)

   


class Post(Base):
    __tablename__ = "post"
    metadata = metadata
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

class Like(Base):
    __tablename__ = "like"
    metadata = metadata
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "post.id", ondelete="CASCADE"), primary_key=True)
    
class Subscribe(Base):
    __tablename__ = "subscribe"
    metadata = metadata
    id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)