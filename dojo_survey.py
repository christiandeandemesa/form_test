from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='Shhhhhhhhhh'

@app.route('/')
def form():
    return render_template('dojo_survey.html')

@app.route('/result')
def result():
    return render_template('dojo_survey_result.html')

@app.route('/compile', methods=['POST'])
def compile():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['kierkegaard'] = request.form['kierkegaard']
    session['kant'] = request.form['kant']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/return', methods = ['POST'])
def go_back():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)