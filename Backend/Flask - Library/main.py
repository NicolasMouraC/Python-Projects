from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db' # load the configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Significant overhead if True. Future default: False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

@app.route('/')
def home():
    all_books = db.session.query(Book).all() # Turn sql into a list
    return render_template('index.html', elements=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
        # all_books.append({'title': request.form['name'],
        #                   'author': request.form['author'],
        #                   'rating': request.form['rating']})
        # print(all_books)
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id') # Get hold of an url parameter
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)

@app.route('/delete')
def delete():
    book_to_delete = Book.query.get(request.args.get('id'))
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

