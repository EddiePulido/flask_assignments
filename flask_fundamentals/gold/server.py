
import datetime
import random
from flask import Flask, render_template, redirect, session, request,Markup



app = Flask(__name__)
app.secret_key = 'secretkeys'
@app.route('/')
def mainpage():

    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html',gold = session['gold'],activities = session['activities'])



@app.route('/process_money', methods=['post'])
def processmoney():

    if request.form['building'] == "farm":
        earnings = random.randrange(10, 20)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form['building'] == "cave":
        earnings = random.randrange(5, 10)
        session['gold'] += earnings
        session['activities'].append(
            Markup('<p>Earned ' + str(earnings) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})</p>'.format(datetime.datetime.now()))
        )
    elif request.form['building'] == "house":
        earnings = random.randrange(2, 5)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form['building'] == "casino":
        earnings = random.randrange(-50, 50)
        session['gold'] += earnings
        if earnings > 0:
            session['activities'].append(
                'Entered a casino and Won ' + str(earnings) + ' gold! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        else:
            session['activities'].append(
                'Entered a casino and Lost ' + str(earnings) + ' gold. Ouch! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
