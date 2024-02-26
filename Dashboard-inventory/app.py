from flask import Flask, request, render_template, login_required, logout_required, redirect, url_for, session, users, abort
from SQLAlchemy import SQLAlchemy
from models import db, BookModel

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dashboard'

@app.route("/")
@login_required
def login():

    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route("/post/new")
@logout_required 
def new_post():
    return render_template('create_post.html', title='New Post')

@app.route('/book/<int:plate>', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        return render_template('bookpage.html')
    
    if request.method == 'POST':
        book_id = request.form['book_id']
        ISBN_number = request.form['ISBN_number']
        author = request.form['author']
        title = request.form['title']
        length = request.form['gas']
        type = request.form['type']
        book = BookModel(book_id=book_id, ISBN_number=ISBN_number, author=author, title=title, length=length, type=type)
        db.session.add(book)
        db.session.commit()
        return redirect('/book')

    
@app.route('/book')
def RetrieveBookList():
    books = BookModel.query.all()
    return render_template('booklist.html',books=books)


@app.route('/book/<int:id>')
def RetrieveSingleBook(id):
    book = BookModel.query.filter_by(book_id=id).first()
    if book:
        return render_template('book.html', book = book)
    return f"Book with id={id} Doesn't exist"


@app.route('/book/<int:id>/update',methods = ['GET', 'POST'])
def update(id):
    book = BookModel.query.filter_by(book_id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit

            ISBN_number = request.form['ISBN_number']
            author = request.form['model']
            title = request.form['title']
            length = request.form['length']
            type = request.form['type']
            book = BookModel(book_id=id, ISBN_number=ISBN_number, author=author, title=title, length=length, type=type)

            db.session.add(book)
            db.session.commit()
            return redirect(f'/book/{id}')
        return f"Book with id = {id} Does not exist"

    return render_template('update.html', book = book)


@app.route('/book/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    book = BookModel.query.filter_by(book_id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            return redirect('/book')
        abort(404)

    return render_template('delete.html')
            
if __name__ == '__main__':
    app.run(debug=True)