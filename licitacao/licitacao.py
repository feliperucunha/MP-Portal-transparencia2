from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

licitacao_bp = Blueprint('licitacao', __name__)

@licitacao_bp.route('/licitacao/Licitacoes', methods=('GET', 'POST'))
def Licitacoes():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Licitacoes.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_li_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_li = df_li_Ano_Mes_Max.Ano.max()
    Mes_max_li = df_li_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    i=0
    lista_ano_anterior=[]
    lista_ano_atual=[]
    while i<=Mes_max_li:
        df_ano_max = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_li)].shape
        lista_ano_atual.append(df_ano_max[0])
        i=i+1
    lista_ano_atual.remove(0)
    i=0
    while i<=12:
        df_ano_ant = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_li -1)].shape
        lista_ano_anterior.append(df_ano_ant[0])
        i=i+1
    lista_ano_anterior.append(0)
    lista_ano_anterior.remove(0)   

    df = df[(df['Mês'] == Mes_max_li) & (df['Ano'] == Ano_max_li)][['Ano', 'Mês', 'N° do Edital (a)', 'Data do Edital (b)', 'N° do processo (c)', 'Objeto (d)', 'Tipo (e)', 'Modalidade (f)', 'Situação (g)', 'Resultado (h)']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Ano', 'Mês', 'N° do Edital (a)', 'Data do Edital (b)', 'N° do processo (c)', 'Objeto (d)', 'Tipo (e)', 'Modalidade (f)', 'Situação (g)', 'Resultado (h)']] #dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_licitacao.html', Ano = Ano_max_li, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Licitações', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_licitacao.html', Ano = Ano_max_li, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Licitações', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@licitacao_bp.route('/licitacao/DispensasInexigibilidade', methods=('GET', 'POST'))
def DispensasInexigibilidade():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'DispensasInexigibilidade.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_di_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_di = df_di_Ano_Mes_Max.Ano.max()
    Mes_max_di = df_di_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_di) & (df['Ano'] == Ano_max_di)][['Ano', 'Mês', 'Dispensa /Inexigibilidade de Licitação (a)' , 'Preceito Legal (b)', 'Número do empenho (c) ' , 'Data do empenho (d)', 'Elemento e Subelemento da Despesa (f)',  'Valor do empenho (g)' , 'Contratado(a) (h)', 'CNPJ/CPF (i)','Nr do Contrato', 'Protocolo']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))
        & (df['Dispensa /Inexigibilidade de Licitação (a)'].str.contains(request.form['Dispensa'])==True)
        & (df['Nr do Contrato'].str.contains(request.form['Contrato']) == True)
        & (df['CNPJ/CPF (i)'].str.contains(request.form['CNPJ_CPF']) == True)
        & (df['Número do empenho (c) '].str.contains(request.form['empenho']) == True)]
        [['Ano', 'Mês', 'Dispensa /Inexigibilidade de Licitação (a)' , 'Preceito Legal (b)', 'Número do empenho (c) ' , 'Data do empenho (d)', 'Objeto (e)', 'Elemento e Subelemento da Despesa (f)',  'Valor do empenho (g)' , 'Contratado(a) (h)', 'CNPJ/CPF (i)','Nr do Contrato', 'Protocolo' ]] #dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_licitacao_di.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Dispensas e Inexigibilidade', form = form, pagination=pagination)

    return render_template('main_licitacao_di.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Dispensas e Inexigibilidade', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@licitacao_bp.route('/licitacao/Contrato', methods=('GET', 'POST'))
def Contrato():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Contrato.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)# todos os dados
    df_co_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_co = df_co_Ano_Mes_Max.Ano.max()
    Mes_max_co = df_co_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_co) & (df['Ano'] == Ano_max_co)][['Mês', 'Ano','Nº (a)', 'Objeto (b)', 'Data da Publicação (c)',
    'Nº do Edital (d)', 'Vigência Inicio (e)', 'Vigência Término (e )',
    'Situação (f)', 'Item Fornecido (g)', 'Unidade de Medida (h)',
    'Valor Unitário (i)', 'Quantidade (j)', 'Valor Total do Item (k)',
    'Valor Total do Contrato (l)', 'Contratado (m)', 'CNPJ/CPF (n)',
    'Sócios (o)', 'Termo Aditivo (p)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
        & (df['Nº (a)'].str.contains(request.form['N']) == True)
        & (df['Contratado (m)'].str.contains(request.form['Contratado']) == True)
        & (df['CNPJ/CPF (n)'].str.contains(request.form['CNPJ_CPF']) == True)
        & (df['Situação (f)'].str.contains(request.form['Situacao']) == True)][['Mês', 'Ano','Nº (a)', 'Objeto (b)', 'Data da Publicação (c)',
       'Nº do Edital (d)', 'Vigência Inicio (e)', 'Vigência Término (e )',
       'Situação (f)', 'Item Fornecido (g)', 'Unidade de Medida (h)',
       'Valor Unitário (i)', 'Quantidade (j)', 'Valor Total do Item (k)',
       'Valor Total do Contrato (l)', 'Contratado (m)', 'CNPJ/CPF (n)',
       'Sócios (o)', 'Termo Aditivo (p)', 'Mês', 'Ano']]  # dados filtrados
        return render_template('main_licitacao_con.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles='Contratos', form=form, pagination=pagination)

    return render_template('main_licitacao_con.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
        titles='Contratos', form=form, pagination=pagination)
    ### -------------------------------------------------------------------------------------------------------------------------------------------------###

@licitacao_bp.route('/licitacao/TA_Contrato', methods=('GET', 'POST'))
def TA_Contrato():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'TA_Contrato.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Nº. do Contrato (a)', 'Nº. do Aditivo (b)', 'Objetivo (c)', 'Data de Publicação (d)', 'Valor Total (e)']]  # dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
        & (df['Nº. do Contrato (a)'].str.contains(request.form['N']) == True)]
        [['Mes', 'Ano', 'Nº. do Contrato (a)', 'Nº. do Aditivo (b)', 'Objetivo (c)', 'Data de Publicação (d)', 'Valor Total (e)']]
        return render_template('main_licitacao_TA.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',                                                                                         table_id="myTable2"),
    titles='Contratos (Termos Aditivos)', form=form, pagination=pagination)

    return render_template('main_licitacao_TA.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles='Contratos (Termos Aditivos)', form=form, pagination=pagination)

# ------------------------------------------------------------------------------------------------------------------------------------ #

@licitacao_bp.route('/licitacao/ContratoInstrumentoCongenere', methods=('GET', 'POST'))
def ContratoInstrumentoCongenere():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContratoInstrumentoCongenere.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    i=0
    lista_ano_anterior=[]
    lista_ano_atual=[]
    while i<=Mes_max_ta:
        df_ano_max = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta)].shape
        lista_ano_atual.append(df_ano_max[0])
        i=i+1
    lista_ano_atual.remove(0)
    i=0
    while i<=12:
        df_ano_ant = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta -1)].shape
        lista_ano_anterior.append(df_ano_ant[0])
        i=i+1
    lista_ano_anterior.append(0)
    lista_ano_anterior.remove(0)   
    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Nº. do Contrato (a)', 'Tipo de Instrumento (b)', 'Objetivo (c)',
       'Data de Publicação (d)', 'Nº. do Processo (e)', 'Vigência Início (l)', 'Vigência Término (l)', 'Situação (g)',
       'Convenente (h)', 'CNPJ/CPF (i)', 'Representantes (j)', 'Valor do Repasse (k)', 'Contrapartida (f)', 'Prestação de Contas (m)', 'Termo Aditivo (n)']]

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Mês', 'Ano', 'Nº. do Contrato (a)', 'Tipo de Instrumento (b)', 'Objetivo (c)',
       'Data de Publicação (d)', 'Nº. do Processo (e)', 'Vigência Início (l)', 'Vigência Término (l)', 'Situação (g)',
       'Convenente (h)', 'CNPJ/CPF (i)', 'Representantes (j)', 'Valor do Repasse (k)', 'Contrapartida (f)', 'Prestação de Contas (m)', 'Termo Aditivo (n)']]

        return render_template('main_licitacao_cic.html', Ano = Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
        titles='Convênios e Instrumentos Congêneres', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_licitacao_cic.html', Ano = Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
        titles='Convênios e Instrumentos Congêneres', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

#--------------------------------------------------------------------------------------------------------------------------------------#

@licitacao_bp.route('/licitacao/TA_ContratoInstrumentoCongenere', methods=('GET', 'POST'))
def TA_ContratoInstrumentoCongenere():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'TA_ContratoInstrumentoCongenere.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Nº do Convênio (a)', 'Nº. do Aditivo (b)', 'Tipo de Instrumento',
       'Objetivo (c)', 'Convenente', 'Data de Publicação (d)', 'Valor Total (e)']]

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
        & (df['Nº do Convênio (a)'].str.contains(request.form['N']) == True)][['Mês', 'Ano', 'Nº do Convênio (a)', 'Nº. do Aditivo (b)', 'Tipo de Instrumento',
       'Objetivo (c)', 'Convenente', 'Data de Publicação (d)', 'Valor Total (e)']]

        return render_template('main_licitacao_TA_cic.html',tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Convênios e Instrumentos Congêneres (Termos Aditivos)', form=form, pagination=pagination)

    return render_template('main_licitacao_TA_cic.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Convênios e Instrumentos Congêneres (Termos Aditivos)', form=form, pagination=pagination)

#--------------------------------------------------------------------------------------------------------------------------------------##

@licitacao_bp.route('/licitacao/AtasRegistroPrecos', methods=('GET', 'POST'))
def AtasRegistroPrecos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'AtasRegistroPrecos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    i=0
    lista_ano_anterior=[]
    lista_ano_atual=[]
    while i<=Mes_max_ta:
        df_ano_max = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta)].shape
        lista_ano_atual.append(df_ano_max[0])
        i=i+1
    lista_ano_atual.remove(0)
    i=0
    while i<=12:
        df_ano_ant = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta -1)].shape
        lista_ano_anterior.append(df_ano_ant[0])
        i=i+1
    lista_ano_anterior.append(0)
    lista_ano_anterior.remove(0)   

    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Nº (a)', 'Situação', 'Órgão Gerenciador da Ata (b)', 'Objeto (c)',
       'Data da Publicação (d)', 'Nº do Edital do Processo (e)', 'Vigência Início (f)', 'Vigência Termino (f)', 'Ítem Registrado (g)', 'Unidade de Medida (h)',
       'Valor Unitário (i)', 'Quantidade (j)', 'Valor Total do Ítem (k)', 'Valor Total do Contrato (l)', 'Contratado (m)', 'CNPJ/CPF (n)', 'Sócios (o)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Mês', 'Ano', 'Nº (a)', 'Situação', 'Órgão Gerenciador da Ata (b)', 'Objeto (c)',
       'Data da Publicação (d)', 'Nº do Edital do Processo (e)', 'Vigência Início (f)', 'Vigência Termino (f)', 'Ítem Registrado (g)', 'Unidade de Medida (h)',
       'Valor Unitário (i)', 'Quantidade (j)', 'Valor Total do Ítem (k)', 'Valor Total do Contrato (l)', 'Contratado (m)', 'CNPJ/CPF (n)', 'Sócios (o)']]


        return render_template('main_licitacao_arp.html', Ano = Ano_max_ta,tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Atas de Registro de Preços Próprias e Aderidas', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_licitacao_arp.html', Ano = Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Atas de Registro de Preços Próprias e Aderidas', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
#------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------

@licitacao_bp.route('/licitacao/TA_AtasRegistroPrecos', methods=('GET', 'POST'))
def TA_AtasRegistroPrecos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'TA_AtasRegistroPrecos.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Nº da ARP (a)', 'Nº do Aditivo (b)', 'Objeto (c)', 'Data da Publicação (d)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
        & (df['Nº da ARP (a)'].str.contains(request.form['N'])== True)][['Mês', 'Ano', 'Nº da ARP (a)', 'Nº do Aditivo (b)', 'Objeto (c)','Data da Publicação (d)']]
        return render_template('main_licitacao_TA_arp.html', Ano = Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Atas de Registro de Preços (próprias e adesões) Termos Aditivos', form=form, pagination=pagination)

    return render_template('main_licitacao_TA_arp.html', Ano = Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Atas de Registro de Preços (próprias e adesões) Termos Aditivos', form=form, pagination=pagination)

#----------------------------------------------------------------------------------------------------------------------------

@licitacao_bp.route('/licitacao/PrestadoresServico', methods=('GET', 'POST'))
def PrestadoresServico():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'PrestadoresServico.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_ta_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ta = df_ta_Ano_Mes_Max.Ano.max()
    Mes_max_ta = df_ta_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    i=1
    lista_ano_anterior=[]
    lista_ano_atual=[]
    while i<=Mes_max_ta:
        df_ano_max = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta)].shape
        lista_ano_atual.append(df_ano_max[0])
        i=i+1
    i=1
    while i<=12:
        df_ano_ant = df[(df['Mês'] == i) & (df['Ano'] == Ano_max_ta -1)].shape
        lista_ano_anterior.append(df_ano_ant[0])
        i=i+1  

    df = df[(df['Mês'] == Mes_max_ta) & (df['Ano'] == Ano_max_ta)][['Mês', 'Ano', 'Empresa Contratada (a)', 'Nº. do Contrato (b)',
       'Nome (c)', 'CPF (d)', 'Cargo/Atividade Exercida (e)', 'Unidade Administrativa (f)']]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
        ][['Mês', 'Ano', 'Empresa Contratada (a)', 'Nº. do Contrato (b)',
       'Nome (c)', 'CPF (d)', 'Cargo/Atividade Exercida (e)', 'Unidade Administrativa (f)']]
        return render_template('main_licitacao_ps.html', Ano=Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Prestadores de Serviços', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_licitacao_ps.html', Ano=Ano_max_ta, tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',table_id="myTable2"),
    titles='Prestadores de Serviços', form=form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)


