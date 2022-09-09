# Note to self, bring to school band binder with music

from flask import Flask, render_template, send_from_directory, request
from replit import db
import hashlib

def makeHash(string):
    hashed_string = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return hashed_string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/isgoingform', methods = ['GET'])
def isgoingform():
    return render_template('isgoingform.html')

@app.route('/login', methods = ['GET', 'POST'])
def loginform():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return "yay you logged in"

@app.route('/trip_rsvp', methods = ['GET'])
def trip_rsvp():
    going = db['irv_woods_0922']['going']
    not_going = db['irv_woods_0922']['not_going']

    return render_template('trip_rsvp.html', going=going, not_going=not_going)


@app.route('/isgoingform', methods = ['POST'])
def isgoingformpost():
    # print(request.form)
    trip = request.form['trip']  
    email = request.form['email']
    name = request.form['name']
    phone = request.form['phone']
    rsvp = 'Yes' if request.form['yes_no'] == '1' else 'No'

    # store trip response in replit key/value store
    scout = {
        'name': name,
        'phone': phone,
        'email': email
    }

    if trip in db:
        if rsvp == 'Yes':
            db[trip]['going'].append(scout)
        else:
            db[trip]['not_going'].append(scout)
    else:
        if rsvp == 'Yes':
            db[trip] = {
                'going': [scout],
                'not_going': []
            }
        else:
            db[trip] = {
                'going': [],
                'not_going': [scout]
            }
            
    print(db['irv_woods_0922'])

    
    return request.form

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)
app.run(host='0.0.0.0', port=81)
