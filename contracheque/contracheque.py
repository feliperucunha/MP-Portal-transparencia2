from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes, ConsultaAno
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

contracheque_bp = Blueprint('contracheque', __name__)


@contracheque_bp.route('/contracheque/RemuneracaoMembroAtivo', methods=('GET', 'POST'))
def RemuneracaoMembroAtivo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContraCheque_MembroAtivo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    #alterar aqui os dados que vão aparecer
    df = df[['Ano', 'Mês','Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
                & (df['Matrícula'].str.contains(request.form['Matricula']) == True)
                & (df['Nome'].str.contains(request.form['Nome']) == True)]
        df = df[['Matrícula', 'Nome', 'Cargo', 'Lotação', 'Remun. do Cargo Efetivo(1)', 'Outras Verbas Remuneratórias ou Legais/Judiciais (2)', 'Função de Confiança ou Cargo em Comissão (3)', 'Gratif. Natalina (4)', 'Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)', 'Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)', 'Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']]  # dados filtrados

        #[['Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
       #alterar main_contracheque
        return render_template('main_contracheque_rma.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração de Membros Ativos', form = form, pagination=pagination)

    return render_template('main_contracheque_rma.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Membros Ativos', form = form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###

@contracheque_bp.route('/contracheque/RemuneracaoMembroInativo', methods=('GET', 'POST'))
def RemuneracaoMembroInativo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContraCheque_MembroInativo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    #alterar aqui os dados que vão aparecer
    df = df[['Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
                & (df['Matrícula'].str.contains(request.form['Matrícula']) == True)
                & (df['Nome'].str.contains(request.form['Nome']) == True)]
        df = df[['Matrícula', 'Nome', 'Cargo', 'Lotação', 'Remun. do Cargo Efetivo(1)', 'Outras Verbas Remuneratórias ou Legais/Judiciais (2)', 'Função de Confiança ou Cargo em Comissão (3)', 'Gratif. Natalina (4)', 'Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)', 'Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)', 'Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']]  # dados filtrados
        # alterar main_contracheque
        return render_template('main_contracheque.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles='Remuneração de Membros Inativos', form=form, pagination=pagination)

    return render_template('main_contracheque.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Membros Inativos', form = form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###

@contracheque_bp.route('/contracheque/RemuneracaoServidorAtivo', methods=('GET', 'POST'))
def RemuneracaoServidorAtivo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContraCheque_ServidorAtivo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    #alterar aqui os dados que vão aparecer
    df = df[['Ano', 'Mês','Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
                & (df['Matrícula'].str.contains(request.form['Matricula']) == True)
                & (df['Nome'].str.contains(request.form['Nome']) == True)]
        df = df[['Ano', 'Mês','Matrícula', 'Nome', 'Cargo', 'Lotação', 'Remun. do Cargo Efetivo(1)', 'Outras Verbas Remuneratórias ou Legais/Judiciais (2)', 'Função de Confiança ou Cargo em Comissão (3)', 'Gratif. Natalina (4)', 'Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)', 'Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)', 'Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']]  # dados filtrados
        # alterar main_contracheque
        return render_template('main_contracheque_rsa.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração de Servidores Ativos', form = form, pagination=pagination)

    return render_template('main_contracheque_rsa.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Servidores Ativos', form = form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###


@contracheque_bp.route('/contracheque/RemuneracaoServidorInativo', methods=('GET', 'POST'))
def RemuneracaoServidorInativo():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContraCheque_ServidorInativo.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    #alterar aqui os dados que vão aparecer
    df = df[['Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
                & (df['Matrícula'].str.contains(request.form['Matrícula']) == True)
                & (df['Nome'].str.contains(request.form['Nome']) == True)]
        df = df[['Matrícula', 'Nome', 'Cargo', 'Lotação', 'Remun. do Cargo Efetivo(1)', 'Outras Verbas Remuneratórias ou Legais/Judiciais (2)', 'Função de Confiança ou Cargo em Comissão (3)', 'Gratif. Natalina (4)', 'Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)', 'Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)', 'Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']]  # dados filtrados
        # alterar main_contracheque
        return render_template('main_contracheque.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração de Servidores Inativos', form = form, pagination=pagination)

    return render_template('main_contracheque.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Servidores Inativos', form = form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###


@contracheque_bp.route('/contracheque/RemuneracaoPensionista', methods=('GET', 'POST'))
def RemuneracaoPensionista():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'ContraCheque_Pensionista.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    #alterar aqui os dados que vão aparecer
    df = df[['Matrícula', 'Nome', 'Cargo','Lotação','Remun. do Cargo Efetivo(1)','Outras Verbas Remuneratórias ou Legais/Judiciais (2)','Função de Confiança ou Cargo em Comissão (3)','Gratif. Natalina (4)','Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)','Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)','Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))
                & (df['Matrícula'].str.contains(request.form['Matrícula']) == True)
                & (df['Nome'].str.contains(request.form['Nome']) == True)]
        df = df[['Matrícula', 'Nome', 'Cargo', 'Lotação', 'Remun. do Cargo Efetivo(1)', 'Outras Verbas Remuneratórias ou Legais/Judiciais (2)', 'Função de Confiança ou Cargo em Comissão (3)', 'Gratif. Natalina (4)', 'Férias (1/3 Const.) (5)', 'Abono de Permanência (6)', 'Outras Remunerações Temporárias (7)', 'Verbas Indenizatórias (8)', 'Total de Rend. Brutos (9)', 'Contr. Previdenciária (10)', 'Imposto de Renda (11)', 'Retenção p/ Teto Constitucional (12)', 'Outros Descontos', 'Total de descontos (13)', 'Rend. Líquido Total (14)']]  # dados filtrados
        # alterar main_contracheque
        return render_template('main_contracheque_rp.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração de Pensionistas', form = form, pagination=pagination)

    return render_template('main_contracheque_rp.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Pensionistas', form = form, pagination=pagination)

### -------------------------------------------------------------------------------------------------------------------------------------------------###


@contracheque_bp.route('/contracheque/RemuneracaoColaboradoresAdministracao', methods=('GET', 'POST'))
def RemuneracaoColaboradoresAdministracao():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'RemuneracaoColaboradoresAdministracao.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    df = df[['Ano', 'Mês', 'Empresa Contratada (a)', 'Nº do Contrato (b)', 'Término', 'Nome completo (c) ',
'CPF (d)', 'Cargo / Atividades exercida (e)', 'Unidade Administrativa / Município (f)', 'Salário']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Empresa Contratada (a)', 'Nº do Contrato (b)', 'Término', 'Nome completo (c) ',
'CPF (d)', 'Cargo / Atividades exercida (e)', 'Unidade Administrativa / Município (f)', 'Salário']] #dados filtrados
        return render_template('main_contracheque_cadm.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração de Colaboradores vinculados ao Departamento de Administração', form = form, pagination=pagination)

    return render_template('main_contracheque_cadm.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração de Colaboradores vinculados ao Departamento de Administração', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@contracheque_bp.route('/contracheque/RemuneracaoColaboradoresObrasManutencao', methods=('GET', 'POST'))
def RemuneracaoColaboradoresObrasManutencao():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'RemuneracaoColaboradoresObrasManutencao.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data) #todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    df = df[['Ano', 'Mês', 'Empresa Contratada (a)', 'Nº do Contrato (b)', 'Término',
       'Nome completo (c) ', 'CPF (d)', 'Cargo / Atividade exercida (e)',
       'Unidade Administrativa (f)', 'Salário Bruto (g)']] #dados filtrados
 #Paginação: https://pythonhosted.org/Flask-paginate/ e #https://stackoverflow.com/questions/34952501/flask-pagination-links-improperly-formatted
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')


    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][['Ano', 'Mês', 'Empresa Contratada (a)', 'Nº do Contrato (b)', 'Término',
       'Nome completo (c) ', 'CPF (d)', 'Cargo / Atividade exercida (e)',
       'Unidade Administrativa (f)', 'Salário Bruto (g)']] #dados filtrados
        return render_template('main_contracheque_rcom.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
    titles = 'Remuneração dos Colaboradores Obras e Manutenção', form = form, pagination=pagination)

    return render_template('main_contracheque_rcom.html',tables=df[(page-1)*PER_PAGE:page*PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
      titles = 'Remuneração dos Colaboradores Obras e Manutenção', form = form, pagination=pagination)
### -------------------------------------------------------------------------------------------------------------------------------------------------###

@contracheque_bp.route('/contracheque/VerbasExerciciosAnteriores', methods=('GET', 'POST'))
def VerbasExerciciosAnteriores():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'VerbasExerciciosAnteriores.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    df = df[['Ano', 'Mês', 'Nome do membro /servidor (1)', 'Valor recebido (2)',
       'Objeto do processo', 'Número do processo (3)',
       'Origem do processo administrativo ou judicial (4)']] #dados filtrados
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
            ['Ano', 'Mês', 'Nome do membro /servidor (1)', 'Valor recebido (2)',
       'Objeto do processo', 'Número do processo (3)',
       'Origem do processo administrativo ou judicial (4)']]  # dados filtrados
        return render_template('main_contracheque_vea.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Verbas de Exercicios Anteriores', form=form,
                               pagination=pagination)

    return render_template('main_contracheque_vea.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Verbas de Exercicios Anteriores', form=form,
                           pagination=pagination)

### -----------------------M\u00eas--------------------------------------------------------------------------------------------------------------------------###

@contracheque_bp.route('/contracheque/VerbasExerciciosAnterioresResol_89', methods=('GET', 'POST'))
def VerbasExerciciosAnterioresResol_89():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'VerbasExerciciosAnterioresResol_89.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    df_rcom_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_rcom = df_rcom_Ano_Mes_Max.Ano.max()
    Mes_max_rcom = df_rcom_Ano_Mes_Max.Mês.max()
    df = df[(df['Mês'] == Mes_max_rcom) & (df['Ano'] == Ano_max_rcom)]
    df = df[['Ano', 'Mês', 'Matrícula', 'Nome do membro /servidor (1)', 'Cargo', 'Lotação',
       'Número do processo (1)', 'Objeto do processo (2)', 'Origem do processo administrativo ou judicial (3)',
       'Valor bruto (4)', 'Contribuição Previdenciária (5)', 'Imposto de renda (6)', 'Total de descontos (7)', 'Valor líquido (8)']]  # dados filtrados

    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data)  # todos os dados
        df = df[(df['Mês'] == int(mes)) & (df['Ano'] == int(ano))][
            ['Ano', 'Mês', 'Matrícula', 'Nome do membro /servidor (1)', 'Cargo', 'Lotação',
       'Número do processo (1)', 'Objeto do processo (2)', 'Origem do processo administrativo ou judicial (3)',
       'Valor bruto (4)', 'Contribuição Previdenciária (5)', 'Imposto de renda (6)', 'Total de descontos (7)', 'Valor líquido (8)']]  # dados filtrados
        return render_template('main_contracheque.html',
                               tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                        table_id="myTable2"),
                               titles='Verbas Exercícios Anteriores (a partir de setembro/2019 conforme Res. 200/19 CNMP)', form=form,
                               pagination=pagination)

    return render_template('main_contracheque.html',
                           tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid',
                                                                                    table_id="myTable2"),
                           titles='Verbas Exercícios Anteriores (a partir de setembro/2019 conforme Res. 200/19 CNMP)', form=form,
                           pagination=pagination)