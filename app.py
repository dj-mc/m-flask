from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return login_user()
    else:
        return display_login_page()


@app.route("/user/<username>")
def profile(username):
    return f"<p>{escape(username)}'s page</p>"


@app.route("/post/<int:post_id>")
def user_post(post_id):
    return f"<p>id: {post_id}</p>"


@app.route("/path/<path:subpath>")
def display_subpath(subpath):
    return f"<p>subpath: {escape(subpath)}"


@app.route("/welcome/")
@app.route("/welcome/<username>")
def welcome(username=None):
    return render_template("welcome.html.j2", username=username)


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="Lemmy Luiseaux"))
    print(url_for("static", filename="style.css"))
    print(url_for("welcome", username="dj"))
