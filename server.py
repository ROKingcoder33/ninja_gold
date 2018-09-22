from flask import Flask, render_template, request, redirect, session
import os
import random
import datetime
app = Flask(__name__)
app.secret_key = os.urandom(24)

now = datetime.datetime.now().strftime("%I:%M%p %b-%d-%Y")


@app.route('/')
def index():
    try:
        session['goldTotal']
    except KeyError:
        session['goldTotal'] = 0
        session['activity'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        getGold = random.randrange(10, 20)
    elif building == 'cave':
        getGold = random.randrange(5, 10)
    elif building == 'house':
        getGold = random.randrange(2, 5)
    elif building == 'casino':
        getGold = random.randrange(-50, 50)
    history = "You earned/lost " + str(getGold) + " in gold (" + \
              str(now) + ")"
    session['goldTotal'] = int(session['goldTotal']) + getGold
    if len(session['activity']) >= 9:
        session['activity'].append(history)
        session['activity'].pop(0)
    else:
        session['activity'].append(history)
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
