from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/play")

def boxes():
    
    return render_template("index.html",times=3,value = "")


@app.route("/play/<x>")

def boxes_x(x):
    return render_template("index.html",times=int(x),value = "")



@app.route("/play/<x>/<color>")

def boxes_and_color(x,color):    
    return render_template("index.html",times=int(x),value = color)



if __name__=="__main__": 
    app.run(debug=True)
