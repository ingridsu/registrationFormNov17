from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.\w{2,4}$')
NAME_REGEX = re.compile(r'^[A-z-A-Z]+$')
PW_REGEX = re.compile(r'^\d.*[A-Z]|[A-Z].*\d$')
app = Flask(__name__)
app.secret_key = "keepitsecretkeepitsafe"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validation', methods=['POST'])
def ninjas():
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthday = request.form['birthday']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        
        if len(birthday) > 0:
            currentdate = int(str(datetime.datetime.now().strftime("%Y")))
            year = int(birthday[:4])
        
        check = True

        #check for required fields
        for key in request.form:
            if len(request.form[key]) < 1:
                flash("**{} field is required.".format(key.title()), "missing")
                check = False
        
        #check for valid email format
        if not EMAIL_REGEX.match(email) and len(email) > 0:
            flash("**email field is invalid.", "error")
            check = False
        
        if not NAME_REGEX.match(firstname) and len(firstname) > 0:
            flash("**First Name field is invalid.", "error")
            check = False
        
        if not NAME_REGEX.match(lastname) and len(lastname) > 0:
            flash("**Last Name field is invalid.", "error")
            check = False

        if password != confirmpassword and len(password) > 0:
            flash("**Passwords do not match", "error")
            check = False

        if len(birthday) > 0:
            if year < currentdate - 120 or year > currentdate - 1:
                flash("**Invalid birth year entered", "error")
                check = False

        if not PW_REGEX.match(password):
            flash("**Password must contain at least one uppercase letter and one number", "error")
            check = False
            
        if check == True:
            flash("Thanks for submitting your form!", "success")

        return redirect('/')
    
            

app.run(debug=True)