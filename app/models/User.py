from app import mongo
import datetime

class User:
  def sign_in(self):
    pass

  def sign_up(self, data):
    info = {
      'name': data['name'],
      'email': data['email'],
      'status': 1,
      'pass_hash': data['pass'],
      'products': [],
      'createdAt': datetime.datetime.utcnow()
    }
    
    id_user = mongo.db.users.insert_one(info).inserted_id

    if id_user:
      return True
    else:
      return False


