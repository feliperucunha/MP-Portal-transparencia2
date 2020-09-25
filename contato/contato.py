from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
from flask_paginate import Pagination, get_page_parameter

contato_bp = Blueprint('contato', __name__)


@contato_bp.route('/contato/RegistroCompetencias', methods=('GET', 'POST'))
def RegistroCompetencias():
    return render_template('main_contato_rc.html')
### -------------------------------------------------------------------------------------------------------------------------------------------------

@contato_bp.route('/contato/EstruturaOrganizacional', methods=('GET', 'POST'))
def EstruturaOrganizacional():
    return render_template('main_contato_eo.html')
### -------------------------------------------------------------------------------------------------------------------------------------------------


@contato_bp.route('/contato/UnidadesEnderecosTelefones', methods=('GET', 'POST'))
def UnidadesEnderecosTelefones():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'UnidadesEnderecosTelefones.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df = df[['Departamento', 'Nome da Unidade (a)', 'Endereço', 'CEP', 'Caracteristica do Imovel (b)', 'Telefone', 'Fax', 'Horário de Atendimento', 'Email', 'Acessibilidade']]

   ## # Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Nome da Unidade (a)'].str.contains(request.form['unidade']) == True)][['Departamento', 'Nome da Unidade (a)', 'Endereço', 'CEP', 'Caracteristica do Imovel (b)', 'Telefone', 'Fax', 'Horário de Atendimento', 'Email', 'Acessibilidade']]  # dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_contato.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Endereço das Unidades', form = form, pagination=pagination)

    return render_template('main_contato.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Endereço das Unidades', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@contato_bp.route('/contato/Email_Membros', methods=('GET', 'POST'))
def Email_Membros():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Email_Membros.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df = df[['Nome do Membro', 'Cargo (a)', 'Lotação (b)', 'E-mail Institucional']]

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[['Nome do Membro', 'Cargo (a)', 'Lotação (b)', 'E-mail Institucional']]  # dados filtrados

        return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='E-mail funcional dos membros', form=form, pagination=pagination)

    return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='E-mail funcional dos membros', form=form, pagination=pagination)

### -----------------------------------------------------------------------------------------------------------------------------------