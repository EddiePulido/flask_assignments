from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=["POST"])
def validate():
    is_valid = True
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!")
        is_valid = False

    if not is_valid:
        return redirect('/')
    else:
        db = connectToMySQL('emails')
        query = "INSERT INTO emails(email, created_at, updated_at)  VALUES(%(email)s, NOW(), NOW());"
        data = {
            'email' : request.form['email']
        }
        db.query_db(query,data)
        return redirect('/success')


@app.route('/success')
def success():
    db = connectToMySQL('emails')
    email_list = db.query_db('SELECT * FROM emails')
    last = email_list[len(email_list)-1]['email']

    return render_template("success.html",emails = email_list,last_email = last)

if __name__ == '__main__':
    app.run(debug=True)