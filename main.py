# Note to self, bring to school band binder with music
# Session code taken from BYGTech
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from flask import Flask, render_template, send_from_directory, request, redirect, session, url_for, flash
# from flask_session import Session
from functools import wraps
import hashlib
from datetime import datetime, timedelta, date
import os
from replit import db
def makeHash(string):
    hashed_string = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return hashed_string




app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

def apology(message, file):
    """Renders message as an apology to user."""
    return render_template(file, message=message)

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    print('testt')
    if session.get("is_loggedin") != 1:
      return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function

def admin_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("is_admin") == 0:
      return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
  session.clear()
  return redirect('/')
@app.route('/isgoingform', methods = ['GET'])
def isgoingform():
    return render_template('isgoingform.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    if session.get("is_loggedin") is not None:
      return redirect('/')

    # if user reached route via POST (as by submitting a form via POST) 
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("Please enter an username.", "login.html")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please enter a password.", "login.html")

        else:
            username = request.form.get("username")
            password = request.form.get("password")
            passwordHashed = makeHash(password)
        # remember which user has logged in
        session["username"] = username
        session["is_admin"] = 1
        session["is_loggedin"] = 1

        # redirect user to home page
        return redirect('/')

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/trip_rsvp', methods = ['GET'])
@login_required
@admin_required
def trip_rsvp():
    trips = ['irv_woods_0922', 'irv_woods_0923']
    readableTripNames = {'irv_woods_0922':'Irvington Woods Trip 2022-23', 'irv_woods_0923':'Irvington Woods Trip 2023-24'}
    allRsvp = []
    for trip in trips:
      try:
        going = db[trip]['going']
        
        not_going = db[trip]['not_going']
      except:
        going = []
        not_going = []
      allRsvp.append({'going': going, 'not_going': not_going, 'name':readableTripNames[trip] })
    print(allRsvp)
    return render_template('trip_rsvp.html', allRsvp=allRsvp)

@app.route('/test')
def test():
  print(session)
  print(session.get("is_admin"))
  return 'hi'

@app.route('/isgoingform', methods = ['POST'])
def isgoingformpost():
    # print(request.form)
    trip = "irv_woods_0923"
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
            

    
    return request.form

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)
app.run(host='0.0.0.0', port=10000)
