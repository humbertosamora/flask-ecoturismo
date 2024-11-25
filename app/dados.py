from time import sleep
from flask_bcrypt import Bcrypt
from sqlalchemy import inspect

from .models import Usuario
from .models import Empresa
from .models import Dica
from .database import db

bcrypt = Bcrypt()

usuarios = [
    Usuario(
        nome="Admin",
        nick="Admin",
        email="admin@puc.com.br",
        senha_hash=bcrypt.generate_password_hash("imjE$c_+aqM"),
    ),
    Usuario(
        nome="Goku",
        nick="kakarotto",
        email="goku@crunchyroll.com",
        senha_hash=bcrypt.generate_password_hash("omaisforte"),
    ),
    Usuario(
        nome="Hulk Paraíba",
        nick="Hulk",
        email="hulk@atletico.com",
        senha_hash=bcrypt.generate_password_hash("G@lo+2024"),
    ),
    Usuario(
        nome="Ronaldo R49",
        nick="Bruxo",
        email="r49@atletico.com",
        senha_hash=bcrypt.generate_password_hash("R49+4Ever"),
    ),
    Usuario(
        nome="Naruto",
        nick="narutinho",
        email="uzumaki@crunchyroll.com",
        senha_hash=bcrypt.generate_password_hash("Kurama4ever"),
    ),
    Usuario(
        nome="Tio Patinhas",
        nick="pao@duro",
        email="patinhas@disney.com",
        senha_hash=bcrypt.generate_password_hash("doraCintilante"),
    ),
]
# Usuário Admin
usuarios[0].flag_admin = True

# EMPRESAS
empresas = [
    Empresa(
        nome="EcoPix - Trekking & Hiking",
        cnpj="32.779.240/0001-22",
        email="contato@ecopixtrekking.com.br",
        site="https://www.ecopixtrekking.com.br/",
        instagram="https://www.instagram.com/ecopix_trekking/",
        tiktok="",
        youtube="",
        facebook="https://www.facebook.com/ecopixtrekking/",
    ),
    Empresa(
        nome="Índio Ecotour",
        cnpj="29.381.572/0001-40",
        email="contato@indioecotour.com.br",
        site="https://www.indioecotour.com.br/",
        instagram="https://www.instagram.com/indioecotour/",
        tiktok="https://www.tiktok.com/@indioecotour/",
        youtube="https://www.youtube.com/c/IndioEcotourViagens/",
        facebook="https://www.facebook.com/indioecotour/",
    ),
    Empresa(
        nome="Vara Mato",
        cnpj="24.371.851/0001-09",
        email="atendimento@varamato.com.br",
        site="https://varamato.com.br/",
        instagram="https://www.instagram.com/varamato/",
        tiktok="",
        youtube="https://www.youtube.com/@VaraMato/",
        facebook="https://www.facebook.com/VaraMato/",
    ),
]

