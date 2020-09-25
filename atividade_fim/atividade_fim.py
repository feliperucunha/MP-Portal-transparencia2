from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

atividade_fim_bp = Blueprint('atividade_fim', __name__)

@atividade_fim_bp.route('/atividade_fim/EstudoLevantamentoEstatistico', methods=('GET', 'POST'))
def EstudoLevantamentoEstatistico():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'EstudoLevantamentoEstatistico.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df['Link'] = '<a href="../static/A4/' + df[['Link']] + '"> ' +df[['Link']]+ '</a>'  # LINK
    df = df[['Ano', 'Nome do Documento', 'Link']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df['Link'] = '<a href="../static/A4/' + df[['Link']] + '"> ' +df[['Link']]+ '</a>'  # LINK
        df = df[(df['Ano']==int(ano))][['Ano', 'Nome do Documento', 'Link']] #dados filtrados
        return render_template('main_atividade_fim.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Estudo e Levantamentos Estatisticos da Atuação', form = form, pagination=pagination)

    return render_template('main_atividade_fim.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Estudo e Levantamentos Estatisticos da Atuação', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###
