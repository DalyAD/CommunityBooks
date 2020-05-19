import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    return render_template("books.html")


@app.route("/editbook")
def editbook():
    return render_template("editbook.html")


@app.route("/addbook")
def addbook():
    return render_template("addbook.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
