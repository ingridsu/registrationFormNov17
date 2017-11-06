from flask import Flask, render_template, redirect, request, flash
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    digit = True
    now = datetime.now()
    date = datetime.strptime(request.form['date'], "%Y-%m-%d")


    if len(request.form['email']) < 1 or len(request.form['fname']) < 1 or len(request.form['lname']) < 1 or len(request.form['pw']) < 1 or len(request.form['cpw']) < 1 or date == '':
        flash("Can't be blank")

    else:
    
        if digit == True:
            for word in request.form['fname']:
                if word.isdigit():
                    flash("First Name can't contain numbers") 
                    digit = False
                    break

            for word in request.form['lname']:
                if word.isdigit(): 
                    flash("Last Name can't contain numbers")
                    digit = False
                    break

        if len(request.form['pw']) < 2:
            flash("Password should be more than 8 characters")
            digit = False

        if request.form['pw'].islower(): 
            flash("Need at least 1 Uppercase")
            digit = False
        
        if request.form['pw'].isalpha() or request.form['pw'].isdigit():
            flash("Need at least 1 numeric value or 1 alpha character")
            digit = False

        if request.form['cpw'] != request.form['pw']:
            flash("Password doesn't match")
            digit = False

        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            digit = False

        if date > now:
            flash("Date need to be after today!")
            digit = False
                    
        if digit == True:
            flash("Success!!!!!!")

    return render_template('index.html')

app.run(debug=True)