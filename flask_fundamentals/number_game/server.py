from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret'



@app.route('/')
def index():
    if 'num' not in session or session['num'] == None:
        session['num'] = random.randint(1,100)
    if 'lowError' not in session:
        session['lowError'] = "none"
    if 'upError' not in session:
        session['upError'] = "none"
    if 'success' not in session:
        session['success'] = "none"
    
    return render_template('index.html',success = session["success"],lowError=session['lowError'],upError=session['upError'])

@app.route('/guess', methods=['POST'])
def checkNumber():
    
    guess = request.form['guess']
    
        if guess.isdigit():
            numguess = int(guess)
            if numguess == session['num']:
                session["success"] = ""
                return redirect('/')
            elif numguess > session['num']:
                flash('Too high', 'error')
            else:
                flash('Too low', 'error')



    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session['num'] = None
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)