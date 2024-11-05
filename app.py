from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'morning','hello','evening','night','day','smooth','torch','good','bad','beautiful','ugly','messy','clean','house','home','garden','building','java','nice','adjust','congrates','then']

@app.route('/')
def index():
    global current_word, guesses, turns
    current_word = random.choice(words)
    guesses = ''
    turns = 5
    return render_template('index.html', failed='_ ' * len(current_word), turns=turns)

@app.route('/guess', methods=['POST'])
def guess():
    global guesses, turns, current_word
    guess = request.form.get('guess').lower()
    guesses += guess

    if guess not in current_word:
        turns -= 1

    failed = [char if char in guesses else '_' for char in current_word]

    if turns <= 0:
        return redirect(url_for('game_over'))

    if '_' not in failed:
        return redirect(url_for('win'))

    return render_template('index.html', failed=' '.join(failed), turns=turns)

@app.route('/game_over')
def game_over():
    global current_word
    return render_template('gameOver.html', word=current_word)

@app.route('/win')
def win():
    global current_word
    return render_template('win.html', word=current_word)

if __name__ == '__main__':
    app.run(debug=True)
