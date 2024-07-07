from config.settings import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Post

post_bp = Blueprint("post", __name__)


@post_bp.route("/")
def index():
    posts = Post.query.order_by(-Post.id).all()
    return render_template("posts/index.html.jinja", posts=posts)


@post_bp.route("/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.html.jinja", post=post)


@post_bp.route("/new")
def new():
    return render_template("posts/new.html.jinja")


@post_bp.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")

    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    flash("新增文章成功！")

    return redirect(url_for("post.index"))


@post_bp.route("/<int:id>/edit")
def edit(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/edit.html.jinja", post=post)


@post_bp.route("/<int:id>/update", methods=["POST"])
def update(id):
    post = Post.query.get_or_404(id)

    post.title = request.form.get("title")
    post.content = request.form.get("content")

    db.session.commit()

    flash("文章更新成功！")
    return redirect(url_for("post.show", id=id))


@post_bp.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    flash("文章已刪除")
    return redirect(url_for("post.index"))
