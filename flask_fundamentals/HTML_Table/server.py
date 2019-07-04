from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def list():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    lst = []

    for i in users:
        name = ""
        for j in i:
            name += i[j] + " "
        lst.append(name)

    return render_template("index.html",length = len(users),user_list = users,full_names = lst)

    









if(__name__ == "__main__"):
    app.run(debug=True)