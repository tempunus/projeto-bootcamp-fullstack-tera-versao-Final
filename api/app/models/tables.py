from enum import unique
from app import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.column(db.String(86),nullable=False,unique=True)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    
    def __init__(self, username, password, name, email):
            self.username = username
            self.password = password
            self.name = name
            self.email = email
            
    def __repr__(self):
        return "<User %r>" % self.username        
    
class Courses(db.Model):
    __tablename__ = 'Course'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    coursename = db.column(db.String(86),nullable=False,unique=True)
    workload = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(86), nullable=False)
    user_id = (db.Integer, db.Foreignkey('users.id'))
    
    user = db.relationship('User', foreign_keys = user_id)
    
    def __init__(self, coursename, workload, category, user_id):
            self.coursename = coursename
            self.workload = workload
            self.category = category
            self.user_id = user_id
             
    def __repr__(self):
        return "<Courses %r>" % self.coursename        