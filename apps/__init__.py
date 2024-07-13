import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from models.user import User

load_dotenv()

ROOT_PATH = Path().parent.absolute()
TEMPLATE_FOLDER = ROOT_PATH / "templates"
DB_PATH = ROOT_PATH / "db" / "blog.sqlite"

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"
login_manager.login_message = "請登入會員帳號"


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
