from flask import Flask
app = Flask(__name__)
import click

@app.route("/greet", defaults={'name':'programmer'})
@app.route("/greet/<name>")
def index(name):
    return "<h1>hello world! %s</h1>"%name


@app.cli.command()
def hello():
    '''输出Hello ''' #用于显示帮助文档
    click.echo("Hello, Human!")
    