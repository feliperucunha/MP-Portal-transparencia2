from flask import Blueprint, json, render_template, request
import os
import numpy as np
from forms import ConsultaAnoMes
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
from flask_paginate import Pagination, get_page_parameter

SIC_bp = Blueprint('SIC', __name__)

@SIC_bp.route('/SIC/UnidadeAutoridadeResponsável', methods=('GET', 'POST'))

def UnidadeAutoridadeResponsável():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json_files', 'Ouvidoria.json')
    json_data = json.load(open(json_url))
    df = pd.DataFrame(json_data)  # todos os dados
    # Renomear o nome das colunas
    df = df.rename(columns={'0': 'Id', '1': 'Data Cadastro', '2': 'Mês', '3': 'Ano', '4': 'Objetivo', '5': 'Assunto',
                            '6': 'Origem', '7': 'Status', '8': 'Municipio', '9': 'Sexo', '10': 'Escolaridade'})

    df_ovi_Ano_Mes_Max = df[df['Ano'] == df.Ano.max()]
    Ano_max_ovi = df_ovi_Ano_Mes_Max.Ano.max()
    Mes_max_ovi = df_ovi_Ano_Mes_Max.Mês.max()
    # ----------Criar grafico-------------------------------------------------#
    # https: // www.chartjs.org / docs / latest /
    # df1 = df[(df['Mês'] == Mes_max_ovi) & (df['Ano'] == Ano_max_ovi)]


    # --- Fim---#

    df = df[(df['Mês'] == Mes_max_ovi) & (df['Ano'] == Ano_max_ovi)][
        ['Ano','Mês', 'Objetivo', 'Assunto', 'Origem', 'Status', 'Municipio', 'Sexo', 'Escolaridade']]  # dados filtrados
    # ----------inicio dos dados dos graficos-------------------------------------------------#
    # https: // www.chartjs.org / docs / latest /          # site com inoformações de criação dos graficos
    # Categoria
    objetivo = df.Objetivo.value_counts().reset_index()
    objetivo = objetivo.rename(columns={'index': 'Objetivo', 'Objetivo': 'Quantidade'})
    categoria = objetivo['Objetivo']
    cat_quantidade = objetivo['Quantidade']
    lista_categoria = categoria.values.tolist()
    lista_cat_quantidade = cat_quantidade.values.tolist()
    # Origem
    origem = df['Origem'].value_counts().reset_index()
    origem = origem.rename(columns={'index': 'Origem', 'Origem': 'Quantidade'})
    nom_origem = origem['Origem']
    ori_quantidade = origem['Quantidade'].astype(int)
    lista_origem = nom_origem.values.tolist()
    lista_ori_quantidade = ori_quantidade.values.tolist()
    # status
    status = df['Status'].value_counts().reset_index()
    status = status.rename(columns={'index': 'Status', 'Status': 'Quantidade'})
    nom_status = status['Status']
    sta_quantidade = status['Quantidade'].astype(int)
    lista_status = nom_status.values.tolist()
    lista_sta_quantidade = sta_quantidade.values.tolist()
    # Assunto
    assunto = df['Assunto'].value_counts().reset_index()
    assunto = assunto.rename(columns={'index': 'Assunto', 'Assunto': 'Quantidade'})
    nom_assunto = assunto['Assunto']
    ass_quantidade = assunto['Quantidade']
    lista_assunto = nom_assunto.values.tolist()
    lista_ass_quantidade = ass_quantidade.values.tolist()
    # Municipio
    municipio = df['Municipio'].value_counts().reset_index()
    municipio = municipio.rename(columns={'index': 'Municipio', 'Municipio': 'Quantidade'})
    nom_municipio = municipio['Municipio']
    mun_quantidade = municipio['Quantidade']
    lista_municipio = nom_municipio.values.tolist()
    lista_mun_quantidade = mun_quantidade.values.tolist()
    # Sexo
    sexo = df['Sexo'].value_counts().reset_index()
    sexo = sexo.rename(columns={'index': 'Sexo', 'Sexo': 'Quantidade'})
    tipo_sexo = sexo['Sexo']
    sex_quantidade = sexo['Quantidade'].astype(int)
    lista_sexo = tipo_sexo.values.tolist()
    lista_sex_quantidade = sex_quantidade.values.tolist()
    # Escolaridade
    escolaridade = df['Escolaridade'].value_counts().reset_index()
    escolaridade = escolaridade.rename(columns={'index': 'Escolaridade', 'Escolaridade': 'Quantidade'})
    nom_escolaridade = escolaridade['Escolaridade']
    esc_quantidade = escolaridade['Quantidade'].astype(int)
    lista_escolaridade = nom_escolaridade.values.tolist()
    lista_esc_quantidade = esc_quantidade.values.tolist()
    # Mês
    meses = df_ovi_Ano_Mes_Max['Mês'].value_counts().reset_index().set_index(['index']).sort_index()
    mes_quantidade = meses['Mês'].astype(int)
    lista_mes_quantidade = mes_quantidade.values.tolist()
    # ----------Fim dos dados dos graficos-------------------------------------------------#
    page = request.args.get(get_page_parameter(), type=int, default=1)
    PER_PAGE = 5
    pagination = Pagination(bs_version=4, page=page, per_page=PER_PAGE, total=len(df), record_name='df')

    form = ConsultaAnoMes()

    if form.validate_on_submit():
        mes = form.mes.data
        ano = form.ano.data
        df = pd.DataFrame(json_data) #todos os dados
        df = df.rename(columns={'0': 'Id', '1': 'Data Cadastro', '2': 'Mês', '3': 'Ano', '4': 'Objetivo', '5': 'Assunto','6': 'Origem', '7': 'Status', '8': 'Municipio', '9': 'Sexo', '10': 'Escolaridade'})
        df = df[(df['Mês'] == int(mes)) & (df['Ano']==int(ano))][['Ano','Mês', 'Objetivo', 'Assunto', 'Origem', 'Status', 'Municipio', 'Sexo', 'Escolaridade']]  # dados filtrados
        # ----------inicio dos dados dos graficos-------------------------------------------------#
        # Categoria
        objetivo = df.Objetivo.value_counts().reset_index()
        objetivo = objetivo.rename(columns={'index': 'Objetivo', 'Objetivo': 'Quantidade'})
        categoria = objetivo['Objetivo']
        cat_quantidade = objetivo['Quantidade']
        lista_categoria = categoria.values.tolist()
        lista_cat_quantidade = cat_quantidade.values.tolist()
        # Origem
        origem = df['Origem'].value_counts().reset_index()
        origem = origem.rename(columns={'index': 'Origem', 'Origem': 'Quantidade'})
        nom_origem = origem['Origem']
        ori_quantidade = origem['Quantidade'].astype(int)
        lista_origem = nom_origem.values.tolist()
        lista_ori_quantidade = ori_quantidade.values.tolist()
        # status
        status = df['Status'].value_counts().reset_index()
        status = status.rename(columns={'index': 'Status', 'Status': 'Quantidade'})
        nom_status = status['Status']
        sta_quantidade = status['Quantidade'].astype(int)
        lista_status = nom_status.values.tolist()
        lista_sta_quantidade = sta_quantidade.values.tolist()
        # Assunto
        assunto = df['Assunto'].value_counts().reset_index()
        assunto = assunto.rename(columns={'index': 'Assunto', 'Assunto': 'Quantidade'})
        nom_assunto = assunto['Assunto']
        ass_quantidade = assunto['Quantidade']
        lista_assunto = nom_assunto.values.tolist()
        lista_ass_quantidade = ass_quantidade.values.tolist()
        # Municipio
        municipio = df['Municipio'].value_counts().reset_index()
        municipio = municipio.rename(columns={'index': 'Municipio', 'Municipio': 'Quantidade'})
        nom_municipio = municipio['Municipio']
        mun_quantidade = municipio['Quantidade']
        lista_municipio = nom_municipio.values.tolist()
        lista_mun_quantidade = mun_quantidade.values.tolist()
        # Sexo
        sexo = df['Sexo'].value_counts().reset_index()
        sexo = sexo.rename(columns={'index': 'Sexo', 'Sexo': 'Quantidade'})
        tipo_sexo = sexo['Sexo']
        sex_quantidade = sexo['Quantidade'].astype(int)
        lista_sexo = tipo_sexo.values.tolist()
        lista_sex_quantidade = sex_quantidade.values.tolist()
        # Escolaridade
        escolaridade = df['Escolaridade'].value_counts().reset_index()
        escolaridade = escolaridade.rename(columns={'index': 'Escolaridade', 'Escolaridade': 'Quantidade'})
        nom_escolaridade = escolaridade['Escolaridade']
        esc_quantidade = escolaridade['Quantidade'].astype(int)
        lista_escolaridade = nom_escolaridade.values.tolist()
        lista_esc_quantidade = esc_quantidade.values.tolist()
        # ----------Fim dos dados dos graficos-------------------------------------------------#
        return render_template('main_SIC_uar.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
                               titles='Ouvidoria do Ministério Público do Estado do Pará', form=form,
                               pagination=pagination, ano=Ano_max_ovi, lista_categoria=lista_categoria,
                               lista_cat_quantidade=lista_cat_quantidade, lista_assunto=lista_assunto, lista_ass_quantidade=lista_ass_quantidade,
                               lista_municipio=lista_municipio, lista_mun_quantidade=lista_mun_quantidade, municipio=municipio,
                               lista_status=lista_status, lista_sta_quantidade=lista_sta_quantidade, lista_origem=lista_origem,
                               lista_ori_quantidade=lista_ori_quantidade, lista_sexo=lista_sexo, lista_sex_quantidade=lista_sex_quantidade,
                               lista_escolaridade=lista_escolaridade, lista_esc_quantidade=lista_esc_quantidade,
                               lista_mes_quantidade=lista_mes_quantidade)

    return render_template('main_SIC_uar.html', tables=df[(page - 1) * PER_PAGE:page * PER_PAGE].to_html(classes='table table-fluid', table_id="myTable2"),
                           titles='Ouvidoria do Ministério Público do Estado do Pará', form=form, pagination=pagination, ano=Ano_max_ovi,
                           lista_categoria=lista_categoria, lista_cat_quantidade=lista_cat_quantidade, lista_assunto=lista_assunto, lista_ass_quantidade=lista_ass_quantidade,
                           lista_municipio=lista_municipio, lista_mun_quantidade=lista_mun_quantidade, municipio=municipio,
                           lista_status=lista_status, lista_sta_quantidade=lista_sta_quantidade, lista_origem=lista_origem,
                           lista_ori_quantidade=lista_ori_quantidade, lista_sexo=lista_sexo, lista_sex_quantidade=lista_sex_quantidade,
                           lista_escolaridade=lista_escolaridade, lista_esc_quantidade=lista_esc_quantidade,
                           lista_mes_quantidade=lista_mes_quantidade)


### -------------------------------------------------------------------------------------------------------------------------------------------------

@SIC_bp.route('/SIC/Ouvidoria', methods=('GET', 'POST'))
def Ouvidoria():
        return render_template('main_SIC.html',titles = 'SIC')
### -------------------------------------------------------------------------------------------------------------------------------------------------###
