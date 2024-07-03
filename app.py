from flask import Flask, render_template, redirect, url_for, request
import os
from config.settings import db
from flask_migrate import Migrate
import models

app = Flask(__name__)


@app.route("/")
@app.route("/posts")
def index():
    return render_template("posts/index.html.jinja")


@app.route("/posts/new")
def new():
    return render_template("posts/new.html.jinja")


@app.route("/posts/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")

    post = models.Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for("index"))


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ROOT_PATH}/db/blog.sqlite"
db.init_app(app)
Migrate(app, db)

if __name__ == "__main__":
    app.run(port=9527, debug=True)
