from app import app



@app.route("/store")
@app.route("/")
def store_index():
    return "Hello world!"