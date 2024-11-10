from flask import *

app = Flask("Kahoot")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us")
def hernandes():
    return render_template("hernandes.html")




app.run()
