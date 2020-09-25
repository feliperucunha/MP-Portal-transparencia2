from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

gestao_pessoas_bp = Blueprint('gestao_pessoas', __name__)

@gestao_pessoas_bp.route('/gestao_pessoas/MembrosAtivos', methods=('GET', 'POST'))
def MembrosAtivos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'MembrosAtivos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Matrícula (a)', 'Nome(b)', 'Cargo Efetivo(c)', 'Função (d)', 'Lotação (e)', 'Nomeação Ato/Portaria Nº(f)', 'Nomeação Data Publicação(g)', 'Vitalício (h)']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Ano', 'Mês','Matrícula (a)', 'Nome(b)', 'Cargo Efetivo(c)', 'Função (d)', 'Lotação (e)', 'Nomeação Ato/Portaria Nº(f)', 'Nomeação Data Publicação(g)', 'Vitalício (h)']] #dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_gestao_pessoas.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Quadro de Membros Ativos', form = form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Quadro de Membros Ativos', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@gestao_pessoas_bp.route('/gestao_pessoas/MembrosInativos', methods=('GET', 'POST'))
def MembrosInativos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'MembrosInativos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Mês', 'Ano', 'Matrícula (a)', 'Nome (b)', 'Cargo Efetivo (c)',  'Nomeação Ato/portaria nº (d)',
    'Nomeação Data Publicação (e)', 'Aposentadoria Ato/portaria nº (f)',  'Aposentadoria Data Publicação (g)']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Mês', 'Ano', 'Matrícula (a)', 'Nome (b)', 'Cargo Efetivo (c)',  'Nomeação Ato/portaria nº (d)',
    'Nomeação Data Publicação (e)', 'Aposentadoria Ato/portaria nº (f)',  'Aposentadoria Data Publicação (g)']] #dados filtrados
        return render_template('main_gestao_pessoas.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Quadro de Membros Inativos', form = form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Quadro de Membros Inativos', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@gestao_pessoas_bp.route('/gestao_pessoas/ServidoresAtivos', methods=('GET', 'POST'))
def ServidoresAtivos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ServidoresAtivos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Mês', 'Ano', 'Matrícula (a)', 'Nome(b)', 'Cargo Efetivo (c)', 'Função (d)',
    'Lotação (e)', 'Nomeação Ato/Portaria n. (f)', 'Nomeação Data publicação (g)', 'Estável(h)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Mês', 'Ano', 'Matrícula (a)', 'Nome(b)', 'Cargo Efetivo (c)', 'Função (d)',
    'Lotação (e)', 'Nomeação Ato/Portaria n. (f)', 'Nomeação Data publicação (g)', 'Estável(h)']]  # dados filtrados
        # return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Servidores Ativos', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Servidores Ativos', form=form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@gestao_pessoas_bp.route('/gestao_pessoas/ServidoresInativos', methods=('GET', 'POST'))
def ServidoresInativos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ServidoresInativos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Mês', 'Ano', 'Matrícula (a)', 'Nome (b)', 'Cargo Efetivo (c)', 'Nomeação Ato/portaria nº (d)', 'Nomeação Data publicação (e)',
       'Aposentadoria Ato/portaria nº (f)', 'Aposentadoria Data publicação (g)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Mês', 'Ano', 'Matrícula (a)', 'Nome (b)', 'Cargo Efetivo (c)', 'Nomeação Ato/portaria nº (d)', 'Nomeação Data publicação (e)',
       'Aposentadoria Ato/portaria nº (f)', 'Aposentadoria Data publicação (g)']]  # dados filtrados
        # return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Servidores Inativos', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Servidores Inativos', form=form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@gestao_pessoas_bp.route('/gestao_pessoas/Pensionistas', methods=('GET', 'POST'))
