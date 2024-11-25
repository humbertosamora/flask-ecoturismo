
import json
from flask import jsonify
from flask import Blueprint
from flask import request
from flask import Response
from flask_bcrypt import Bcrypt
from flask_cors import cross_origin
from flask_login import current_user
from flask_login import login_required

from ..models import Usuario
from ..database import db
from ..tools import substituir_nulo

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")

bcrypt = Bcrypt()


@bp_usuarios.route("/", methods=["GET"])
@login_required
@cross_origin()
def retrieve_all():
    try:
        if not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário não é administrador."}),
                status=403,
                mimetype="application/json"
            )

        usuarios = Usuario.query.all()
        array_usuarios = []
        for u in usuarios:
            array_usuarios.append(u.to_json())

        return jsonify(array_usuarios)
    except Exception as err:
        res = Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
        return res


@bp_usuarios.route("/<int:id>", methods=["GET"])
@login_required
@cross_origin()
def retrieve(id):
    try:
        u = Usuario.query.get(id)
        if not u:
            return Response(
                json.dumps({"Erro": f"Usuário #{id} não localizado."}),
                status=404,
                mimetype="application/json"
            )

        if current_user.id != u.id and not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário só pode editar seus dados."}),
                status=403,
                mimetype="application/json"
            )

        return jsonify(u.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_usuarios.route("/", methods=["POST"])
@cross_origin()
def create():
    try:
        nome = request.form.get("nome")
        nick = str(request.form.get("nick") or "")
        email = request.form.get("email")
        senha = request.form.get("senha")
        senha_confirmacao = request.form.get("senha_confirmacao")

        if (not nome) or (not email) or (not senha):
            return Response(
                json.dumps({"Erro": "Informe nome, email e senha para cadastrar um suario."}),
                status=400,
                mimetype="application/json"
            )

        if senha != senha_confirmacao:
            return Response(
                json.dumps({"Erro": "As senhas informadas não conferem."}),
                status=400,
                mimetype="application/json"
            )

        senha_hash = bcrypt.generate_password_hash(senha)
        u = Usuario(nome, nick, email, senha_hash)
        db.session.add(u)
        db.session.commit()
        return jsonify(u.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_usuarios.route("/<int:id>", methods=["PUT"])
@login_required
@cross_origin()
def update(id):
    try:
        u = Usuario.query.get(id)
        if not u:
            return Response(
                json.dumps({"Erro": f"Usuário #{id} não localizado."}),
                status=404,
                mimetype="application/json"
            )

        if current_user.id != u.id and not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário só pode editar seus dados."}),
                status=403,
                mimetype="application/json"
            )
        
        if current_user.id != u.id and current_user.flag_admin and u.flag_admin:
            return Response(
                json.dumps({"Erro": "Contate o DBA para gerenciar dados de outros usuários admin."}),
                status=403,
                mimetype="application/json"
            )

        fields = [k for k in request.form]                                      
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
        nome = substituir_nulo(request.form.get("nome"), u.nome)
        nick = substituir_nulo(request.form.get("nick"), u.nick)
        email = substituir_nulo(request.form.get("email"), u.email)
        senha_atual = request.form.get("senha_atual")
        senha_nova = request.form.get("senha_nova")
        senha_confirmacao = request.form.get("senha_confirmacao")

        if (not nome) or (not email):
            return Response(
                json.dumps({"Erro": "Informe nome, email e senha atual para editar um suario."}),
                status=400,
                mimetype="application/json"
            )

        # Só atualiza a senha caso tenha enviado como parâmetro
        if senha_atual or senha_nova or senha_confirmacao:
            if not bcrypt.check_password_hash(u.senha_hash, senha_atual):
                return Response(
                    json.dumps({"Erro": "A senha atual está incorreta."}),
                    status=400,
                    mimetype="application/json"
                )
            elif senha_nova != senha_confirmacao:
                return Response(
                    json.dumps({"Erro": "A nova senha e a confirmação são diferentes."}),
                    status=400,
                    mimetype="application/json"
                )
            else:
                u.senha_hash = bcrypt.generate_password_hash(senha_nova)

        u.nome = nome
        u.nick = nick
        u.email = email
        db.session.commit()
        return jsonify(u.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_usuarios.route("/<int:id>", methods=["DELETE"])
@login_required
@cross_origin()
def delete(id):
    try:
        u = Usuario.query.get(id)
        if not u:
            return Response(
                json.dumps({"Erro": f"Usuário #{id} não localizado."}),
                status=404,
                mimetype="application/json"
            )

        if not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário não possui as permissões necessárias."}),
                status=403,
                mimetype="application/json"
            )
        
        if current_user.flag_admin and u.flag_admin:
            return Response(
                json.dumps({"Erro": "Contate o DBA para gerenciar usuários admin."}),
                status=403,
                mimetype="application/json"
            )

        db.session.delete(u)
        db.session.commit()
        return jsonify(u.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
