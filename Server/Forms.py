from wtforms import Form
from wtforms import StringField, TextField, PasswordField, IntegerField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class AñadirEmpleadoForm(Form):
    Name = StringField('Nombre: ', [validators.required(message = "Debe ingresar un Nombre")])
    Surname = StringField('Apellido: ', [validators.required(message = "Debe ingresar un Apellido")])
    Email = EmailField('Email: ', [validators.email(message='Ingresa un email valido'),
                                        validators.required(message= 'Se necesita ingresa un email')])
    
    PhoneNumber = StringField('Numero Movil: ', [validators.required('Se necesita ingresar un telefono'),
                                                validators.length(min=10,max=11, message='Ingrese un telefono valido que comience con +54 y prosiga con los 8 digitos de su telefono')])
    
    Address = StringField('Calle: ', [validators.required(message = "Debe ingresar una dirección")])
    ZipCode = StringField('Numero Postal: ', [validators.required(message = "Debe ingresar un codigo postal")])
    Position = StringField('Posición: ', [validators.required(message = "Debe ingresar una posición")])


class LoginForm(Form):
    username = StringField('Username', [validators.length(min=4, max=30, message='Ingrese un username mas largo o mas corto' ), 
                                        validators.required(message = "El username es requerido")])

    passw = PasswordField('Contraseña',[validators.required(message= 'Se necesita una contraseña')])


class CrearAdminForm(Form):
    username = StringField('Username', [validators.length(min=4, max=30, message='Ingrese un username mas largo o mas corto' ), 
                                        validators.required(message = "El username es requerido")])

    passw = PasswordField('Contraseña',[validators.required(message= 'Se necesita una contraseña')])
