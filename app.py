from flask import Flask, render_template, request, redirect, url_for
from models import Question
from collections import deque
from datetime import datetime

app = Flask(__name__)

q1 = Question("What is 2 + 2?", ["1","2","3","4"], "4")
q2 = Question("Capital of France?", ["London","Paris","Rome","Berlin"], "Paris")
q3 = Question("Python is a ?", ["Snake","Programming Language","Car","Game"], "Programming Language")

question_queue = deque([q1,q2,q3])

score = 0
current_question = None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    global score
    global current_question

    if request.method == "POST":
        user_answer = request.form["answer"]

        if current_question.check_answer(user_answer):
            score += 1

    if question_queue:
        current_question = question_queue.popleft()
        return render_template("quiz.html", question=current_question)

    return redirect(url_for("result"))

@app.route("/result")
def result():
    time = datetime.now()
    return render_template("result.html", score=score, time=time)

if __name__ == "__main__":
    app.run(debug=True)