def Pensionistas():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Pensionistas.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Instituidor da Pensão(a)', 'Cargo Efetivo (b)', 'Pensionista(c)',
       'Ato/Portaria nº (d)', 'Data publicação (e)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Instituidor da Pensão(a)', 'Cargo Efetivo (b)', 'Pensionista(c)',
       'Ato/Portaria nº (d)', 'Data publicação (e)']]  # dados filtrados
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Pensionistas', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Pensionistas', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@gestao_pessoas_bp.route('/gestao_pessoas/CedidosPeloMP', methods=('GET', 'POST'))
def CedidosPeloMP():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'CedidosPeloMP.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Cargo (c)', 'Função (d)',
       'Lotação (e)', 'Ato/portaria nº (f)', 'Data publicação (g)',
       'Órgão de Destino (h)', 'Ônus (i)', 'Prazo (j)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Cargo (c)', 'Função (d)',
       'Lotação (e)', 'Ato/portaria nº (f)', 'Data publicação (g)',
       'Órgão de Destino (h)', 'Ônus (i)', 'Prazo (j)']] # dados filtrados

        return render_template('main_gestao_pessoas.html',tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),titles='Cedidos Pelo MP', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
                               titles='Cedidos Pelo MP', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@gestao_pessoas_bp.route('/gestao_pessoas/CedidosParaMP', methods=('GET', 'POST'))
def CedidosParaMP():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'CedidosParaMP.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Cargo de Origem (c)', 'Cargo Atual (d)', 'Função (e)', 'Lotação (f)',
       'Ato/portaria nº (g)', 'Data publicação (h)', 'Órgão de Origem (i)', 'Ônus (j)', 'Prazo (k)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Cargo de Origem (c)', 'Cargo Atual (d)', 'Função (e)', 'Lotação (f)',
       'Ato/portaria nº (g)', 'Data publicação (h)', 'Órgão de Origem (i)', 'Ônus (j)', 'Prazo (k)']]  # dados filtrados
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Cedidos Para MP', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Cedidos Para MP', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@gestao_pessoas_bp.route('/gestao_pessoas/MembroFuncaoGratificada', methods=('GET', 'POST'))
def MembroFuncaoGratificada():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'MembroFuncaoGratificada.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Gratificação (c)', 'Lotação (d)',
     'Nomeação - Ato/Portaria nº (e)', 'Nomeação Data Publicação (f)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Gratificação (c)', 'Lotação (d)',
       'Nomeação - Ato/Portaria nº (e)', 'Nomeação Data Publicação (f)']]  # dados filtrados

        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Membro Função Gratificada', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Membro Função Gratificada', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@gestao_pessoas_bp.route('/gestao_pessoas/ServidorFuncaoGratificada', methods=('GET', 'POST'))
def ServidorFuncaoGratificada():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ServidorFuncaoGratificada.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Gratificação (c)', 'Lotação (d)',
       'Vínculo Efetivo (e)', 'Ato/Portaria (f)', 'Data da Publicação (g)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Matrícula (a)', 'Nome (b)', 'Gratificação (c)', 'Lotação (d)',
       'Vínculo Efetivo (e)', 'Ato/Portaria (f)', 'Data da Publicação (g)']]

        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Servidores de Função Gratificada', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Servidores de Função Gratificada', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###

