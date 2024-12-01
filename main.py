import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.database import db
from app.dados import prencher_banco_dados
from app.controllers.default import bp_default
from app.controllers.docs import bp_docs
from app.controllers.dicas import bp_dicas
from app.controllers.empresas import bp_empresas
from app.controllers.usuarios import bp_usuarios
from app.login_manager import lm

app = Flask(__name__, template_folder="./app/templates", static_folder="./app/static")

app.config.from_object("config")

CORS(app, supports_credentials=True)

db.init_app(app)

lm.init_app(app)

app.register_blueprint(bp_default, url_prefix="/")
app.register_blueprint(bp_dicas, url_prefix="/dicas")
app.register_blueprint(bp_docs, url_prefix="/docs")
app.register_blueprint(bp_empresas, url_prefix="/empresas")
app.register_blueprint(bp_usuarios, url_prefix="/usuarios")

migrate = Migrate(app, db)


# Inserção de dados no BD para teste.
# Como não há requisição HTTP, então é necessário
# criar um contexto com app_context.
# with app.app_context():
#     prencher_banco_dados()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    print(f"Flask rodando na porta {port}")
    app.run(host="0.0.0.0", port=port)
