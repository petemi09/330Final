from flask import Flask, request, render_template, jsonify
import googlemaps
app = Flask(__name__)

users = {"millan04": "andrew", "millaand000": "millan"}

@app.route('/')
def login():
	user_name = request.args.get("user")
	password = request.args.get("password")
	not_robot = request.args.get("robot")
	if (user_name in users) and (users[user_name] == password): # and isinstance(not_robot, str):
		return render_template('display.html')
	else:
		return render_template('login.html', message = "Incorrecct Username or Password")

@app.route('/processform')
def procform():
	key = 'AIzaSyCANwUbNqn7nOnqcwUG2p2PX5O0cg7sINE'
	city = request.args.get("city")
	state = request.args.get("state")

	full_name = city + ', ' + state

	gm = googlemaps.Client(key = key)
	geocode_result = gm.geocode(full_name)[0]
	detail = []
	detail.append("Formal address: " + geocode_result['formatted_address'])
	detail.append("Region: "+ geocode_result['address_components'][1]['long_name'])
	detail.append("Latitude: "+ str(geocode_result['geometry']['location']['lat']))
	detail.append("Longitude: "+ str(geocode_result['geometry']['location']['lng']))

	return render_template('display.html', location = detail)

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
