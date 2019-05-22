from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    target = HiddenField('Target', validators=[DataRequired()])
