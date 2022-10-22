from flask import render_template, flash, redirect, url_for, Response, request, Blueprint
from flask_login import login_user, logout_user
from app import app, db, lm
import json
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login.")
    return render_template('login.html', form=form)

@app.route("/cadastro", methods=["GET", "POST"])
def signup():
    return render_template("cadastro.html")


@app.route("/register", methods=["POST"])
def register():

        username=request.form.get("username")
        password=request.form.get("password")
        name=request.form.get("name")
        email=request.form.get("email")


        new_user = User(username=username, password=generate_password_hash(password, method='sha256'), name=name, email=email)  


        db.session.add(new_user)
        db.session.commit() 

        return render_template('registerSuccess.html')
        # user = User(username=username, password=password, name=name, email=email)
        # db.session.add(user)
        # db.session.commit()

        # return ("ok")  
  
           

    # try:
    #     users = User(
    #         username=body["username"],
    #         nome=body["nome"],
    #         email=body["email"],
    #         password=body["password"],
    #     )

    #     db.session.add(users)
    #     db.session.commit()

    #     return gera_response(201, "usuario", users.to_json(), "Criado com Sucesso")
    # except Exception as e:
    #     print('Erro', e)
    #     return gera_response(500, "usuario", {}, "Erro ao cadastrar")


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


@app.route("/test")
def test():
    i = User("dyda1991220", "123456", "Edjalma Silvaa Almeida", "dyda1991220@gmail.com")
    print(i)
    db.session.add(i)
    db.session.commit()
    return "ok"




