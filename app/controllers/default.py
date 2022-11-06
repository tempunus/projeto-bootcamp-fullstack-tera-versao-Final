from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, current_user
from app import app, db, bcrypt


from app.models.tables import User, User_info
from app.models.forms import LoginForm, RegisterForm


@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

####### LOGIN ########

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('logged'))
    form = LoginForm()
    print (form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        logged_user = form.username.data
        session["logged_user"] = logged_user

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("logged"))
        else:
            flash(f'Erro ao logar no usuário {form.username.data}', category='danger')
    return render_template('login.html', form=form)

###### Sessão #######
@app.route("/logged")
def logged():
    if "logged_user" in session:
        logged_user = session["logged_user"]
        return render_template("index.html")
    else:
        return redirect(url_for("login"))   


####### logout #######
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))    

####### Cadastrar #######
# @app.route("/cadastro", methods=["GET", "POST"])
# def signup():
#     if current_user.is_authenticated:
#         return redirect( url_for('logged'))
#     return render_template("cadastro.html")

# @app.route("/register", methods=["POST", "GET"])
# def register():
#         if current_user.is_authenticated:
#             return redirect( url_for('logged'))
#         username=request.form.get("username")
#         password=request.form.get("password")
#         name=request.form.get("name")
#         email=request.form.get("email")

#         encrypted_password = bcrypt.generate_password_hash(password).decode("utf-8")

#         new_user = User(username=username, password=encrypted_password, name=name, email=email)  


#         db.session.add(new_user)
#         db.session.commit() 

#         return render_template("registerSuccess.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm() 
    if current_user.is_authenticated:
         return redirect( url_for('logged'))
    if form.validate_on_submit(): 

        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        new_user = User(username=form.username.data, password=encrypted_password, name=form.name.data, email=form.email.data)  

        db.session.add(new_user)
        db.session.commit() 

        flash(f'Conta criada com socesso para o usuário {form.username.data}', category='success')

        return redirect(url_for('login'))
    return render_template('cadastro.html', form=form)

###### editar informações ####

@app.route("/edit_user", methods=["POST", "GET"])
def edit_user():
    if not current_user.is_authenticated:
         return redirect( url_for('login'))

    user_id = current_user.id
    user_informations = User_info.query.filter_by(user_id=user_id).first()
    if request.method == 'POST':
        if user_informations:
            db.session.delete(user_informations)
            user_informations = User_info(
                user_id = user_id,
                age = request.form.get("age"),
                city = request.form.get("city"),
                state = request.form.get("state"),
                adress = request.form.get("adress"),
                number = request.form.get("number"),
                profile_status = request.form.get("profile_status")
            )
            db.session.add(user_informations)
            db.session.commit()
            

        else:
            

            user_informations = User_info(
                user_id = user_id,
                age = request.form.get("age"),
                city = request.form.get("city"),
                state = request.form.get("state"),
                adress = request.form.get("adress"),
                number = request.form.get("number"),
                profile_status = request.form.get("profile_status")
            )

            db.session.add(user_informations)
            db.session.commit()
        
        return redirect( url_for('profile'))    
       
    return render_template("user_informations.html")    
         


@app.route("/trilhas")
def trails():    
    if not current_user.is_authenticated:
         return redirect( url_for('login'))
    return render_template("trails.html")   

@app.route("/course_template")
def course_template():
    if not current_user.is_authenticated:
         return redirect( url_for('login'))
    return render_template("courses/courseTemplate.html")    

@app.route("/profile")     
def profile():
    if not current_user.is_authenticated:
         return redirect( url_for('login'))
    id = current_user.id
    infos = User_info.query.filter_by(user_id=id)
    return render_template("profilePage.html", infos=infos)

