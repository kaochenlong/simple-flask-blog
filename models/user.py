from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from config.settings import db
from .mixins.datetime import TimeTrackable
from flask_login import UserMixin


class User(db.Model, TimeTrackable, UserMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50), unique=True, nullable=False)
    password = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.username}"
