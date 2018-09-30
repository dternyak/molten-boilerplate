import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text

from db import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer(), primary_key=True)
    date_created = Column(DateTime)
    content = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    def __init__(self,  user_id, content):
        self.user_id = user_id
        self.content = content
        self.date_created = datetime.datetime.now()