# DICAS
dicas = [
    Dica(
        id_usuario=2,
        titulo="É cansando o corpo que a gente descança a mente!",
        descricao="Esse jargão da Índio Ecotour traduz como podemos melhorar nossa saúde mental praticando ecoturismo. A imersão na natureza possibilita experiências únicas, sensação de bem estar e possibilita fazer amigos pelas trilas.",
        lugar="",
        link="https://www.instagram.com/indioecotour/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=3,
        titulo="Respeite os seus limites",
        descricao="Iniciar uma nova aventura é desafiador, mas pesquise a extensão (km) e o nível de dificuldade técnica da trilha antes de escolher seu destino. Pessoas com baixo condicionamento físico podem ter dificuldade no começo. Inicie aos poucos porque o importante é o seu bem estar.",
        lugar="",
        link="https://www.colibriaventura.com.br/2020/09/22/7-duvidas-de-quem-quer-praticar-o-trekking-mas-tem-receio-de-perguntar/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=4,
        titulo="Procure uma agência experiente",
        descricao="Agências experientes irão proporcionar boas experiências e segurança nas trilhas. Verifique se a agência possui CADASTUR e confira as avaliações nas redes sociais. Dê preferência para as agências que contratam guias locais - moradores da região conhecem melhor o bioma, as trilhas e a condição atual do lugar.",
        lugar="",
        link="https://www.ecopixtrekking.com.br/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=5,
        titulo="Nunca ande sozinho nas trilhas",
        descricao="A ideia fazer trilas sozinho(a) pode ser excitante e libertadora, mas esse esporte exige trabalho em equipe porque toda atividade envolve riscos. A prática consciente do Trekking pode ser feita por pessoas de todas as idades, sempre em grupo para termos ajuda em situações excepcionais (acidentes, problemas com veículos, compartilhamento de água ou lanches, etc.).",
        lugar="",
        link="https://www.viviantelles.com.br/10-dicas-para-comecar-no-trekking/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=6,
        titulo="Use roupas adequadas",
        descricao="Para roteiros na primavera ou verão leve calça leve, camisa de manga comprida, chapéu, óculos escuros e bota são itens básicos. Dê preferência para roupas respiráveis e com proteção UV. Evite roupas de algodão porque elas ficam pesadas quando molhadas. Nas trilhas temos que lidar com sol, mosquitos, capins e galhos. A bota ajuda a proteger o tornozelo e evita lesões. Durante o inverno ou em regiões frias pode ser necessário usar roupas térmicas e em camadas.",
        lugar="",
        link="https://www.boipebatur.com.br/post/o-que-levar-para-fazer-trilha/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=2,
        titulo="Cuidado com o sol",
        descricao="Sempre leve protetor solar e chapéu. As atividades de trekking geralmente duram várias horas e não queremos que você tenha uma insolação.",
        lugar="",
        link="https://mundodotrekking.com.br/acessorios-protecao-sol-trilhas/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=3,
        titulo="Alimentação e hidratação",
        descricao="Leve lanches para toda a trilha mesmo que seja curta porque imprevistos podem acontecer. Trekkings de 2 ou mais dias exigem um melhor planejamento das refeições. Também não esqueça de levar água para todo o percurso e consulte a agência de ecoturismo para saber a quantidade mínima (mín. 2L por dia).",
        lugar="",
        link="https://mundodotrekking.com.br/dicas-incriveis-de-comidas-e-lanches-para-trekking/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=4,
        titulo="Mochila para trekking",
        descricao="Não leve muito peso! Trilha não é salão de beleza! Podemos usar a mesma roupa por mais de um dia. Dependendo do roteiro também poderemos lavá-las ao longo do caminho. Leve só o essencial porque você terá de carregar a mochila por todo o percurso.",
        lugar="",
        link="https://levenaviagem.com.br/saiba-o-que-levar-na-mochila-de-trekking/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=5,
        titulo="Respeite seus joelhos",
        descricao="Não fique pulando pedras nem dando saltos desnecessários. Com o passar dos anos isso pode prejudicar seus joehos.",
        lugar="",
        link="https://adrianoleonardi.com.br/artigos/preparar-joelhos-trilhas/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=6,
        titulo="Bastão de caminhada",
        descricao="Caso sinta algum desconforto nos joelhos ou cansaço maior durante as trilhas, avalie usar bastões de caminhadas. O esforço da caminhada e dividida entre os seus inferiores e superiores, aliviando a pressão sobre seus joehos e pernas.",
        lugar="",
        link="https://blog.penatrilha.com.br/bastao-de-caminhada-saiba-como-usar-para-aproveitar-as-vantagens/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=2,
        titulo="Respeite a natureza",
        descricao="Trombas d'água acontecem. Se o tempo estiver nublado com risco de chuva na cabeçeira da trilha cancele a trilha. A chuva que cai ao longo de vários quilômetros acima do rio (à montante) se junta e pode encher rapidamente áreas de cânions ou cursos de rios. Sempre ande com agências experientes principalmente no período chuvoso.",
        lugar="",
        link="https://blog.thenorthface.com.br/dicas/7-regras-para-reduzir-o-impacto-ambiental-em-seu-trekking/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=3,
        titulo="Lanterna, agasalhos e apito",
        descricao="Imprevistos acontecem e uma atividade pode durar mais que o esperadao. Se anoitecer durante o percurso é importante ter um agasalho e uma lanterna. Apito pode ser útil caso alguém se perca.",
        lugar="",
        link="https://www.boipebatur.com.br/post/o-que-levar-para-fazer-trilha/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=4,
        titulo="Planeje com antecedência",
        descricao="Pesquise sobre a trilha antes, converse com a agência sobre o percurso (extensão e nível técnico), verifique os locais de camping ou hospedagem. Alguns distritos ou vilarejos não possuem caixa eletrônico e posto de combustível.",
        lugar="",
        link="https://circuitodoouro.tur.br/blog/2016/09/01/11-cuidados-que-voce-deve-ter-ao-fazer-trekking/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=5,
        titulo="Só leve fotos e recordações",
        descricao="Não deixe lixo na trilha, mesmo que seja orgânico porque o material é exógeno à região e pode desequilibar o ecossistema local. Não retive galhos, folhas ou pedras da trila - se todos que passarem por alí levarem um pedacinho para casa, em breve não haverá mais trilha.",
        lugar="",
        link="https://pisa.tur.br/blog/2022/08/25/trekking-5-dicas-para-comecar-a-praticar/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=6,
        titulo="Seja solidário",
        descricao="Siga a regra de ouro nas trilhas - trate as pessoas como gostaria de ser tratado. Podemos precisar de ajuda para atraver cursos d'água, subir trilhas mais íngremes, dividir lanche ou água, redistribuir o peso da mochila de algum colega que não esteja bem, enfim... seja solidário!",
        lugar="",
        link="https://openspacetrust.org/pt/blog/hiking-tips/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=2,
        titulo="Não interaja com animais silvestres",
        descricao="Por mais fofinhos que alguns animais podem parecer, eles podem possuir parasitas ou bactérias. Respeite-os e se afaste. Não maltrate nem alimente porque não queremos desequilibar o ecossistema local.",
        lugar="",
        link="https://legadodasaguas.com.br/como-praticar-ecoturismo-com-responsabilidade/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=3,
        titulo="Não leve cães ou outros pets para trilhas",
        descricao="Cães e outros pets possuem instinto caçador. Se virem algum animal sivestre, tentarão caçar de podem desequilibrar o ecossistema local.",
        lugar="",
        link="https://altamontanha.com/levar-seu-cao-para-a-montanha-pode-prejudicar-a-fauna-selvagem/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
    Dica(
        id_usuario=4,
        titulo="Experimente diferentes biomas",
        descricao="O Brasil é um país continental e possui diferentes biomas, cada um com suas belezas particulares - Amazônia, Caatinga, Cerrado, Mata Atlântica, Pampa e Pantanal. Algumas áreas de destaque são Serra do Cipó (MG), Serra da Canastra (MG), Chapada Diamantina (BA), Pantanal (MT), Chapada dos Veadeiros (GO), Lençois Maranhenses (MA), Bonito (MS), Alter do Chão (PA), Floresta Amazônica (AM), Jalapão (TO)",
        lugar="",
        link="https://www.cnnbrasil.com.br/viagemegastronomia/viagem/ecoturismo/",
        flag_praia=False,
        flag_montanha=False,
        flag_cachoeira=False,
        flag_camping=False,
        flag_vestuario=False,
        flag_alimentacao=False,
    ),
]


def prencher_banco_dados():
    inspector = inspect(db.engine)
    if inspector.has_table("usuarios") and db.session.query(Usuario).count() == 0:
        print("Populando tabela 'usuarios' banco de dados:")
        for u in usuarios:
            db.session.add(u)
            db.session.commit()
            print(f"Usuário #{u.id}")

    if inspector.has_table("empresas") and db.session.query(Empresa).count() == 0:
        print("Populando tabela 'empresas' banco de dados:")
        for e in empresas:
            db.session.add(e)
            db.session.commit()
            print(f"Empresa #{e.id}")

    if inspector.has_table("dicas") and db.session.query(Dica).count() == 0:
        print("Populando tabela 'empresas' banco de dados:")
        for d in dicas:
            db.session.add(d)
            db.session.commit()
            print(f"Dica #{d.id}")
