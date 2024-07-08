from flask import Blueprint, render_template, request, redirect, flash, url_for
from .forms import UserRegisterForm
from models.user import User
from config.settings import db

user_bp = Blueprint("user", __name__)


@user_bp.route("/sign_up")
def new():
    form = UserRegisterForm()
    return render_template("users/new.html.jinja", form=form)


@user_bp.route("/create", methods=["POST"])
def create():
    form = UserRegisterForm(request.form)

    if form.validate():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("註冊成功！")
        return redirect(url_for("root"))

    return render_template("users/new.html.jinja", form=form)
