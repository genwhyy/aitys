from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from database import Base


## These are models taken from Lecture 7
# Nothing new here though 

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False) # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    user_sname = Column(String(255))
    password = Column(String(255), nullable=False)

   


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")