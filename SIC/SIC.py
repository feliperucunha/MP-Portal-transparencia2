from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

SIC_bp = Blueprint('SIC', __name__)

@SIC_bp.route('/SIC/UnidadeAutoridadeResponsável', methods=('GET', 'POST'))
def UnidadeAutoridadeResponsável():
    return render_template('main_SIC_uar.html', titles = 'Ouvidoria do Ministério Público do Estado do Pará')
### -------------------------------------------------------------------------------------------------------------------------------------------------
#teste de comunicaçãogit add .
@SIC_bp.route('/SIC/PublicacaoAnualSIC', methods=('GET', 'POST'))
def PublicacaoAnualSIC():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'PublicacaoAnualSIC.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df = df[(df['Ano'] == df.Ano.max())][['Ano', 'Publicação', 'Link']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Ano']==int(ano))][['Ano', 'Publicação', 'Link']] #dados filtrados
        return render_template('main_SIC.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'SIC', form = form, pagination=pagination)

    return render_template('main_SIC.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'SIC', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###
