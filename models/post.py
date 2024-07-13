from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from config.settings import db
from .mixins.datetime import TimeTrackable


class Post(db.Model, TimeTrackable):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(Text)
    user_id = mapped_column(
        Integer, ForeignKey("users.id", name="fk_post_to_user_id"), nullable=False
    )
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"{self.title}"
