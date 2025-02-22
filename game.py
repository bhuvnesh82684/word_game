from flask import Flask
import service.word_service as word_service
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/game/start/<id>')
def start_game(id):
    print("start game with id" + id)
    word = word_service.word_selection(id)
    return str(len(word))

@app.route('/game/word_check/<id>/<word>')
def word_check(id, word):
    return word_service.word_check(id,word.upper())

if __name__ == '__main__':
    app.run(debug=True)