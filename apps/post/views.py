from config.settings import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Post
from flask_login import login_required, current_user
from .forms import PostForm

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
@login_required
def new():
    form = PostForm()
    return render_template("posts/new.html.jinja", form=form)


@post_bp.route("/create", methods=["POST"])
@login_required
def create():
    form = PostForm(request.form)

    if form.validate():
        title = form.title.data
        content = form.content.data

        post = Post(title=title, content=content)
        post.author = current_user
        db.session.add(post)
        db.session.commit()

        flash("新增文章成功！")
        return redirect(url_for("post.index"))

    return render_template("posts/new.html.jinja", form=form)


@post_bp.route("/<int:id>/edit")
@login_required
def edit(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()
    form = PostForm(obj=post)
    return render_template("posts/edit.html.jinja", post=post, form=form)


@post_bp.route("/<int:id>/update", methods=["POST"])
@login_required
def update(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()
    form = PostForm(request.form, obj=post)

    if form.validate():
        form.populate_obj(post)
        db.session.commit()

        flash("文章更新成功！")
        return redirect(url_for("post.show", id=id))

    return render_template("posts/edit.html.jinja", post=post, form=form)


@post_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()

    db.session.delete(post)
    db.session.commit()

    flash("文章已刪除")
    return redirect(url_for("post.index"))
