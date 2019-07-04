from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberries = request.form['strawberry']
    raspberries = request.form['raspberry']
    apples = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count = strawberries + raspberries + apples

    return render_template("checkout.html",straws = strawberries,rasps = raspberries, apps = apples, fName = first_name, lName = last_name,sID = student_id,count = count)

@app.route('/fruits')         
def fruits():
    # images = os.listdir(os.path.join(app.static_folder,"img"))

    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    