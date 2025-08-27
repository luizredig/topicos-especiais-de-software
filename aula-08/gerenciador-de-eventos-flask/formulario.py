# pip install flask_wtf, wtforms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length

class FormularioCriarconta(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha: ', validators=[Length(6, 20)])
    submit = SubmitField('Registrar')

class FormularioEvento(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    data = DateField("Data: ", format='%Y-%m-%d', validators=[DataRequired()])
    descricao = TextAreaField("Descricao:")
    submit = SubmitField("Salvar")

