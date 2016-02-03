from django.forms import ModelForm, PasswordInput, forms
from django.contrib.auth.models import User
from gestion_personal.models import Personal
from django.db import models
from datetimewidget.widgets import DateWidget
import re

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password':PasswordInput(),
        }

class AltaPersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['foto','nombre','apellidos','dni','f_nacimiento','sexo',
                  'direccion','localidad', 'cod_postal', 'telefono','num_seg_social']

        dateOptions = {
            'startView' : 4, # Para que empieze por el año
        }
        widgets = {
            'f_nacimiento': DateWidget(options = dateOptions, bootstrap_version=3),
        }

    def clean(self):
        cd = self.cleaned_data

        if not re.match('^\d{8}[A-Za-z]$' , cd.get('dni')):
            raise forms.ValidationError('Formato DNI: XXXXXXXXL')

        if not re.match('^\d{12}$' , cd.get('num_seg_social')):
            raise forms.ValidationError('Formato Número seguridad social: XXXXXXXXXXXX')

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')

#El usuario y la contraseña solo los puede cambiar el administrador.
class ModificarPersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['foto','nombre','apellidos','f_nacimiento','sexo',
                  'direccion','localidad', 'cod_postal', 'telefono']

        dateOptions = {
            'startView' : 4, # Para que empieze por el año
        }
        widgets = {
            'f_nacimiento': DateWidget(options = dateOptions, bootstrap_version=3),
        }

    def clean(self):
        cd = self.cleaned_data

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')
