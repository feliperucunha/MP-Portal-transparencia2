from flask import Blueprint, json, render_template, request

menu_bp = Blueprint('menu', __name__)


@menu_bp.route('/menu/legislacao', methods=('GET', 'POST'))
def legislacao():
    return render_template('menu_legislacao.html')

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@menu_bp.route('/menu/manual_portal', methods=('GET', 'POST'))
def manual_portal():
    return render_template('menu_manual_portal.html')

### -------------------------------------------------------------------------------------------------------------------------------------------------###
@menu_bp.route('/menu/perguntasfrequentes', methods=('GET', 'POST'))
def perguntasfrequentes():
    return render_template('menu_duvidas_frequentes.html')
