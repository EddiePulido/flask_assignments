from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

app.count = 0

@app.route("/")
def counter():
    # global count
    # count += 1
    session["count"] += 1
    return render_template("index.html",counter = session["count"])

@app.route("/destroy_session")
def destroy():    
    session["count"] = 0
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():    
    session["count"] = 0
    return redirect("/")

@app.route("/add",methods = ["POST"])
def add():
    session["count"] += 1
    return redirect("/")

@app.route("/choice_add",methods=["POST"])
def add_choice():
    num = request.form("num")
    session["count"] += int(num) - 1
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)