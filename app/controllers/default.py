import json
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import Response
from flask import render_template
from flask_cors import cross_origin
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_bcrypt import Bcrypt

from .usuarios import Usuario
from ..login_manager import lm

bp_default = Blueprint("default", __name__, template_folder="templates")

bcrypt = Bcrypt()


@bp_default.route("/")
@bp_default.route("/index")
@cross_origin()
def index():
    return render_template("index.html")


@bp_default.route("/login", methods=["POST"])
@cross_origin()
def login():
    try:
        email = request.form.get("email")
        senha = request.form.get("senha")
        u = Usuario.query.filter_by(email=email).first()
        if not u:
            return Response(
                json.dumps({"Erro": f"Usuário não localizado."}),
                status=404,
                mimetype="application/json"
            )

        if not bcrypt.check_password_hash(u.senha_hash, senha):
            return Response(
                json.dumps({"Erro": "A senha está incorreta."}),
                status=401,
                mimetype="application/json"
            )

        login_user(u)
        return jsonify(u.to_json())
    except Exception as err:
        res = Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
        return res


@bp_default.route("/logout", methods=["POST"])
@login_required
@cross_origin()
def logout():
    logout_user()
    return jsonify({"mensagem": "Logout realizado com sucesso."})


@lm.user_loader
@cross_origin()
def load_user(user_id):
    return Usuario.query.get(int(user_id))
