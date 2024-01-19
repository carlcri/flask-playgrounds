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


    def validate_username(self, username_to_validate):
        print(username_to_validate)
#        print(type(username_to_validate))
#        print(username_to_validate.data)
        with app.app_context():
            consulta = User.query.filter_by(username=username_to_validate.data).first()
        if consulta is not None:
            raise ValidationError(f'Usuario: {consulta} ya existe, intente nuevamente') 
        
    
    def validate_email_address(self, email_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(email_address=email_to_validate.data).first().email_address
            if consulta is not None:
                raise ValidationError(f'correo {consulta}: ya existe, intento otro correo')
        

