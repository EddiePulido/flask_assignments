from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def board():
    return render_template("index.html",rows = 8, columns = 8,col1 = "red",col2 = "black")

@app.route("/<x>")
def boardX(x):
    return render_template("index.html",rows=int(x),columns = 8,col1= "red", col2= "black")

@app.route("/<x>/<y>")
def boardXY(x,y):
    return render_template("index.html",rows=int(x),columns=int(y))

@app.route("/<x>/<y>/<color1>/<color2>")
def boardXYColors(x,y,color1, color2):
    return render_template("index.html",rows=int(x),columns=int(y),col1 = color1, col2 = color2)
if(__name__ == "__main__"):
    app.run(debug=True)