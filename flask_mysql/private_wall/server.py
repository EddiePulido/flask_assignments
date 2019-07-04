from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt        


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

app = Flask(__name__)
app.secret_key = "secret"
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'id' in session:
        return redirect('/wall')

    return render_template("index.html")

@app.route('/wall')
def welcome():
    if 'id' not in session:
        flash("You are not logged in",'not_logged')
        return redirect('/')

    db = connectToMySQL('wall')
    query= "SELECT * from messages JOIN users ON users.id = messages.from_id WHERE to_id = %(id)s"
    data = {
        'id': session['id']
    }
    messages = db.query_db(query,data)
    

    db2 = connectToMySQL('wall')
    
    users = db2.query_db("SELECT * from users")

    return render_template("wall.html",name = session['user_name'], messages = messages,users = users)

@app.route('/register', methods=["POST"])
def register():
    is_valid = True
    if(len(request.form['first_name']) < 2):
        is_valid = False
        flash("First name must contain at least two letters and contain only letters",'fName')
    if(len(request.form['last_name']) < 2):
        is_valid = False
        flash("Last name must contain at least two letters and contain only letters", 'lName')
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!",'email')
    if(len(request.form['password']) < 8 or len(request.form['password']) > 15):
        is_valid = False
        flash("Password must be between 8 and 15",'password')
    if(request.form['password'] != request.form['password_confirm']):
        is_valid = False
        flash("Passwords must match",'pConfirm')
    if not is_valid:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        db = connectToMySQL('wall')
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : pw_hash
        }

        userid = db.query_db(query,data)
        session['id'] = userid
        session['user_name'] = request.form['first_name']
        # flash("You've been successfully registered",'success')

        return redirect("/wall")

@app.route('/login',methods = ['POST'])
def login():

    db = connectToMySQL('wall')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
        'email' : request.form["email"]
    }

    result = db.query_db(query, data)
    if(len(result) > 0):
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['id'] = result[0]['id']
            session['user_name'] = result[0]['first_name']
            return redirect('/wall')

    flash("You could not be logged in",'log_fail')
    return redirect("/")

@app.route('/logout')
def logout():
    session.clear()
        
    return redirect('/')

@app.route('/send', methods= ["POST"])
def send():
    db = connectToMySQL('wall')
    query = "INSERT INTO messages(message,created_at,updated_at,to_id,from_id) VALUES(%(message)s, NOW(),NOW(),%(recipient)s,%(sender)s)"
    data = {
        'message' : request.form["message_text"],
        'sender' : session['id'],
        'recipient' : request.form['id']
    }
    db.query_db(query,data)
    flash("Message sent!","sent_message")
    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete():
    db = connectToMySQL('wall')
    query = "DELETE FROM messages WHERE id = %(id)s"
    data = {
        'id' : request.form['id']
    }

    db.query_db(query,data)

    return redirect('/wall')


if __name__ == '__main__':
    app.run(debug=True)














