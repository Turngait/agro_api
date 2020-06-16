import paths
from app import app, mongo
import routes_user
from flask import jsonify, request
import os


@app.route('/')
def index():
    online_users = mongo.db.users.find()
    return '<h1>Hello, user</h1><br><p>Your browser is ' + str(online_users[0]) + '</p>'

@app.route('/test')
def test():
    obj_test = {
        'name': 'Kate',
        'age': 30
    }

    return jsonify(obj_test)

@app.route('/testFile', methods=['POST'])
def testFile():
    req = request.files['avatar']
    file_name = req.filename
    app_root = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(app_root, 'img/')
    destination = '/'.join([target, file_name])
    req.save(destination)

    return jsonify({'test': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
