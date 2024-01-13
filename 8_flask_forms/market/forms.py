from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='usuario')
    email_address = StringField(label='correo electronico')
    password1 = PasswordField(label='contraseña')
    password2 = PasswordField(label='confirmar contraseña')
    submit = SubmitField('Registrarse') 
