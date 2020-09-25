from flask import Flask, render_template
from atividade_fim.atividade_fim import atividade_fim_bp
from contato.contato import contato_bp
from orcamento.orcamento import orcamento_bp
from licitacao.licitacao import licitacao_bp
from gestao_pessoas.gestao_pessoas import gestao_pessoas_bp
from planejamento.planejamento import planejamento_bp
from contracheque.contracheque import contracheque_bp
from SIC.SIC import SIC_bp
from publicacao_anual_SIC.publicacao_anual_SIC import publicacao_anual_SIC_bp
from menu.menu import menu_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lablam.2017'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='enter_your_public_key'
app.config['RECAPTCHA_PRIVATE_KEY']='enter_your_private_key'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}

app.register_blueprint(atividade_fim_bp)
app.register_blueprint(contato_bp)
app.register_blueprint(orcamento_bp)
app.register_blueprint(licitacao_bp)
app.register_blueprint(gestao_pessoas_bp)
app.register_blueprint(planejamento_bp)
app.register_blueprint(contracheque_bp)
app.register_blueprint(SIC_bp)
app.register_blueprint(publicacao_anual_SIC_bp)
app.register_blueprint(menu_bp)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
