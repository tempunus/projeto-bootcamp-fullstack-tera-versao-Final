from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, current_user
from app import app, db, bcrypt


from app.models.tables import User, User_info
from app.models.forms import LoginForm


# @lm.user_loader
# def load_user(id):
#     return User.query.filter_by(id=id).first()
    

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('logged'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        logged_user = form.username.data
        session["logged_user"] = logged_user

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("logged"))
        else:
            flash("Invalid login.")
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))    


@app.route("/cadastro", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect( url_for('logged'))
    return render_template("cadastro.html")

@app.route("/register", methods=["POST", "GET"])
def register():
        if current_user.is_authenticated:
            return redirect( url_for('logged'))
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




@app.route("/logged")
def logged():
    if "logged_user" in session:
        logged_user = session["logged_user"]
        return render_template("index.html")
    else:
        return redirect(url_for("login"))    



@app.route("/trilhas")
def trails():
    return render_template("trails.html")   

@app.route("/profile")     
def profile():
    return render_template("profilePage.html")

@app.route("/edit_user")
def edit():
    return render_template("user_informations.html")

@app.route("/user_informations", methods=["POST", "GET"])
def user_informations():
    age = request.form.get("age")
    city = request.form.get("city")
    state = request.form.get("state")
    adress = request.form.get("adress")
    number = request.form.get("number")
    profile_status = request.form.get("profile_status")

   
    #new_info = User_info(age=age, city=city, state=state,  profile_status=profile_status)
    new_info = User_info(user_id=current_user.id, age=age, city=city, state=state, adress=adress, number=number, profile_status=profile_status)

    db.session.add(new_info)
    db.session.commit() 


    return redirect(url_for("profile"))    


# @app.route("/test")
# def test():
#     u_id = current_user.id
#     i = User_info( u_id,"22", "São Paulo", "SP", "Rua 1", "2", "OK")
#     print(i)
#     db.session.add(i)
#     db.session.commit()
#     return "ok"




