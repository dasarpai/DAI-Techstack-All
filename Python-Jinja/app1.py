# app.py
import flask
app = flask.Flask(__name__)

@app.route("/")
def home () :
    return "This is home page"

@app.route("/hello/")
def hello () :
    return "Hello World! "

if __name__ == "__main__" :
    app.run( debug=True)
