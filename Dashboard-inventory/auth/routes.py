from flask import Flask, books_list, request, jsonify

app = Flask(__name__)


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_auth = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        new_num = request.form['number']
        new_len = request.form['length']
        new_type = request.form['book']
        iD = books_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'author': new_auth,
            'language': new_lang,
            'title': new_title,
            'ISBN': new_num,
            'length': new_len,
            'book': new_type
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/book/<int:id>', methods=['GET','PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book[id] == id:
                return jsonify(book)
            pass
        if request.method == 'PUT':
            for book in books_list:
                if book['id'] == id:
                    book['author'] = request.form['author']
                    book['language'] = request.form['language']
                    book['title'] = request.form['title']
                    update_book = {
                        'id': id,
                        'author': book['author'],
                        'language': book['language'],
                        'title': book['title']
                    }   
                    return jsonify(update_book)   
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)
            