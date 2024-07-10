import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask

load_dotenv()

ROOT_PATH = Path().parent.absolute()
TEMPLATE_FOLDER = ROOT_PATH / "templates"
DB_PATH = ROOT_PATH / "db" / "blog.sqlite"

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.secret_key = os.getenv("APP_SECRET_KEY")
