from app import app
from User import User
from flask import jsonify, request
from DTO import DTO
import hashlib


@app.route('/name/<name>')
def user(name):
    password = 'turngait'
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    result = m.hexdigest()
    return '<h1>Hello, '+name+'</h1><p>'+str(result)+'</p>'


@app.route('/user/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        dto = DTO()
        data = request.get_json()
        user = User()
        token = user.sign_in(data)

        if token:
            dto.setSuccessCreate()
            dto.setData({'token': token})
            responce = dto.getResponce()
            status = 200
        else: 
            dto.setAccesDenied()
            responce = dto.getResponce()
            status = 403

        return jsonify(responce), status


@app.route('/user/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        dto = DTO()
        data = request.get_json()
        user = User()
        is_signup = user.sign_up(data)
        
        if is_signup:
            dto.setSuccessCreate()
            responce = dto.getResponce()
            status = 204

        else: 
            dto.setServerError()
            responce = dto.getResponce()
            status = 503

        return jsonify(responce), status