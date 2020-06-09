from app import mongo
import datetime
from secure_config import hashPass, createPaper, crateToken

class User:
  def sign_in(self, data):
    email = data['email']
    user = mongo.db.users.find_one({'email': email})
    password = hashPass(data['pass'], user['paper'])
    
    if user['pass_hash'] == password:
      token = crateToken(email)
      user['token'] = token
      is_update = mongo.db.users.replace_one({'email': email}, user)

      if is_update:
        return token
      else:
        return False
    else:
      return False

  def sign_up(self, data):
    user = mongo.db.users.find_one({'email': data['email']})
    if user:
      return False
    
    paper = createPaper(datetime.datetime.utcnow())
    password = hashPass(data['pass'], paper)
    info = {
      'name': data['name'],
      'email': data['email'],
      'status': 1,
      'pass_hash': password,
      'paper': paper,
      'products': [],
      'createdAt': datetime.datetime.utcnow()
    }
    
    id_user = mongo.db.users.insert_one(info).inserted_id

    if id_user:
      return True
    else:
      return False


