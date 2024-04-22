# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request

from Handlers.municipality_handler import municipality_handler
from Handlers.user_handler import user_handler
from flask_cors import CORS, cross_origin

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)

app.register_blueprint(user_handler, url_prefix='/averias/users')
app.register_blueprint(municipality_handler, url_prefix='/averias/municipalities')

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run("0.0.0.0",debug=True)
