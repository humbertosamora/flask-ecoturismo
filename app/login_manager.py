from flask_login import LoginManager
from app.models import Usuario

lm = LoginManager()


@lm.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
