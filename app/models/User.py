from app import mongo
import datetime
from secure_config import hashPass, createPaper

class User:
  def sign_in(self):
    pass

  def sign_up(self, data):
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


