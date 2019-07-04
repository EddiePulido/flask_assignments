from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    rating = request.form['rating']
    tech = request.form.getlist('tech')






    return render_template("results.html", tName=name, tLocation=location,tLanguage=language,tComment = comment,tRating = rating,tTech = tech)


if(__name__ == "__main__"):
    app.run(debug=True)