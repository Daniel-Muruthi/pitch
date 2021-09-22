from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

#callback function to retrieve a user when a unique identifier is passed 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    passcode = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.passcode = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passcode, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'

class NewPitch(db.Model):
    __tablename__ = "minutepitches"

    id = db.Column(db.Integer, primary_key = True)
    mypitch = db.Column(db.String)
    author = db.Column(db.String(255))
    postedby = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.mypitch}'

