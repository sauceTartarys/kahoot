from flask import *

from DBManager import DBManager

app = Flask("Kahoot")
db_name = "kahoot.db"
app.secret_key = "123"


@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    print(quizzes)
    return render_template("index.html",quizzes=quizzes)

@app.route("/about_us")
def hernandes():
    return render_template("hernandes.html")

@app.route("/quizz/<int:quizz_id>")
def get_question(quizz_id):
    db_manager = DBManager(db_name)
    questions = db_manager.get_questions(quizz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0

    return redirect(url_for("show_question", quizz_id=quizz_id))

@app.route("/quizz/<int:quizz_id>/question")
def show_question(quizz_id):
    nomer = session["quest_index"]
    q = session["questions"][nomer]
    db_manager = DBManager(db_name)
    options = db_manager.get_options(q[0])

    return  str(q) + "<br>" + str(options)




app.run()