@gestao_pessoas_bp.route('/gestao_pessoas/EstRemuneratoriaCargoFuncaoMembro', methods=('GET', 'POST'))
def EstRemuneratoriaCargoFuncaoMembro():
# cargo
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'EstRemuneratoriaCargoMembro.json')
    json_data = json.load(open(json_url))
    df_cargo = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_cargo[df_cargo['Ano'] == df_cargo.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_cargo = df_cargo[(df_cargo['Mês'] == Mes_max_ma) & (df_cargo['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Cargo', 'Valor']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 15
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_cargo), record_name='df_cargo')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_cargo = pd.DataFrame(json_data)  # todos os dados
        df_cargo = df_cargo[(df_cargo['Mês'] == int(mes)) & (df_cargo['Ano'] == int(ano))][['Ano', 'Mês','Cargo', 'Valor']]
# função
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'EstRemuneratoriaFuncaoMembro.json')
    json_data = json.load(open(json_url))
    df_funcao = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_funcao[df_funcao['Ano'] == df_funcao.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_funcao = df_funcao[(df_funcao['Mês'] == Mes_max_ma) & (df_funcao['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Função', 'Valor']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 15
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_funcao), record_name='df_funcao')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_funcao = pd.DataFrame(json_data)  # todos os dados
        df_funcao = df_funcao[(df_funcao['Mês'] == int(mes)) & (df_funcao['Ano'] == int(ano))][['Ano', 'Mês', 'Função', 'Valor']]

        return render_template('main_gestao_pessoas_erm.html',
                               tables_cargo=df_cargo[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
                               tables_funcao=df_funcao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
                               titles='Estrutura Remuneratória de Membro', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas_erm.html',
                            tables_cargo=df_cargo[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
                            tables_funcao=df_funcao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
                               titles='Estrutura Remuneratória de Membro', form=form, pagination=pagination)


### -------------------------------------------------------------------------------------------------------------------------------------------------

@gestao_pessoas_bp.route('/gestao_pessoas/RemuneracaoVencimentoCargoFuncaoServidores', methods=('GET', 'POST'))
def RemuneracaoVencimentoCargoFuncaoServidores():
# Remuneração
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'RemuneracaoServidores.json')
    json_data = json.load(open(json_url))
    df_Remuneracao = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_Remuneracao[df_Remuneracao['Ano'] == df_Remuneracao.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_Remuneracao = df_Remuneracao[(df_Remuneracao['Mês'] == Mes_max_ma) & (df_Remuneracao['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Cargo', 'Remuneração #']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_Remuneracao), record_name='df_Remuneracao')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_Remuneracao = pd.DataFrame(json_data)  # todos os dados
        df_Remuneracao = df_Remuneracao [(df_Remuneracao['Mês'] == int(mes)) & (df_Remuneracao['Ano'] == int(ano))][['Ano', 'Mês', 'Cargo', 'Remuneração #']]

# Vencimento
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'VencimentoBaseServidores.json')
    json_data = json.load(open(json_url))
    df_vencimento = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_vencimento[df_vencimento['Ano'] == df_vencimento.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_vencimento = df_vencimento[(df_vencimento['Mês'] == Mes_max_ma) & (df_vencimento['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Cargo', 'Vencimento Base']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_vencimento), record_name='df_vencimento')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_vencimento = pd.DataFrame(json_data)  # todos os dados
        df_vencimento = df_vencimento[(df_vencimento['Mês'] == int(mes)) & (df_vencimento['Ano'] == int(ano))][['Ano', 'Mês', 'Cargo', 'Vencimento Base']]

# Comissão
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'CargoComissaoServidores.json')
    json_data = json.load(open(json_url))
    df_comissao = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_comissao[df_comissao['Ano'] == df_comissao.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_comissao = df_comissao[(df_comissao['Mês'] == Mes_max_ma) & (df_comissao['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Cargo de Provimento em Comissão', 'Remuneração *']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_comissao), record_name='df_comissao')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_comissao= pd.DataFrame(json_data)  # todos os dados
        df_comissao= df_comissao[(df_comissao['Mês'] == int(mes)) & (df_comissao['Ano'] == int(ano))][['Ano', 'Mês', 'Cargo de Provimento em Comissão', 'Remuneração *']]

# FuncaoServidores
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'FuncaoServidores.json')
    json_data = json.load(open(json_url))
    df_funcao = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df_funcao[df_funcao['Ano'] == df_funcao.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df_funcao = df_funcao[(df_funcao['Mês'] == Mes_max_ma) & (df_funcao['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Função', 'Valor']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df_funcao), record_name='df_funcao')
    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df_funcao = pd.DataFrame(json_data)  # todos os dados
        df_funcao = df_funcao[(df_funcao['Mês'] == int(mes)) & (df_funcao['Ano'] == int(ano))][['Ano', 'Mês', 'Função', 'Valor']]

        return render_template('main_gestao_pessoas_ers.html',
                               tables_remuneracao=df_Remuneracao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                                   classes='table table-fluid',
                                   table_id="myTable2"),
                               tables_Fservidores=df_funcao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                                   classes='table table-fluid', table_id="myTable2"),
                               tables_Vencimento=df_vencimento[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                                   classes='table table-fluid', table_id="myTable2"),
                               tables_comissao=df_comissao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                                   classes='table table-fluid', table_id="myTable2"),
                               titles='Estrutura Remuneratória de Servidor', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas_ers.html',
                           tables_remuneracao=df_Remuneracao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                               classes='table table-fluid',
                               table_id="myTable2"),
                           tables_Fservidores=df_funcao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                               classes='table table-fluid', table_id="myTable2"),
                           tables_Vencimento=df_vencimento[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                               classes='table table-fluid', table_id="myTable2"),
                           tables_comissao=df_comissao[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(
                               classes='table table-fluid', table_id="myTable2"),
                           titles='Estrutura Remuneratória de Servidor', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/FuncaoServidores', methods=('GET', 'POST'))
def FuncaoServidores():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'FuncaoServidores.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Função', 'Valor']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')
    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Função', 'Valor']]

        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Função Servidores', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Função Servidores', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------

