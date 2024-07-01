from flask import Flask, render_template, redirect, url_for

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
    # 寫入資料庫，待會做...
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=9527, debug=True)
