import json
from flask import jsonify
from flask import Blueprint
from flask import request
from flask import Response
from flask_cors import cross_origin
from flask_login import current_user
from flask_login import login_required

from ..models import Dica
from ..database import db
from ..tools import substituir_nulo

bp_dicas = Blueprint("dicas", __name__, template_folder="templates")


@bp_dicas.route("/", methods=["GET"])
@cross_origin()
def retrieve_all():
    try:
        dicas = Dica.query.all()
        array_dicas = []
        for d in dicas:
            array_dicas.append(d.to_json())
        
        return jsonify(array_dicas)
    except Exception as err:
        res = Response(
            json.dumps({"Erro": str(err)}),
            status=501,
            mimetype="application/json"
        )
        return res


@bp_dicas.route("/<int:id>", methods=["GET"])
@cross_origin()
def retrieve(id):
    try:
        d = Dica.query.get(id)
        if not d:
            return Response(
                json.dumps({"Erro": f"Dica #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )

        return jsonify(d.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Error": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_dicas.route("/", methods=["POST"])
@login_required
@cross_origin()
def create():
    try:
        id_usuario = current_user.id
        titulo = str(request.form.get("titulo") or "")
        descricao = str(request.form.get("descricao") or "")
        lugar = str(request.form.get("lugar") or "")
        link = str(request.form.get("link") or "")
        flag_praia = bool(request.form.get("flag_praia"))
        flag_montanha = bool(request.form.get("flag_montanha"))
        flag_cachoeira = bool(request.form.get("flag_cachoeira"))
        flag_camping = bool(request.form.get("flag_camping"))
        flag_vestuario = bool(request.form.get("flag_vestuario"))
        flag_alimentacao = bool(request.form.get("flag_alimentacao"))

        if not titulo or not descricao:
            return Response(
                json.dumps({"Erro": "Informe um título e uma descrição para a Dica."}),
                status=400,
                mimetype="application/json"
            )

        d = Dica(id_usuario, titulo, descricao, lugar, link, flag_praia,
                 flag_montanha, flag_cachoeira, flag_camping,
                 flag_vestuario, flag_alimentacao)
        db.session.add(d)
        db.session.commit()
        return jsonify(d.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Error": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_dicas.route("/<int:id>", methods=["PUT"])
@login_required
@cross_origin()
def update(id):
    try:
        d = Dica.query.get(id)
        if not d:
            return Response(
                json.dumps({"Erro": f"Dica #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )

        if current_user.id != d.id_usuario and not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário só pode editar suas dicas."}),
                status=401,
                mimetype="application/json"
            )

        titulo = substituir_nulo(request.form.get("titulo"), d.titulo)
        descricao = substituir_nulo(request.form.get("descricao"), d.descricao)
        lugar = substituir_nulo(request.form.get("lugar"), d.lugar)
        link = substituir_nulo(request.form.get("link"), d.link)
        flag_praia = substituir_nulo(request.form.get("flag_praia"), d.flag_praia)
        flag_montanha = substituir_nulo(request.form.get("flag_montanha"), d.flag_montanha)
        flag_cachoeira = substituir_nulo(request.form.get("flag_cachoeira"), d.flag_cachoeira)
        flag_camping = substituir_nulo(request.form.get("flag_camping"), d.flag_camping)
        flag_vestuario = substituir_nulo(request.form.get("flag_vestuario"), d.flag_vestuario)
        flag_alimentacao = substituir_nulo(request.form.get("flag_alimentacao"), d.flag_alimentacao)

        if not titulo or not descricao:
            return Response(
                json.dumps({"Erro": "Informe um título e uma descrição para a Dica."}),
                status=400,
                mimetype="application/json"
            )

        d.titulo = titulo
        d.descricao = descricao
        d.lugar = lugar
        d.link = link
        d.flag_praia = flag_praia
        d.flag_montanha = flag_montanha
        d.flag_cachoeira = flag_cachoeira
        d.flag_camping = flag_camping
        d.flag_vestuario = flag_vestuario
        d.flag_alimentacao = flag_alimentacao
        db.session.commit()
        return jsonify(d.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Error": str(err)}),
            status=501,
            mimetype="application/json"
        )


@bp_dicas.route("/<int:id>", methods=["DELETE"])
@login_required
@cross_origin()
def delete(id):
    try:
        d = Dica.query.get(id)
        if not d:
            return Response(
                json.dumps({"Erro": f"Dica #{id} não localizada."}),
                status=404,
                mimetype="application/json"
            )

        if current_user.id != d.id_usuario and not current_user.flag_admin:
            return Response(
                json.dumps({"Erro": "Usuário só pode excluir suas dicas."}),
                status=401,
                mimetype="application/json"
            )

        db.session.delete(d)
        db.session.commit()
        return jsonify(d.to_json())
    except Exception as err:
        return Response(
            json.dumps({"Error": str(err)}),
            status=501,
            mimetype="application/json"
        )
