from app import app
from User import User

@app.route('/name/<name>')
def user(name):
    return '<h1>Hello, '+name+'</h1>'
