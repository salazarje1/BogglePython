from flask import Flask, render_template, session, request, jsonify
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

words = boggle_game.words


@app.route('/')
def get_index():
    game = boggle_game.make_board()
    session['game'] = game
    return render_template('index.html', game=game)


@app.route('/guess-word')
def check_word():
    word = request.args['guess']
    game = session['game']
    print(request.args)
    # if word not in words: 
    #     return jsonify({"result":"not-a-word"})

    result = boggle_game.check_valid_word(game, word)
    
    return jsonify({"result": result})


@app.route('/top-score', methods=['POST'])
def get_top_score():
    if session['times-played']: 
        session['times-played'] += 1
    else: 
        session['times-played'] = 1
    
    session['top-score'] = 0
    score = request.json['score']
    if session['top-score'] < score:
        session['top-score'] = score 
    print(request.json['score'])
    return '', 200 