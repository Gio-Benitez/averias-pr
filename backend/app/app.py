# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, jsonify

from Handlers.municipality_handler import municipality_handler
from Handlers.user_handler import user_handler
from Handlers.report_data_Handler import report_data_handler
from Handlers.category_handler import category_handler



from flask_cors import CORS, cross_origin

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app, origins='http://localhost:4000')


app.register_blueprint(user_handler, url_prefix='/averias/users')
app.register_blueprint(municipality_handler, url_prefix='/averias/municipalities')
app.register_blueprint(report_data_handler, url_prefix='/averias/report_data')
app.register_blueprint(category_handler, url_prefix='/averias/categories')
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.


# Example route to get data from the database
@app.route('/', methods=['GET'])
def get_data():
    # Fetch data from the database
    data = ["dad","charma"]  # Fetch data from your local database here
    return jsonify(data)


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run("0.0.0.0",debug=True)
