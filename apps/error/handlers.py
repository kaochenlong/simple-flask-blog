from flask import Blueprint, render_template

error_bp = Blueprint("error", __name__)


@error_bp.app_errorhandler(404)
def page_not_found(_):
    return render_template("errors/404.html.jinja"), 404
