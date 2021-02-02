from flask import Flask
app = Flask(__name__)
@app.route("/greet", defaults={'name':'programmer'})
@app.route("/greet/<name>")
def index(name):
    return "<h1>hello world! %s</h1>"%name
    