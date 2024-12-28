# app.py
import flask
app = flask.Flask(__name__)

@app.route("/")
def home () :
    return flask.render_template("base.html", title="Dr Hari Thapliyaal's Server")

@app.route("/hello/")
def hello () :
    return "Hello World! "

if __name__ == "__main__" :
    app.run( debug=True)
