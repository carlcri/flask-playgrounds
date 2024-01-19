from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from market.models import User
from market import app

class RegisterForm(FlaskForm):
 
    username = StringField(label='usuario' , validators=[DataRequired(), Length(min=4, max=30)])
    email_address = StringField(label='correo electronico', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='contraseña', validators=[DataRequired(), Length(min=5)])
    password2 = PasswordField(label='confirmar contraseña', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Registrarse')
