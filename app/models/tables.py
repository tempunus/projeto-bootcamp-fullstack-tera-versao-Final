from enum import unique
from re import T
from flask_login import UserMixin
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(1000), unique=True, nullable=False)

    info = db.relationship('User_info', backref='info', lazy=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username


class User_info(db.Model):
    __tablename__ = "user_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    age = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.Text, unique=False, nullable=False)
    state = db.Column(db.Text, nullable=False)
    adress = db.Column(db.Text, unique=False, nullable=False)
    number = db.Column(db.Text, nullable=False)
    profile_status = db.Column(db.Text, unique=False, nullable=False)


    def __init__(self, user_id, age, city, state, adress, number, profile_status):
        self.user_id = user_id
        self.age = age
        self.city = city
        self.state = state
        self.adress = adress
        self.number = number
        self.profile_status = profile_status

        db.create_all()
        db.session.commit()


    #  def __repr__(self):
    #      return "<User_info %r>" % self.id

