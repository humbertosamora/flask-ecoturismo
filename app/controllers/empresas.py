import json
from flask import jsonify
from flask import Blueprint
from flask import request
from flask import Response
from flask_login import current_user
from flask_login import login_required

from ..models import Empresa
from ..database import db
from ..tools import substituir_nulo

bp_empresas = Blueprint("empresas", __name__, template_folder="templates")


@bp_empresas.route("/", methods=["GET"])
def retrieve_all():
    try:
        empresas = Empresa.query.all()
        array_empresas = []
        for e in empresas:
            array_empresas.append(e.to_json())

        return jsonify(array_empresas)
    except Exception as err:
        res = Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
        return res


@bp_empresas.route("/<int:id>", methods=["GET"])
def retrieve(id):
    try:
        e = Empresa.query.get(id)
        if not e:
            return Response(
                json.dumps({"Erro": f"Empresa #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )

        return jsonify(e.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_empresas.route("/", methods=["POST"])
@login_required
def create():
    try:
        if not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário não é administrador."}),
                status=403,
                mimetype="application/json"
            )
        
        nome = str(request.form.get("nome") or "")
        cnpj = str(request.form.get("cnpj") or "")
        email = str(request.form.get("email") or "")
        site = str(request.form.get("site") or "")
        instagram = str(request.form.get("instagram") or "")
        tiktok = str(request.form.get("tiktok") or "")
        youtube = str(request.form.get("youtube") or "")
        facebook = str(request.form.get("facebook") or "")
        if not nome:
            return Response(
                json.dumps({"Erro": "Informe o nome para cadastrar uma empresa."}),
                status=400,
                mimetype="application/json"
            )

        e = Empresa(nome, cnpj, email, site, instagram, tiktok, youtube, facebook)
        file = request.files.get("logo")
        if bool(file) and bool(file.filename):
            e.imagem = file.read()
        db.session.add(e)
        db.session.commit()
        return jsonify(e.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_empresas.route("/<int:id>", methods=["PUT"])
@login_required
def update(id):
    try:
        if not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário não é administrador."}),
                status=403,
                mimetype="application/json"
            )

        e = Empresa.query.get(id)
        if not e:
            return Response(
                json.dumps({"Erro": f"Empresa #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )
        fields = [k for k in request.form]                                      
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
        nome = substituir_nulo(request.form.get("nome"), e.nome)
        cnpj = substituir_nulo(request.form.get("cnpj"), e.cnpj)
        email = substituir_nulo(request.form.get("email"), e.email)
        site = substituir_nulo(request.form.get("site"), e.site)
        instagram = substituir_nulo(request.form.get("instagram"), e.instagram)
        tiktok = substituir_nulo(request.form.get("tiktok"), e.tiktok)
        youtube = substituir_nulo(request.form.get("youtube"), e.youtube)
        facebook = substituir_nulo(request.form.get("facebook"), e.facebook)
        if not nome:
            return Response(
                json.dumps({"Erro": "Informe o nome para editar uma empresa."}),
                status=400,
                mimetype="application/json"
            )

        e.nome = nome
        e.cnpj = cnpj
        e.email = email
        e.site = site
        e.instagram = instagram
        e.tiktok = tiktok
        e.youtube = youtube
        e.facebook = facebook
        file = request.files.get("logo")
        if bool(file) and bool(file.filename):
            e.imagem = file.read()
        
        db.session.commit()
        return jsonify(e.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_empresas.route("/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    try:
        if not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário não é administrador."}),
                status=403,
                mimetype="application/json"
            )

        e = Empresa.query.get(id)
        if not e:
            return Response(
                json.dumps({"Erro": f"Empresa #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )

        db.session.delete(e)
        db.session.commit()
        return jsonify(e.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
