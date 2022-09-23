from flask import flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@localhost/flask_login'
login_manager = LoginManager(app)

db = SQLAlchemy(app)