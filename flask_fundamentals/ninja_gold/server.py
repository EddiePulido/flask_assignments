from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)

def farmRand():
    

@app.route("/")
def ninja_gold():
    
    return render_template("index.html")

@app.route("/process_money",methods=["POST"])
def process_money():
    redirect("/")




if __name__ == '__main__':
    app.run(debug=True)

