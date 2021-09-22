from . import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pitch = db.Column(db.String)

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
    postedby = db.Column(db.String(255), db.ForeignKey('users.username'))

    def __repr__(self):
        return f'User {self.mypitch}'

