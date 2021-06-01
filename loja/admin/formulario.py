from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome completo:', [validators.Length(min=4, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('Ensira uma senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Sua senha nao sao iguais')
    ])
    confirm = PasswordField('Repita a senha novamente')

class LoginFormulario(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [ validators.DataRequired()])

         
   
   

