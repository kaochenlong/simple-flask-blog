import os
from flask import Flask
from config.settings import db
from flask_migrate import Migrate
from dotenv import load_dotenv
from apps.post.views import post_bp
from apps.error.handlers import error_bp

load_dotenv()

app = Flask(__name__)
app.register_blueprint(post_bp)
app.register_blueprint(error_bp)

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ROOT_PATH}/db/blog.sqlite"
app.secret_key = os.getenv("APP_SECRET_KEY")
db.init_app(app)
Migrate(app, db)

if __name__ == "__main__":
    app.run(port=9527, debug=True)
