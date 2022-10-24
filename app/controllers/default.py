from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user
from app import app, db, lm, bcrypt


from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm


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
        logged_user = form.username.data
        session["logged_user"] = logged_user

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("profile"))
        else:
            flash("Invalid login.")
    return render_template('login.html', form=form)


@app.route("/cadastro", methods=["GET", "POST"])
def signup():
    return render_template("cadastro.html")

@app.route("/register", methods=["POST", "GET"])
def register():
        username=request.form.get("username")
        password=request.form.get("password")
        name=request.form.get("name")
        email=request.form.get("email")

        encrypted_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(username=username, password=encrypted_password, name=name, email=email)  
        print(new_user)


        db.session.add(new_user)
        db.session.commit() 

        
        return render_template("registerSuccess.html")




@app.route("/profile")
def profile():
    if "logged_user" in session:
        logged_user = session["logged_user"]
        return render_template("loggedIndex.html")
    else:
        return redirect(url_for("login"))    

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




