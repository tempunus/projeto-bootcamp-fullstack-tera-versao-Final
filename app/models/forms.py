from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=20)])
    name = StringField("name", validators =[DataRequired(), Email()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(), Length(min=6, max=16)])
    confirm_password=PasswordField("confirmPassword", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("submit")

