from flask import Flask, render_template, send_from_directory, request
from replit import db


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/isgoingform', methods = ['GET'])
def isgoingform():
    return render_template('isgoingform.html')

@app.route('/isgoingform', methods = ['POST'])
def isgoingformpost():
    # print(request.form)
    trip = request.form['trip']  
    email = request.form['email']
    name = request.form['name']
    phone = request.form['phone']
    rsvp = 'Yes' if request.form['yes_no'] == 'on' else 'No'

    # store trip response in replit key/value store
    db[(trip, name)] = {
        'name': name,
        'phone': phone,
        'email': email,
        'rsvp': rsvp
    }
    
    
    return request.form

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)
app.run(host='0.0.0.0', port=81)
