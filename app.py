from flask import Flask,request,abort
app = Flask(__name__)
import click

@app.route("/greet", defaults={'name':'programmer'},methods=['GET', 'POST'])
@app.route("/greet/<name>")
def index(name):
    num = request.args.get('num', '999gi')
    return "<h1>hello world! %s  No.%s</h1>"%(name,num)


@app.cli.command()
def hello():
    '''输出Hello ''' #用于显示帮助文档
    click.echo("Hello, Human!")

@app.route('/404')
def not_found():
    abort(404)