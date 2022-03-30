from flask import Flask
# https://flask.palletsprojects.com/en/2.0.x/

# __name__ is a property with the name of the module
# It helps Flask search for the templates and static files
# Create an instance of the Flask class
app = Flask(__name__)


# This is the root of the application
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


# This is a second page
@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# The application will run on the local host: http://127.0.0.1:5000/
if __name__ == '__main__':
    app.run(debug=True)
