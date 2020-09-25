from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

planejamento_bp = Blueprint('planejamento', __name__)

@planejamento_bp.route('/planejamento/PlanejamentoEstrategico', methods=('GET', 'POST'))
def PlanejamentoEstrategico():
    return render_template('main_planejamento_map.html')

### -------------------------------------------------------------------------------------------------------------------------------------------------###

@planejamento_bp.route('/planejamento/QuadroDemonstrativo', methods=('GET', 'POST'))
def QuadroDemonstrativo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'QuadroDemonstrativo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df = df[['Objetivos (a)', 'Ação', 'Indicador (b)', 'Meta (c) 2016-2019', 'Resultado alcançado até o momento (d) 2018',
    'Resultado alcançado em 2019 (d)', 'Documento (e)', 'Obs']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[['Objetivos (a)', 'Ação', 'Indicador (b)', 'Meta (c) 2016-2019', 'Resultado alcançado até o momento (d) 2018',
    'Resultado alcançado em 2019 (d)', 'Documento (e)', 'Obs']] #dados filtrados
        return render_template('main_planejamento.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Quadro Demostrativo', form = form, pagination=pagination)

    return render_template('main_planejamento.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Quadro Demostrativo', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@planejamento_bp.route('/planejamento/ResultadosAlcancados', methods=('GET', 'POST'))
def ResultadosAlcancados():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ResultadosAlcancados.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df = df[['Exercicio', 'Resultados Alcançados']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[['Exercicio', 'Resultados Alcançados']]  # dados filtrados

        return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Resultados Alcançados', form=form, pagination=pagination)

    return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Resultados Alcançados', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@planejamento_bp.route('/planejamento/Projetos_MPPA', methods=('GET', 'POST'))
def Projetos_MPPA():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Projetos_MPPA.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df['Arquivo'] = '<a href= ../static/A3/' + df[['Arquivo']] + '> ' +df[['Arquivo']]+ '</a>'  # LINK
    df = df[['Ano', 'Objetivo Estratégico vinculado PEN', 'Nome do Projeto', 'Descrição', 'Situação', 'Arquivo', 'Anexos']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df['Arquivo'] = '<a href="../static/A3/' + df[['Arquivo']] + '"> ' +df[['Arquivo']]+ '</a>'  # LINK
        df = df[['Ano', 'Objetivo Estratégico vinculado PEN', 'Nome do Projeto', 'Descrição', 'Situação', 'Arquivo', 'Anexos']]  # dados filtrados
        return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2", escape=False),
                               titles='Projetos do MPPA Cadastrados no Banco Nacional de Projetos/CNMP', form=form, pagination=pagination)

    return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2", escape=False),
                               titles='Projetos do MPPA Cadastrados no Banco Nacional de Projetos/CNMP', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------#
@planejamento_bp.route('/planejamento/PlanosAtuacao', methods=('GET', 'POST'))
def PlanosAtuacao():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'PlanosAtuacao.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df = df[['Planos de Atuação', 'Anexos']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[['Planos de Atuação', 'Anexos']]  # dados filtrados

        return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Planos de Atuação', form=form, pagination=pagination)

    return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Planos de Atuação', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------#
@planejamento_bp.route('/planejamento/Obras', methods=('GET', 'POST'))
def Obras():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Obras.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df = df[['Tipo', 'Minicípio','Objetivo Estratégico', 'Custo Envolvido', 'Empresa',
       'Data Início', 'Data Fim', 'Percentual de Execução', 'Status']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[['Tipo', 'Minicípio','Objetivo Estratégico', 'Custo Envolvido', 'Empresa',
       'Data Início', 'Data Fim', 'Percentual de Execução', 'Status']]  # dados filtrados

        return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Obras', form=form, pagination=pagination)

    return render_template('main_planejamento.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable"),
                               titles='Obras', form=form, pagination=pagination)
