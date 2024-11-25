import base64
from sqlalchemy import String
from sqlalchemy import LargeBinary
from sqlalchemy import BOOLEAN
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .database import db


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    nick: Mapped[str] = mapped_column(String(20), nullable=True,
                                      unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False,
                                       unique=True)
    senha_hash: Mapped[str] = mapped_column(String(100), nullable=False)
    flag_admin: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                server_default="0",
                                                insert_default=False)
    dicas = relationship("Dica", back_populates="usuario",
                         cascade="all, delete-orphan")

    def __init__(self, nome, nick, email, senha_hash):
        self.nome = nome
        self.nick = nick
        self.email = email
        self.senha_hash = senha_hash

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nick": self.nick,
            "email": self.email
        }

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Dica(db.Model):
    __tablename__ = "dicas"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"), nullable=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(1000), nullable=False)
    lugar: Mapped[str] = mapped_column(String(100), nullable=True)
    link: Mapped[str] = mapped_column(String(300), nullable=True)
    flag_praia: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                server_default="0",
                                                insert_default=False)
    flag_montanha: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                   server_default="0",
                                                   insert_default=False)
    flag_cachoeira: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                    server_default="0",
                                                    insert_default=False)
    flag_camping: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                  server_default="0",
                                                  insert_default=False)
    flag_vestuario: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                    server_default="0",
                                                    insert_default=False)
    flag_alimentacao: Mapped[BOOLEAN] = mapped_column(BOOLEAN(), nullable=False,
                                                      server_default="0",
                                                      insert_default=False)
    usuario = relationship("Usuario", back_populates="dicas")

    def __init__(self, id_usuario, titulo, descricao, lugar, link,
                 flag_praia=False, flag_montanha=False, flag_cachoeira=False,
                 flag_camping=False, flag_vestuario=False, flag_alimentacao=False):
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.descricao = descricao
        self.lugar = lugar
        self.link = link
        self.flag_praia = flag_praia
        self.flag_montanha = flag_montanha
        self.flag_cachoeira = flag_cachoeira
        self.flag_camping = flag_camping
        self.flag_vestuario = flag_vestuario
        self.flag_alimentacao = flag_alimentacao

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "lugar": self.lugar,
            "link": self.link,
            "flag_praia": self.flag_praia,
            "flag_montanha": self.flag_montanha,
            "flag_cachoeira": self.flag_cachoeira,
            "flag_camping": self.flag_camping,
            "flag_vestuario": self.flag_vestuario,
            "flag_alimentacao": self.flag_alimentacao
        }


class Empresa(db.Model):
    __tablename__ = "empresas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(18), nullable=True, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    site: Mapped[str] = mapped_column(String(200), nullable=True)
    instagram: Mapped[str] = mapped_column(String(200), nullable=True)
    tiktok: Mapped[str] = mapped_column(String(200), nullable=True)
    youtube: Mapped[str] = mapped_column(String(200), nullable=True)
    facebook: Mapped[str] = mapped_column(String(200), nullable=True)
    imagem: Mapped[LargeBinary] = mapped_column(LargeBinary(length=(2**32)-1),
                                                nullable=True)

    def __init__(self, nome, cnpj, email, site, instagram, tiktok,
                 youtube, facebook, imagem=None):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.site = site
        self.instagram = instagram
        self.tiktok = tiktok
        self.youtube = youtube
        self.facebook = facebook
        self.imagem = imagem

    def to_json(self):
        img = "" if bool(self.imagem) == False else base64.b64encode(self.imagem).decode("ascii")
        return {"id": self.id, "nome": self.nome, "cnpj": self.cnpj,
                "email": self.email, "site": self.site,
                "instagram": self.instagram, "tiktok": self.tiktok,
                "youtube": self.youtube, "facebook": self.facebook,
                "imagem": img}
