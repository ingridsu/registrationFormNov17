from flask import Flask, render_template, redirect, session, flash, request
import re

app = Flask(__name__)
app.secret_key = "thatsthescrect"

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_NUM_REGEX = re.compile(r'[0-9]?')
PASSWORD_UPPERALPHA_REGEX = re.compile(r'[A-Z]?')
NAME_REGEX = re.compile(r'\D+')




@app.route('/')
def index():
    session['first_name'] = ""
    session['last_name'] = ""
    session['email'] = ""

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def method_name():
    session['first_name']       = request.form['first_name']
    session['last_name']        = request.form['last_name']
    session['email']            = request.form['email']
    process_error = False
    if(len(request.form['first_name']) < 1):
        flash("Fist Name cannot be left blank!!!!", "error") 
        process_error = True   
    elif not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
        flash("Fist & Last Name cannot have numbers!!!!", "error")
        process_error = True
    elif(len(request.form['last_name']) < 1):
        flash("Last Name cannot be left blank!!!!", "error")
        process_error = True
    elif(len(request.form['email']) < 1):
        flash("Email cannot be left blank!!!!", "error")
        process_error = True
    elif(len(request.form['password']) < 1):
        flash("Password cannot be left blank!!!!", "error")
    elif(len(request.form['password']) < 8):
        flash("Password must be aleast 8 characters!!!!", "error")
        process_error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email address. It should be of the format joe@email.com", "error")
        process_error = True
    elif (request.form['password'] != request.form['confirm_password']):
        flash("Confirm password doesn't match Password ", "error")
        process_error = True
    else:
        flash("Thanks for submitting your information.", "success")  
        session['first_name'] = ""
        session['last_name'] = ""
        session['email'] = ""  

    return render_template('index.html')

app.run(debug=True)