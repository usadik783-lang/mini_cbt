from flask import Flask

app = Flask(__name__)

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

@app.route("/")
def home():
    return "Mini CBT System"

if __name__ == "__main__":
    app.run(debug=True)
