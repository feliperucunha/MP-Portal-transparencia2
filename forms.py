#https://pythonspot.com/flask-web-forms/
#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import SelectField, SubmitField, StringField, validators
from wtforms.validators import DataRequired
#from wtforms import StringField, TextAreaField, SubmitField
#from wtforms.validators import Email, InputRequired


class ConsultaAnoMes(FlaskForm):
    mes = SelectField('Selecione o Mês', validators=[DataRequired()],
                        choices=[('1', 'Janeiro'),
                                 ('2', 'Fevereiro'),
                                 ('3', 'Março'),
                                 ('4', 'Abril'),
                                 ('5', 'Maio'),
                                 ('6', 'Junho'),
                                 ('7', 'Julho'),
                                 ('8', 'Agosto'),
                                 ('9', 'Setembro'),
                                 ('10', 'Outubro'),
                                 ('11', 'Novembro'),
                                 ('12', 'Dezembro')])
    ano = SelectField('Selecione o Ano', validators=[DataRequired()],
                        choices=[('2020', '2020'),
                                 ('2019', '2019'),
                                 ('2018', '2018'),
                                 ('2017', '2017'),
                                 ('2016', '2016'),
                                 ('2015', '2015')])
    submit = SubmitField('Buscar')

class ConsultaAno(FlaskForm):
    ano = SelectField('Selecione o Ano', validators=[DataRequired()],
                        choices=[('2020', '2020'),
                                 ('2019', '2019'),
                                 ('2018', '2018'),
                                 ('2017', '2017'),
                                 ('2016', '2016'),
                                 ('2015', '2015')])
    submit = SubmitField('Buscar')

class ConsultaAnoMesDesp(FlaskForm):
    mes = SelectField('Selecione o Mês', validators=[DataRequired()],
                        choices=[('1', 'Janeiro'),
                                 ('2', 'Fevereiro'),
                                 ('3', 'Março'),
                                 ('4', 'Abril'),
                                 ('5', 'Maio'),
                                 ('6', 'Junho'),
                                 ('7', 'Julho'),
                                 ('8', 'Agosto'),
                                 ('9', 'Setembro'),
                                 ('10', 'Outubro'),
                                 ('11', 'Novembro'),
                                 ('12', 'Dezembro')])
    ano = SelectField('Selecione o Ano', validators=[DataRequired()],
                        choices=[('2020', '2020'),
                                 ('2019', '2019'),
                                 ('2018', '2018'),
                                 ('2017', '2017'),
                                 ('2016', '2016'),
                                 ('2015', '2015')])
    tdespesa = StringField('Tipo de Despesa', validators=[DataRequired()], id="tipodespesa", render_kw={"placeholder": "Tipo de despesa"})
    submit = SubmitField('Buscar')

class ConsultaAnoMesAcao(FlaskForm):
    mes = SelectField('Selecione o Mês', validators=[DataRequired()],
                        choices=[('1', 'Janeiro'),
                                 ('2', 'Fevereiro'),
                                 ('3', 'Março'),
                                 ('4', 'Abril'),
                                 ('5', 'Maio'),
                                 ('6', 'Junho'),
                                 ('7', 'Julho'),
                                 ('8', 'Agosto'),
                                 ('9', 'Setembro'),
                                 ('10', 'Outubro'),
                                 ('11', 'Novembro'),
                                 ('12', 'Dezembro')])
    ano = SelectField('Selecione o Ano', validators=[DataRequired()],
                        choices=[('2020', '2020'),
                                 ('2019', '2019'),
                                 ('2018', '2018'),
                                 ('2017', '2017'),
                                 ('2016', '2016'),
                                 ('2015', '2015')])
    tacao = StringField('Descrição da Ação (a)', validators=[DataRequired()], id="tipoacao", render_kw={"placeholder": "Tipo de ação"})
    submit = SubmitField('Buscar')