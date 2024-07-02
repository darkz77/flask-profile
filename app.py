from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    name = request.argv.get("name", "world")
    return render_template(greet.html, name=name)