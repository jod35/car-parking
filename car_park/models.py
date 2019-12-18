from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password_hash=db.Column(db.Text)
    service=db.relationship('Service',backref='parking',lazy=True)
    

    def __repr__(self):
        return "{}".format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Service(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    vehicle_name =db.Column(db.String(25),nullable=False)
    num_plate =db.Column(db.String(10),nullable=False)
    owner =db.Column(db.String(25),nullable=False)
    contact =db.Column(db.String(10),nullable=False)
    date_parked =db.Column(db.DateTime,default=datetime.utcnow)
    payment=db.Column(db.Boolean)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return "{}".format(self.id)
    
    

