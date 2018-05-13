from flask import Flask, request, render_template
import random

app = Flask(__name__)

users = {"millan04": "andrew", "millaand000": "millan", "petemi09": "1234"}

@app.route('/')
def login():
	user_name = request.args.get("user")
	password = request.args.get("password")
	not_robot = request.args.get("robot")
	if (user_name in users) and (users[user_name] == password):# and isinstance(not_robot, str):
		return render_template('display.html')
	else:
		return render_template('login.html', message = users)

@app.route('/processform')
def procform():

	return render_template('display.html')

@app.route('/newuser')
def new_user():
	user_name = request.args.get("user")
	password = request.args.get("password")
	if user_name in users:
		return render_template('newuser.html', message = "Username already in use")
		
	else:
		users[user_name] = password
		return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)
