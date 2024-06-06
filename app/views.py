from app import app
from flask import render_template


@app.route("/store")
@app.route("/")
def store_index() -> str:
    names = ["Amy", "Clara", "Vika"]

    return render_template("index.html", page="Home", names=names)