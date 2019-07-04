from flask import Flask, render_template,request,redirect, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def form():
    return render_template("index.html")

@app.route('/result')
def results():
    db = connectToMySQL('survey')
    last = db.query_db('SELECT * FROM users ORDER BY ID DESC LIMIT 1;')
    print(last)
    user = last[0]
    name = user['full_name']
    location = user['dojo_location']
    language = user['language']
    comment = user['comment']


    return render_template("results.html",name = name, location = location, language = language, comment = comment)


@app.route('/update', methods=['POST'])
def create_user():    
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Please enter a name")
    if len(request.form['location']) < 1:
        is_valid = False
        flash("Please enter a location")
    if len(request.form['language']) < 1:
        is_valid = False
        flash("Please select a language")
    if len(request.form['comment']) > 120:
        is_valid = False
        flash("Please keep your comment to 120 characters or less")

    if not is_valid:
        return redirect('/')
    else:
        db = connectToMySQL('survey')
        query = "INSERT INTO users(full_name,dojo_location,language,comment,created_at,updated_at) VALUES(%(name)s,%(dojo)s,%(language)s,%(comment)s,NOW(),NOW());"
        data = {
            'name' : request.form['name'],
            'dojo' : request.form['location'],
            'language' : request.form['language'],
            'comment' : request.form['comment']
        }

        db.query_db(query,data)
        return redirect("/result")


if(__name__ == "__main__"):
    app.run(debug=True)