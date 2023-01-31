# Flask version of 'Hello World'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def goodbye_world():
    return "<p>Good Bye, Cruel World!</p>"
