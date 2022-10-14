# -------------------- IMPORT --------------------
from enum import unique
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config,from_object('config')

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.column(db.String(86),nullable=False,)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    def to_json(self):
            return {
            'id': self.id,
            'nome': self.name,
            'email': self.email,
            'password': self.password
        }
        
# -------------------- CREAT --------------------
@app.route("/user", methods=["POST"])
def create_users():
    body = request.get_json()

    try:
        users = Users(
            nome=body["nome"],
            email=body["email"],
            password=body["password"]
        )

        db.session.add(users)
        db.session.commit()

        return gera_response(201, "usuario", users.to_json(), "Criado com Sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(500, "usuario", {}, "Erro ao cadastrar")

# -------------------- READ --------------------
@app.route("/users", methods=['GET'])
def select_users():
    users_objects = Users.query.all()
    users_json = [users.to_json() for users in users_objects]

    return gera_response(200, "usuarios", users_json, "OK")


@app.route("/users/<id>", methods=["GET"])
def select_users1(id):
    users_objects = Users.query.filter_by(id=id).first()
    users_json = users_objects.to_json()

    return gera_response(200, "usuario", users_json)

# -------------------- UPDATE --------------------
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    users_objects = Users.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if ('nome' in body):
            users_objects.nome = body["nome"]
        if ('email' in body):
            users_objects.email = body["email"]
        if ('password' in body):
            users_objects.password = body["password"]
       
        db.session.add(users_objects)
        db.session.commit()
        return gera_response(200, "usuario", users_objects.to_json(), "Atualizado com Sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao Atualizar")

# -------------------- DELETE --------------------
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    users_objects = Users.query.filter_by(id=id).first()

    try:
        db.session.delete(users_objects)
        db.session.commit()
        return gera_response(200, "usuario", users_objects.to_json(), "Deletado com Sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao Deletar")

# -------------------- RESPONSE --------------------
def gera_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if (message):
        body["mensagem"] = message
    return Response(json.dumps(body), status=status, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
