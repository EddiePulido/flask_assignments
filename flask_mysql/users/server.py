  from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/users')
def all_users():
    db = connectToMySQL('users')
    user_list = db.query_db('SELECT * FROM users;')
    return render_template("index.html", user_list = user_list)

@app.route('/users/<idx>')
def show_user(idx):
    db = connectToMySQL('users')
    query = 'SELECT * from users WHERE id = %(idx)s;'
    data = {
        'idx' : int(idx)
    }

    user_list = db.query_db(query,data)
    user = user_list[0]
    full_name = user["first_name"] + " " + user["last_name"]
    email = user["email"]
    created = user["created_at"]
    updated = user["updated_at"]


    return render_template("show_user.html",id = idx, full_name = full_name, email = email,created = created, updated = updated)

@app.route('/users/new')
def add_user_page():
     
    return render_template("add_user.html")

@app.route('/users/new/add', methods=['POST'])
def add():
    db = connectToMySQL('users')
    query ='INSERT INTO users(first_name, last_name, email,created_at,updated_at) VALUES(%(fname)s,%(lname)s,%(email)s,NOW(),NOW());'          

    data = {
        'fname' : request.form["first_name"],
        'lname' : request.form["last_name"],
        'email' : request.form["email"]
    }

    id = db.query_db(query,data)

    return redirect("/users/"+str(id))

@app.route('/users/<id>/edit')
def edit_page(id):
    db = connectToMySQL('users')
    query = 'SELECT * from users WHERE id = %(idx)s;'
    data = {
        'idx' : int(id)
    }

    user_list = db.query_db(query,data)
    user = user_list[0]
    first_name = user["first_name"] 
    last_name = user["last_name"]
    email = user["email"]
    created = user["created_at"]
    updated = user["updated_at"]

    return render_template("edit_user.html",id = id, first_name = first_name, last_name = last_name, email = email,created = created, updated = updated)

@app.route('/users/<id>/update', methods=['POST'])
def edit(id):
    db = connectToMySQL('users')
    query = 'UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;'
    data = {
        'fname' : request.form["first_name"],
        'lname' : request.form["last_name"],
        'email' : request.form["email"],
        'id' : id
    }
    db.query_db(query,data)

    return redirect("/users/"+id)

@app.route('/users/<id>/destroy')
def destroy(id):
    db = connectToMySQL('users')
    query = 'DELETE FROM users WHERE id = %(id)s;'
    data ={'id': int(id)}
    db.query_db(query,data)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)