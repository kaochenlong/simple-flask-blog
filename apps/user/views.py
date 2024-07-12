from flask import Blueprint, render_template, request, redirect, flash, url_for
from .forms import UserRegisterForm, UserLoginForm
from models.user import User
from config.settings import db
from flask_bcrypt import Bcrypt
from apps import app
from flask_login import login_user, logout_user

user_bp = Blueprint("user", __name__)
bcrypt = Bcrypt(app)


@user_bp.route("/sign_up")
def new():
    form = UserRegisterForm()
    return render_template("users/new.html.jinja", form=form)


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    form = UserLoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("登入成功")
            return redirect(url_for("root"))
        else:
            flash("登入失敗，請確認後再重試一次")
    return render_template("users/login.html.jinja", form=form)


@user_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    flash("已登出！")
    return redirect(url_for("root"))


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
