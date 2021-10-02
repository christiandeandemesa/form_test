from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    if session['count'] == 1:
        word='time'
    else:
        word='times'
    if 'real_count' not in session:
        session['real_count'] = 1
    else:
        session['real_count'] += 1
    if session['real_count'] == 1:
        word='time'
    else:
        word='times'
    return render_template('counter.html', num=session['count'], word=word, real_num=session['real_count'])

@app.route('/destroy_session')
def delete():
    session.clear()
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    session['count'] += 1
    session['real_count'] -= 1
    return redirect('/')

@app.route('/set', methods=['POST'])
def set():
    session['count'] = int(request.form['number'])
    session['count'] -= 1
    session['real_count'] -= 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)