import paths
from app import app, mongo
from User_controller import User_controller
from flask import jsonify


@app.route('/')
def index():
    controller = User_controller()
    answer = controller.showMain()
    return answer


@app.route('/name/<name>')
def user(name):
    return '<h1>Hello, '+name+'</h1>'

@app.route('/test')
def test():
    obj_test = {
        'name': 'Kate',
        'age': 30
    }

    return jsonify(obj_test)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
