from flask import Flask, render_template, redirect, url_for, request, flash, abort
import os
from config.settings import db
from flask_migrate import Migrate
from models import Post
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
@app.route("/posts")
def index():
    posts = Post.query.order_by(-Post.id).all()
    return render_template("posts/index.html.jinja", posts=posts)


@app.route("/posts/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.html.jinja", post=post)


@app.route("/posts/new")
def new():
    return render_template("posts/new.html.jinja")


@app.route("/posts/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")

    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    flash("新增文章成功！")

    return redirect(url_for("index"))


@app.route("/posts/<int:id>/edit")
def edit(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/edit.html.jinja", post=post)


@app.route("/posts/<int:id>/update", methods=["POST"])
def update(id):
    post = Post.query.get_or_404(id)

    post.title = request.form.get("title")
    post.content = request.form.get("content")

    db.session.commit()

    flash("文章更新成功！")
    return redirect(url_for("show", id=id))


@app.route("/posts/<int:id>/delete", methods=["POST"])
def delete(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    flash("文章已刪除")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html.jinja"), 404


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ROOT_PATH}/db/blog.sqlite"
app.secret_key = os.getenv("APP_SECRET_KEY")
db.init_app(app)
Migrate(app, db)

if __name__ == "__main__":
    app.run(port=9527, debug=True)
