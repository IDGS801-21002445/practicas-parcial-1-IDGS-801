#from wtforms import Form
from wtforms import Form
#from wtforms import StringField, TelField, IntegerField
from wtforms import StringField,TelField,IntegerField
#from wtforms import EmailField
from wtforms import StringField,TelField,IntegerField
#from wtforms.validators import DataRequired, Email
from wtforms.validators import DataRequired,Email



class UserForm(Form):
    nombre = StringField('nombre')
    email = StringField("email")
    apaterno = TelField("apaterno")
    amaterno = StringField('amamterno')
    edad = IntegerField('edad')