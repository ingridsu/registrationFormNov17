from flask import Flask, render_template, request, flash , redirect , session
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "ThisisSecret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	session['email'] = request.form['email']
	session['fname'] = request.form['fname']
	session['lname'] = request.form['lname']
	session['fpw'] = request.form['fpw']
	session['cpw'] = request.form['cpw']

	errors = False

	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is incorrect---")
		errors = True
		
	if len(request.form['fname']) < 1:
		flash ("Please type your first name---")
		errors = True
	for i in request.form['fname']:
		if i.isdigit():
			errors=True
			flash("Please no numbers in name, Please retype First Name---")
			break

	if len(request.form['lname']) < 1:
		flash ("Please type your last name---")
		errors = True
	for j in request.form['lname']:
		if j.isdigit():
			errors=True
			flash("Please no numbers in name, Please retype Last Name---")
			break			

	if request.form['fpw'] != request.form['cpw']:
		flash ("Passwords do not match, please match passwords---")
		errors = True

	if len(request.form['fpw']) < 8:
		flash ("Password needs to be atleast 8 characters long---")
		errors = True

	if errors:
		return redirect('/')
	else:
		flash ("Thank you for submitting your information")
		return render_template("submit.html")


app.run(debug=True)