from wtforms import Form, StringField, IntegerField, TelField, RadioField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SelectField, RadioField
from wtforms import validators

class Resistencias(Form):
    ban1 = SelectField('Banda 1', 
                         choices=[('0', 'Negro'), ('1', 'Cafe'), ('2', 'Rojo'),
                                  ('3', 'Naranja'), ('4', 'Amarillo'), ('5', 'Verde'),
                                  ('6', 'Azul'), ('7', 'Morado'), ('8', 'Gris'),
                                  ('9', 'Blanco')])
    ban2 = SelectField('Banda 2', 
                       choices=[('0', 'Negro'), ('1', 'Cafe'), ('2', 'Rojo'),
                                  ('3', 'Naranja'), ('4', 'Amarillo'), ('5', 'Verde'),
                                  ('6', 'Azul'), ('7', 'Morado'), ('8', 'Gris'),
                                  ('9', 'Blanco')])
    ban3 = SelectField('Banda 3', 
                        choices=[('1', 'Negro'), ('10', 'Cafe'), ('100', 'Rojo'),
                                  ('1000', 'Naranja'), ('10000', 'Amarillo'), ('100000', 'Verde'),
                                  ('1000000', 'Azul'), ('10000000', 'Morado'), ('100000000', 'Gris'),
                                  ('1000000000', 'Blanco')])
    tole = RadioField('Selecciona la tolerancia', choices=[('.1', 'Dorado'), ('.05', 'Plateado')])
class distanciasForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField('y2')
    d = IntegerField('d')

#Sin validaciones
# class UserForm(Form):
#     nombre = StringField('nombre')
#     email = StringField("email")
#     apaterno = TelField("apaterno")
#     amaterno = StringField('amamterno')
#     edad = IntegerField('edad') 

#Con Validaciones  
# class UserForm(Form):
#     nombre = StringField('nombre',[validator.DataRequired(message='El campo es requerido'),
#                                     validator.length(min=4,max=10,message='Ingresa un nombre válido')])
    
#     email = StringField("email",[validator.Email(message='Ingresa un email válido')])

#     apaterno = TelField("apaterno",[validator.DataRequires(message='El campo es requerido'),
#                                     validator.length(min=4,max=10,message='Ingresa un apellido válido')])
    
#     amaterno = StringField('amamterno',[validator.DataRequires(message='El campo es requerido'),
#                                     validator.length(min=4,max=10,message='Ingresa un apellido válido')])
    
#     edad = IntegerField('edad',[validator.DataRequires(message='El campo es requerido'),
#                                     validator.length(min=4,max=10,message='Ingresa un edad válido')]) 
    

class diccionario(Form):
    palabra = StringField("Español", validators = [DataRequired(message="No has escrito la palabra en español"),
        Length(min=4, max=50, message="Ingresa una palabra válida de entre 4 y 50 caracteres")
    ])
                                    
    word = StringField('Inglés',validators = [DataRequired(message="No has escrito la palabra en inglés"),
        Length(min=4, max=50, message="Ingresa una palabra válida de entre 4 y 50 caracteres")
    ])
    idioma = RadioField('Selecciona el lenguaje', choices=[('Espaniol', 'Español'), ('English', 'English')], validators=[
        DataRequired(message="No has escrito la palabra en ingles"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    buscar = StringField("Palabra a buscar", validators=[
        DataRequired(message="No has escrito la palabra a buscar"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
   
class Traductor(Form):
    palabra = StringField("Palabra en español", validators=[
        DataRequired(message="No has escrito la palabra en español"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    word = StringField("Palabra en ingles", validators=[
        DataRequired(message="No has escrito la palabra en ingles"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    buscar = StringField("Palabra a buscar", validators=[
        DataRequired(message="No has escrito la palabra a buscar"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    traductor = RadioField('Selecciona el lenguaje', choices=[('Español', 'Español'), ('Ingles', 'Ingles')], validators=[
        DataRequired(message="No has escrito la palabra en ingles"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    idioma = RadioField('Selecciona el idioma', choices=[('Espaniol', 'Español'), ('English', 'English')])