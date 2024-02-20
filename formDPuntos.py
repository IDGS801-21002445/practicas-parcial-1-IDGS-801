#from wtforms import Form
from wtforms import Form
#from wtforms import StringField, TelField, IntegerField
from wtforms import StringField,TelField,IntegerField
#from wtforms import EmailField
from wtforms import StringField,TelField,IntegerField
#from wtforms.validators import DataRequired, Email
from wtforms.validators import DataRequired,Email



class UserForm(Form):
    x1 = StringField("x1")
    x2 = StringField("x2")
    y1 = TelField("y1")
    y2 = StringField('y2')
    d = IntegerField('d')

