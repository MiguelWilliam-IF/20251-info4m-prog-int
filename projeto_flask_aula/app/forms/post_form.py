from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = StringField('Postagem', validators=[DataRequired(message="Por favor, preencha o texto do post.")])
    submit = SubmitField('Salvar')