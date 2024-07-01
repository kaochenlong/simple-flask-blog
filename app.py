from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/posts")
def index():
    return render_template("posts/index.html.jinja")

if __name__ == "__main__":
    app.run(port=9527, debug=True)
