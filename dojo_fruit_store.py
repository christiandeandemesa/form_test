from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key='fruit ninja'

@app.route('/')         
def index():
    return render_template("dojo_fruit_store.html")

@app.route('/confirm', methods=['POST'])         
def confirm():
    print(request.form)
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['blackberry'] = request.form['blackberry']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['count'] = int(request.form['strawberry'])
    session['count'] += int(request.form['raspberry'])
    session['count'] += int(request.form['apple'])
    session['count'] += int(request.form['blackberry'])
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    print(f"Charging {session['first_name']} for {session['count']} fruits")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   