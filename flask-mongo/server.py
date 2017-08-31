import os
from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

db = os.getenv('DB', 'db')
port = int(os.getenv('DB_PORT', 27017))

connection = MongoClient(db, port)
words = connection.adhoc.words

app = Flask(__name__)


@app.route('/')
def index():
    result = words.find()
    result_list = [record['word'] for record in result]
    return render_template('home.html', words=result_list)


@app.route('/add_word', methods=['POST'])
def add_word():
    if 'word' in request.form:
        words.insert({'word': request.form['word']})
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
