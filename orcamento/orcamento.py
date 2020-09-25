from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno, ConsultaAnoMesDesp, ConsultaAnoMesAcao
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
from flask_paginate import Pagination, get_page_parameter
import matplotlib.pyplot as plt
import pygal

orcamento_bp = Blueprint('orcamento', __name__)

@orcamento_bp.route('/orcamento/ReceitasProprias', methods=('GET', 'POST'))

def ReceitasProprias():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ReceitasProprias.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rp_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rp = df_rp_Ano_Mes_Max.Ano.max()
    Mes_max_rp = df_rp_Ano_Mes_Max.Mês.max()
  
    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Mês'] == Mes_max_rp) & (df['Ano'] == Ano_max_rp) &
                    ((df['Objeto (a)'] == 'Crédito Orçamentário Liberado') |
                    (df['Objeto (a)'] == 'Receitas Próprias'))].sum().iloc[5:17]
    df_ano_ant = df[(df['Mês'] == 12) & (df['Ano'] == Ano_max_rp -1) &
                    ((df['Objeto (a)'] == 'Crédito Orçamentário Liberado') |
                    (df['Objeto (a)'] == 'Receitas Próprias'))].sum().iloc[5:17]
    # Criar uma lista com os dados anteriores
    lista_ano_anterior = df_ano_ant.values.tolist()
    lista_ano_atual = df_ano_max.values.tolist()
    


    # -------------------------------------------------------------------------------------------------------------------------#
    df = df[(df['Mês'] == Mes_max_rp) & (df['Ano'] == Ano_max_rp)][['Ano','Mês','Objeto (a)', 'Valores Previstos (b)', 'Jan', 'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Total']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 7
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='Qtde')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Ano','Mês','Objeto (a)', 'Valores Previstos (b)', 'Jan',	'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Total']] #dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_orcamento_rpro.html', Ano= Ano_max_rp, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Receitas Próprias', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_orcamento_rpro.html', Ano = Ano_max_rp, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-striped', table_id="myTable2"),
      titles = 'Receitas Próprias', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/FundosSaldosReceitas', methods=('GET', 'POST'))
def FundosSaldosReceitas():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'FundosSaldosReceitas.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_sfr_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_sfr = df_sfr_Ano_Mes_Max.Ano.max()
    Mes_max_sfr = df_sfr_Ano_Mes_Max.Mês.max()
    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Mês'] == Mes_max_sfr) & (df['Ano'] == Ano_max_sfr) &
                    (df['Fundo (a)'] == 'Fundo de Reaparelhamento (Lei nº 5.832 de 18/03/1994; Res.nº 007/2004 de 07/12/04 e Res.nº 001/08 de 07/08/08)')].sum().iloc[4:16]
    df_ano_ant = df[(df['Mês'] == 12) & (df['Ano'] == Ano_max_sfr -1) &
                    (df['Fundo (a)'] == 'Fundo de Reaparelhamento (Lei nº 5.832 de 18/03/1994; Res.nº 007/2004 de 07/12/04 e Res.nº 001/08 de 07/08/08)')].sum().iloc[4:16]
   # Criar uma lista com os dados anteriores
    lista_ano_anterior = df_ano_ant.values.tolist()
    lista_ano_atual = df_ano_max.values.tolist()
    
    # -------------------------------------------------------------------------------------------------------------------------#
    df = df[(df['Mês'] == Mes_max_sfr) & (df['Ano'] == Ano_max_sfr)][['Ano','Mês','Fundo (a)', 'Saldo do Fundo em Janeiro (b)', 'Jan',	'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Saldo Atual (d)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Ano','Mês','Fundo (a)', 'Saldo do Fundo em Janeiro (b)', 'Jan', 'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Saldo Atual (d)']] #dados filtrados
        return render_template('main_orcamento_fsr.html',Ano = Ano_max_sfr, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Fundos: Saldos e Receitas', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_orcamento_fsr.html',Ano = Ano_max_sfr, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Fundos: Saldos e Receitas', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/DetalhamentoDespesas', methods=('GET', 'POST'))
