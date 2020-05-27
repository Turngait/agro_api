from app import app
from User import User
from flask import jsonify, request


@app.route('/name/<name>')
def user(name):
    return '<h1>Hello, '+name+'</h1>'


@app.route('/user/signin', methods=['POST'])
def signin():
    return jsonify({'test': True})


@app.route('/user/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        user = User()
        is_signup = user.sign_up(data)
        
        if is_signup:
            responce = {'status': True}
        else: 
            responce = {'status': False}

        return jsonify(responce)