@gestao_pessoas_bp.route('/gestao_pessoas/Estagiarios', methods=('GET', 'POST'))
def Estagiarios():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Estagiarios.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][
        ['Ano', 'Mês', 'Especialidade (c) ', 'Nome (a)', 'Nível (b)', 'Obrigatório (d)', 'Prazo (e)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
            ['Ano', 'Mês', 'Especialidade (c) ', 'Nome (a)', 'Nível (b)', 'Obrigatório (d)', 'Prazo (e)']]  # dados filtrados
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Estagiários', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Estagiários', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------

@gestao_pessoas_bp.route('/gestao_pessoas/PlanoCarreira', methods=('GET', 'POST'))
def PlanoCarreira():
    return render_template('main_gestao_pessoas_pc.html')

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/CargoVagosOcupadosMembros', methods=('GET', 'POST'))
def CargoVagosOcupadosMembros():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'CargoVagosOcupadosMembros.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][
        ['Ano', 'Mês', 'Cargos (a)', 'Existentes (b)', 'Ocupados (c)','Ocupados (c)', 'Vagos (d)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        if form.validate_on_submit():
            mes = form.mes.data
            ano = form.ano.data
            df = pd.DataFrame(json_data)  # todos os dados
            df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
                ['Ano', 'Mês', 'Cargos (a)', 'Existentes (b)', 'Ocupados (c)','Ocupados (c)', 'Vagos (d)']]

        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Cargos Vagos Ocupados pelos Membros', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Cargos Vagos Ocupados pelos Membros', form=form, pagination=pagination)


### -------------------------------------------------------------------------------------------------------------------------------------------------

@gestao_pessoas_bp.route('/gestao_pessoas/CargoVagosOcupadosServidores', methods=('GET', 'POST'))
def CargoVagosOcupadosServidores():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'CargoVagosOcupadosServidores.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][
        ['Mês', 'Ano', 'Cargos (a)', 'Existentes (b)', 'Ocupados (c)', 'Vagos (d)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        if form.validate_on_submit():
            mes = form.mes.data
            ano = form.ano.data
            df = pd.DataFrame(json_data)  # todos os dados
            df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Mês', 'Ano', 'Cargos (a)', 'Existentes (b)', 'Ocupados (c)', 'Vagos (d)']]

        return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Cargos Vagos Ocupados pelos Servidores', form=form, pagination=pagination)

    return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Cargos Vagos Ocupados pelos Servidores', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/FuncoesVagasOcupadas', methods=('GET', 'POST'))
