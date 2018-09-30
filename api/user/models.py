from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    email_address = Column(String(255), unique=True, nullable=True)
    display_name = Column(String(255), unique=False, nullable=True)
    title = Column(String(255), unique=False, nullable=True)

    comments = relationship("Comment", backref="user", lazy=True)

    def __init__(self, email_address=None, display_name=None, title=None):
        self.email_address = email_address
        self.display_name = display_name
        self.title = title
