from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import mapped_column
from config.settings import db
from .mixins.datetime import TimeTrackable


class Post(db.Model, TimeTrackable):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(Text)

    def __repr__(self):
        return f"{self.title}"