def DetalhamentoDespesas():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'DetalhamentoDespesas.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_dp_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_dp = df_dp_Ano_Mes_Max.Ano.max()
    Mes_max_dp = df_dp_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Mês'] == Mes_max_dp) & (df['Ano'] == Ano_max_dp)].sum().iloc[4:16]
    df_ano_ant = df[(df['Mês'] == 12) & (df['Ano'] == Ano_max_dp -1)].sum().iloc[4:16]
    # Criar uma lista com os dados anteriores
    lista_ano_anterior = df_ano_ant.values.tolist()
    lista_ano_atual = df_ano_max.values.tolist()
    
    df = df[(df['Mês'] == Mes_max_dp) & (df['Ano'] == Ano_max_dp)][['Ano','Mês','Tipo de Despesa', 'Objeto', 'Valores Previstos', 'Jan',	'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Total']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMesDesp()
  
    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        tdespesa = form.tdespesa.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano)) & (df['Tipo de Despesa']==str(tdespesa))][['Ano','Mês','Tipo de Despesa', 'Objeto', 'Valores Previstos', 'Jan', 'Fev',	'Mar',	'Abr',	'Mai',	'Jun',	'Jul',	'Ago',	'Set',	'Out',	'Nov',	'Dez', 'Total']] #dados filtrados
        return render_template('main_orcamento.html', Ano = Ano_max_dp, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Detalhamento das Despesas', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
    return render_template('main_orcamento.html', Ano = Ano_max_dp, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Detalhamento das Despesas', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/DespesaAcaoOrcamentaria', methods=('GET', 'POST'))
def DespesaAcaoOrcamentaria():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'DespesaAcaoOrcamentaria.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_dao_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_dao = df_dao_Ano_Mes_Max.Ano.max()
    Mes_max_dao = df_dao_Ano_Mes_Max.Mês.max()

#----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Ano'] == Ano_max_dao)].sum().iloc[7]
    df_ano_ant = df[(df['Ano'] == Ano_max_dao -1)].sum().iloc[7]
    # Criar uma lista com os dados anteriores
    lista_ano_anterior = [df_ano_ant, 0]
    lista_ano_atual = [0, df_ano_max]
   

    df = df[(df['Mês'] == Mes_max_dao) & (df['Ano'] == Ano_max_dao)][['Ano','Mês','Descrição da Ação (a)', 'Autorizado (b)', 'Empenhados (c)', 'Liquidados (d)','Pagos (e)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMesAcao()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        tacao = form.tacao.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano)) & (df['Descrição da Ação (a)']==str(tacao))][['Ano','Mês','Descrição da Ação (a)', 'Autorizado (b)', 'Empenhados (c)', 'Liquidados (d)','Pagos (e)']] #dados filtrados
        return render_template('main_orcamento_dao.html', Ano = Ano_max_dao, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Despesas  por Ação Orcamentaria', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_orcamento_dao.html', Ano = Ano_max_dao, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Despesas  por Ação Orcamentaria', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/DespesasCartaoCorporativo', methods=('GET', 'POST'))
def DespesasCartaoCorporativo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'DespesasCartaoCorporativo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_dc_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_dc = df_dc_Ano_Mes_Max.Ano.max()
    Mes_max_dc = df_dc_Ano_Mes_Max.Mês.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Ano'] == Ano_max_dc)].sum().iloc[5]
    df_ano_ant = df[(df['Ano'] == Ano_max_dc -1)].sum().iloc[5]
    # Criar uma lista com os dados anteriores
    lista_ano_anterior = [df_ano_ant, 0]
    lista_ano_atual = [0, df_ano_max]
    
    df = df[(df['Mês'] == Mes_max_dc) & (df['Ano'] == Ano_max_dc)][['Mês', 'Ano', 'Suprido (a)', 'Período de Aplicação (c)', 'Aprovação de Contas (d)', 'Data (e)', 'Nome (f)', 'CNPJ/CPF (g)',  'Motivo (h)', 'Valor Pago (i)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Mês', 'Ano', 'Suprido (a)', 'Período de Aplicação (c)', 'Aprovação de Contas (d)', 'Data (e)', 'Nome (f)', 'CNPJ/CPF (g)',  'Motivo (h)', 'Valor Pago (i)']] #dados filtrados
        #return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
        return render_template('main_orcamento_dcc.html', Ano = Ano_max_dc, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Despesas com Cartão Corporativo e Suprimento de Fundos', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_orcamento_dcc.html', Ano = Ano_max_dc, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Despesas com Cartão Corporativo e Suprimento de Fundos', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

#return render_template('main_orcamento.html',tables=[df.to_html(classes='table table-fluid', table_id="myTable")], form = form, pagination=pagination)
#DataFrame.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=None, escape=True, notebook=False, border=None, table_id=None, render_links=False)[source]
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/OutrosBeneficios', methods=('GET', 'POST'))
def OutrosBeneficios():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'OutrosBeneficios.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_ob_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ob = df_ob_Ano_Mes_Max.Ano.max()
    Mes_max_ob = df_ob_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_ob) & (df['Ano'] == Ano_max_ob)][['Ano', 'Mês', 'Justificativa (a)', 'Nome Recebedor (b)', 'Cargo (c)', 'Valores (d)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano)) & (df['Nome Recebedor (b)'].str.capitalize().str.contains(request.form['Nome'])==True)][['Ano', 'Mês', 'Justificativa (a)', 'Nome Recebedor (b)', 'Cargo (c)', 'Valores (d)']] #dados filtrados
        return render_template('main_orcamento_ob.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Outros Benefícios', form = form, pagination=pagination)

    return render_template('main_orcamento_ob.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Outros Benefícios', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/RepassesPrevidenciarios', methods=('GET', 'POST'))
def RepassesPrevidenciarios():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'RepassesPrevidenciarios.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rpre_Ano_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rpre = df_rpre_Ano_Max.Ano.max()

    #----------Criar grafico-------------------------------------------------#
    # Criação de um DF com apenas informação dos meses e os dois últimos anos
    df_ano_max = df[(df['Ano'] == Ano_max_rpre)].sum().iloc[14]
    df_ano_ant = df[(df['Ano'] == Ano_max_rpre -1)].sum().iloc[14]
    # Criar uma lista com os dados anteriores
    lista_ano_anterior = [df_ano_ant, 0]
    lista_ano_atual = [0, df_ano_max]

    df = df[['Ano','Fundo ou Instituto Previdenciário (a)', 'Ano', 'Jan(b)', 'Fev(c)',	'Mar(d)',	'Abr(e)',	'Mai(f)',	'Jun(g)',	'Jul(h)',	'Ago(i)', 'Set(j)',	'Out(k)', 'Nov(l)',	'Dez(m)', 'Total (n)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df[(df['Ano']==int(ano))][['Ano','Fundo ou Instituto Previdenciário (a)', 'Ano', 'Jan(b)', 'Fev(c)',	'Mar(d)',	'Abr(e)',	'Mai(f)',	'Jun(g)',	'Jul(h)',	'Ago(i)', 'Set(j)',	'Out(k)', 'Nov(l)',	'Dez(m)', 'Total (n)']] #dados filtrados
        return render_template('main_orcamento_rfip.html', Ano = Ano_max_rpre, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Repasses a Fundos e Institutos Previdenciários', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)

    return render_template('main_orcamento_rfip.html', Ano = Ano_max_rpre, tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable"),
      titles = 'Repasses a Fundos e Institutos Previdenciários', form = form, pagination=pagination, lista_ano_anterior=lista_ano_anterior, lista_ano_atual=lista_ano_atual)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/LimiteGastosPessoas', methods=('GET', 'POST'))
def LimiteGastosPessoas():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'LimiteGastosPessoas.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df['Arquivo'] = '<a href="../static/A1/'+df[['Arquivo']]+'">' +df[['Arquivo']]+ '</a>'  # LINK
    df = df[['Ano', 'Período' ,'Arquivo']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 15
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df['Arquivo'] = '<a href= "../static/A1/'+df[['Arquivo']]+'">' +df[['Arquivo']]+ '</a>'  # LINK
        df = df[(df['Ano']==int(ano))][['Ano', 'Período', 'Arquivo']] #dados filtrados
        return render_template('main_orcamento_lgp.html', tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Limites de Gastos Com Pessoas', form = form, pagination=pagination)

    return render_template('main_orcamento_lgp.html', tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Limites de Gastos Com Pessoas', form = form, pagination=pagination)


### -------------------------------------------------------------------------------------------------------------------------------------------------###

@orcamento_bp.route('/orcamento/PrestacaoContasAnual', methods=('GET', 'POST'))
def PrestacaoContasAnual():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'PrestacaoContasAnual.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df['Arquivo'] = '<a href="../static/A2/' + df[['Arquivo']] + '"> ' +df[['Arquivo']]+ '</a>'  # LINK
    df = df[['Ano', 'Arquivo']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 15
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAno()

    if form.validate_on_submit():
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df['Arquivo'] = '<a href="../static/A2/' + df[['Arquivo']] + '"> ' +df[['Arquivo']]+ '</a>'  # LINK
        df = df[(df['Ano']==int(ano))][['Ano', 'Arquivo']] #dados filtrados
        return render_template('main_orcamento_pca.html', tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Prestação Contas Anual', form = form, pagination=pagination)

    return render_template('main_orcamento_pca.html', tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2", escape=False),
      titles = 'Prestação Contas Anual', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

