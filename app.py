from flask import Flask,request,abort, make_response, redirect, url_for
import click
from flask import session #加密cookie
from flask import render_template, flash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secret string") #获取session密钥

@app.route("/greet", defaults={'name':'programmer'},methods=['GET', 'POST'])
@app.route("/greet/<name>")
def index(name):
    num = request.args.get('num', '999')
    return "<h1>hello world! %s  No.%s</h1>"%(name,num)

@app.route('/watchlist')
def watchlist():
    user = {
        'username' : 'Grey Li',
        'bio' : 'A boy who loves movies'
    }

    movies = [
        {'name' : 'My Neighbor', 'year':'1988'},
        {'name':'这个杀手不太冷', 'year':'2012'},
    ]
    return render_template('watchlist.html', user=user, movies=movies)

@app.route('/')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name')
        response = '<h1>Hello World! %s</h1>'%name
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'
        return response
    

#设置cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name',name)
    return response

#自定义命令
@app.cli.command()
def hello():
    '''输出Hello ''' #用于显示帮助文档
    click.echo("Hello, Human!")

@app.route('/404')
def not_found():
    abort(404)   
    '''abort()函数前不需要使用return语句，但一旦abort()函数被调用，abort()函数之后的代码将不会被执行。
'''

#设置session
@app.route("/login")
def login():
    session['logged_in'] = True #写入session
    session.permanent = True #将session的寿命保存为默认周期,31天
    return redirect(url_for('hello'))


#删除session
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))

@app.route('/flash')
def get_flash():
    flash('I am flash, whos is looking at me')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
