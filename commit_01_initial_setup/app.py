Commit 1: Initial Flask CBT application setup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Mini CBT System"

if __name__ == "__main__":
    app.run(debug=True)
