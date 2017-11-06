from flask import Flask, render_template, request, redirect, flash, session
import re, datetime
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'asdf'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.before_first_request
def initialize():
    session['error']=False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getResult():
    now = datetime.now()
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1:
        flash("There are empty fields!", 'length error')
        session['error'] = True
    if not request.form['first_name'].isalpha():
        flash("First name cannot have numbers!", 'invalid input')
        session['error'] = True
    if not request.form['last_name'].isalpha():
        flash("Last name cannot have numbers!", 'invalid input')
        session['error'] = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email!", 'invalid input')
        session['error'] = True
    if len(request.form['password']) < 8:
        flash("Password is too short!", 'length error')
        session['error'] = True
    if request.form['password'] != request.form['confirm_password']:
        flash("Password do not match!", 'invalid password')
        session['error'] = True
    if re.search('[A-Z]', request.form['password']) is None:
        flash("Password must contain at least one uppercase letter")
    if re.search('[0-9]', request.form['password']) is None:
        flash("Password must contain at least one number")
    try:
        datetime.strptime(request.form['dob'], "%Y-%m-%d")
    except ValueError:
        flash("Invalid date format: Year, month, day")
    try:
        now < datetime.strptime(request.form['dob'], '%Y-%m-%d')
    except ValueError:    
        flash("You cannot be born in the future")
    if session['error'] is False:
        flash("Thanks for submitting your information!", "success")
    return render_template('index.html')

app.run(debug=True)
