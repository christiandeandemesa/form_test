import random

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='Whatever'

@app.route('/')
def random_number():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    print(session['num'])
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('great_number_game.html', num=session['count'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)