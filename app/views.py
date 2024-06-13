from app import app
from flask import render_template


@app.route("/")
@app.route("/store")
def store_index() -> str:
    return "<p>Hello World!</p>"

