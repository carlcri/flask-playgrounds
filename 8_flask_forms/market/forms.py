from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Usuario')
    email_address = StringField(label='Correo electronico')
    password1 = PasswordField(label='Contraseña')
    password2 = PasswordField(label='Confirmar contraseña')
    submit = SubmitField('Registrarse') 
