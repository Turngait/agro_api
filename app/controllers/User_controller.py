from app import mongo

class User_controller:
  def showMain(self):
      online_users = mongo.db.users.find()
      return '<h1>Hello, user</h1><br><p>Your browser is ' + str(online_users[0]) + '</p>'

