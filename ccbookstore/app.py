from flask import Flask, render_template, request

# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]
categories = [
    {"id": 1, "name": "Fiction"},
    {"id": 2, "name": "Science"},
    {"id": 3, "name": "History"},
    {"id": 4, "name": "Crime"}
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]
books = [
    {"bookId": 1, "categoryId": 1, "title": "Alice in Wonderland", "author": "Lewis Carroll",
     "isbn": "9780582534148", "price": 12.99, "image": "aliceland.jpg", "readNow": 1},

    {"bookId": 2, "categoryId": 1, "title": "Pride and Prejudice", "author": "Jane Austen",
     "isbn": "9780141439518", "price": 10.50, "image": "pride.jpg", "readNow": 0},

    {"bookId": 3, "categoryId": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
     "isbn": "9780743273565", "price": 14.25, "image": "gatsby.jpg", "readNow": 1},

    {"bookId": 4, "categoryId": 1, "title": "1984", "author": "George Orwell",
     "isbn": "9780451524935", "price": 9.99, "image": "1984.jpg", "readNow": 0},

    {"bookId": 5, "categoryId": 2, "title": "Quarks", "author": "Harald Fritzsch",
     "isbn": "9780713915334", "price": 14.99, "image": "quarks.jpg", "readNow": 1},

    {"bookId": 6, "categoryId": 2, "title": "Cosmos", "author": "Ann Druyan",
     "isbn": "9780345539434", "price": 19.50, "image": "cosmos.jpg", "readNow": 1},

    {"bookId": 7, "categoryId": 2, "title": "A Brief History of Time", "author": "Stephen Hawking",
     "isbn": "9780553380163", "price": 16.00, "image": "historyoftime.jpg", "readNow": 0},

    {"bookId": 8, "categoryId": 2, "title": "The Selfish Gene", "author": "Richard Dawkins",
     "isbn": "9780199291151", "price": 15.75, "image": "selfishgene.jpg", "readNow": 1},

    {"bookId": 9, "categoryId": 4, "title": "Case Book of Sherlock Holmes", "author": "Arthur Conan Doyle",
     "isbn": "9780486810133", "price": 11.25, "image": "sherlock.jpg", "readNow": 0},

    {"bookId": 10, "categoryId": 3, "title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari",
     "isbn": "9780062316097", "price": 18.99, "image": "sapiens.jpg", "readNow": 1},

    {"bookId": 11, "categoryId": 3, "title": "The Silk Roads", "author": "Peter Frankopan",
     "isbn": "9781101912379", "price": 17.50, "image": "silkroads.jpg", "readNow": 0},

    {"bookId": 12, "categoryId": 3, "title": "Guns, Germs, and Steel", "author": "Jared Diamond",
     "isbn": "9780393317558", "price": 16.95, "image": "guns.jpg", "readNow": 1},

    {"bookId": 13, "categoryId": 3, "title": "The Wright Brothers", "author": "David McCullough",
    "isbn": "9781476728759", "price": 17.00, "image": "wrightbrothers.jpg", "readNow": 0},

    {"bookId": 14, "categoryId": 4, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson",
     "isbn": "9780307454546", "price": 11.95, "image": "dragontattoo.jpg", "readNow": 0},

    {"bookId": 15, "categoryId": 4, "title": "The Da Vinci Code", "author": "Dan Brown",
     "isbn": "9780307474278", "price": 13.50, "image": "davinci.jpg", "readNow": 1},

    {"bookId": 16, "categoryId": 4, "title": "The Silence of the Lambs", "author": "Thomas Harris",
     "isbn": "9780312924584", "price": 10.75, "image": "lambs.jpg", "readNow": 0}
]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)

@app.route('/category/<int:categoryId>')
def category(categoryId):
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    selected_books = [b for b in books if b["categoryId"] == categoryId]

    return render_template(
        "category.html",
        categories=categories,
        books=selected_books,
        selectedCategory=categoryId
    )

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template("search.html")

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e)# render the edit template

if __name__ == "__main__":
    app.run(debug=True)