def FuncoesVagasOcupadas():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'FuncoesVagasOcupadas.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês', 'Descrição (a)', 'Existentes (b)', 'Ocupados com vinculo (c) Membros',
       'Ocupados com vinculo (c) Servidores', 'Sem vínculo (d)', 'Vagos (e= (b) (c) (d))']]  # dados filtrados

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        if form.validate_on_submit():
            mes = form.mes.data
            ano = form.ano.data
            df = pd.DataFrame(json_data)  # todos os dados
            df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
                ['Ano', 'Mês', 'Descrição (a)', 'Existentes (b)', 'Ocupados com vinculo (c) Membros',
       'Ocupados com vinculo (c) Servidores', 'Sem vínculo (d)', 'Vagos (e= (b) (c) (d))']]


        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Cargos Vagos Ocupados pelos Servidores', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Cargos Vagos Ocupados pelos Servidores', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/ProvimentoMembros', methods=('GET', 'POST'))
def ProvimentoMembros():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ProvimentoMembros.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        if form.validate_on_submit():
            mes = form.mes.data
            ano = form.ano.data
            df = pd.DataFrame(json_data)  # todos os dados
            df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]

        return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Provimento dos Membros', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Provimento dos Membros', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/ProvimentoServidores', methods=('GET', 'POST'))
def ProvimentoServidores():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ProvimentoServidores.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
    Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        if form.validate_on_submit():
            mes = form.mes.data
            ano = form.ano.data
            df = pd.DataFrame(json_data)  # todos os dados
            df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]

        return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Provimento dos Servidores', form=form, pagination=pagination)
    return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Provimento dos Servidores', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/VacanciaMembros', methods=('GET', 'POST'))
def VacanciaMembros():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'json_files', 'VacanciaMembros.json')
        json_data = json.load(open(json_url))
        df = pd.DataFrame(json_data)  # todos os dados
        df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
        Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
        Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
        df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][
            ['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]  # dados filtrados
        page = request.args.get(get_page_parameter(), type=int, default=1)
        PER_PAGE = 5
        pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

        form = ConsultaAnoMes()

        if form.validate_on_submit():
            if form.validate_on_submit():
                mes = form.mes.data
                ano = form.ano.data
                df = pd.DataFrame(json_data)  # todos os dados
                df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
                    ['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]

            return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Vacâncias Membros', form=form, pagination=pagination)
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Vacâncias Membros', form=form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------
@gestao_pessoas_bp.route('/gestao_pessoas/VacanciaServidores', methods=('GET', 'POST'))
def VacanciaServidores():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'json_files', 'VacanciaServidores.json')
        json_data = json.load(open(json_url))
        df = pd.DataFrame(json_data)  # todos os dados
        df_ma_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
        Ano_max_ma = df_ma_Ano_Mes_Max.Ano.max()
        Mes_max_ma = df_ma_Ano_Mes_Max.Mês.max()
        df = df[(df['Mês'] == Mes_max_ma) & (df['Ano'] == Ano_max_ma)][
            ['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]  # dados filtrados
        page = request.args.get(get_page_parameter(), type=int, default=1)
        PER_PAGE = 5
        pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

        form = ConsultaAnoMes()

        if form.validate_on_submit():
            if form.validate_on_submit():
                mes = form.mes.data
                ano = form.ano.data
                df = pd.DataFrame(json_data)  # todos os dados
                df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
                    ['Ano', 'Mês','Nome (a)', 'Cargo Efetivo (b)', 'Ato/Portaria nº (c)', 'Data Publicação (d)']]

            return render_template('main_gestao_pessoas.html',
                                   tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                            table_id="myTable2"),
                                   titles='Vacância dos Servidores', form=form, pagination=pagination)
        return render_template('main_gestao_pessoas.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Vacância dos Servidores', form=form, pagination=pagination)
