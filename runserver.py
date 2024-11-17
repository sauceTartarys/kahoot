from flask import *

from DBManager import DBManager

app = Flask("Kahoot")
db_name = "kahoot.db"


@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    print(quizzes)
    return render_template("index.html",quizzes=quizzes)

@app.route("/about_us")
def hernandes():
    return render_template("hernandes.html")




app.run()
