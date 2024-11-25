from flask import Blueprint
from flask import render_template
from flask_cors import cross_origin

bp_docs = Blueprint("doc", __name__, template_folder="templates")


@bp_docs.route("/dicas")
@cross_origin()
def doc_dicas():
    return render_template("dicas.html")

@bp_docs.route("/usuarios")
@cross_origin()
def doc_usuarios():
    return render_template("usuarios.html")


@bp_docs.route("/empresas")
@cross_origin()
def doc_empresas():
    return render_template("empresas.html")


@bp_docs.route("/login")
@cross_origin()
def doc_login():
    return render_template("login.html")


@bp_docs.route("/logou")
@cross_origin()
def doc_logout():
    return render_template("logout.html")


@bp_docs.route("/sobre")
@cross_origin()
def doc_sobre():
    return render_template("sobre.html")
