from flask import Blueprint, render_template, request, redirect, flash, url_for
from models import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/sign_up")
def new():
    return render_template("users/new.html.jinja")


@user_bp.route("/create", methods=["POST"])
def create():
    pass
