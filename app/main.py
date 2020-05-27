import paths
from app import app, mongo
import routes_user
from flask import jsonify


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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
