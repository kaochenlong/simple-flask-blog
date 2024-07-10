from flask import Blueprint, render_template, request, redirect, flash, url_for
from .forms import UserRegisterForm
from models.user import User
from config.settings import db
from flask_bcrypt import Bcrypt
from apps import app

user_bp = Blueprint("user", __name__)
bcrypt = Bcrypt(app)


@user_bp.route("/sign_up")
def new():
    form = UserRegisterForm()
    return render_template("users/new.html.jinja", form=form)


@user_bp.route("/create", methods=["POST"])
def create():
    form = UserRegisterForm(request.form)

    if form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("註冊成功！")
        return redirect(url_for("root"))

    return render_template("users/new.html.jinja", form=form)
