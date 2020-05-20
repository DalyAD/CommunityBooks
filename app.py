import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "CommunityBooks"
app.config["MONGO_URI"] = "mongodb+srv://dalyad:DS47@myfirstcluster-f5w6l.mongodb.net/CommunityBooks?retryWrites=true&w=majority"


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    return render_template("books.html", booklist=mongo.db.books.find())


@app.route("/edit_book/<book_id>")
def edit_book(book_id):
    """edits a book"""
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("editbook.html", book=the_book)


@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    book = mongo.db.books
    book.update({'_id': ObjectId(book_id)},
                {
        'author': request.form.get('author'),
        'title': request.form.get('title'),
        'plot': request.form.get('plot'),
        'year_published': request.form.get('year_published'),
        'pages': request.form.get('pages')
    })
    return redirect(url_for('books'))


@app.route("/addbook")
def addbook():
    return render_template("addbook.html")


@app.route("/insert_book", methods=["POST"])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for("books"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
