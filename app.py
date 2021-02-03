from flask import Flask,request,abort, make_response
app = Flask(__name__)
import click

@app.route("/greet", defaults={'name':'programmer'},methods=['GET', 'POST'])
@app.route("/greet/<name>")
def index(name):
    num = request.args.get('num', '999gi')
    return "<h1>hello world! %s  No.%s</h1>"%(name,num)

@app.route('/set/<name>')
def set_cookie():
    response = make_response(redirect(url_for(index)))
    response.set_cookie('name', name)
    return response

@app.cli.command()
def hello():
    '''输出Hello ''' #用于显示帮助文档
    click.echo("Hello, Human!")

@app.route('/404')
def not_found():
    abort(404)   
    '''abort()函数前不需要使用return语句，但一旦abort()函数被调用，abort()函数之后的代码将不会被执行。
'''