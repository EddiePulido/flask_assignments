from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say(name):
    return "Hi " + str(name)

@app.route("/repeat/<num>/<var>")
def repeat(num,var):
    return str(var) * int(num)

@app.route("/<anything>/")
def error(anything):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
