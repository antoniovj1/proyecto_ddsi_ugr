import re

from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, forms

from gestion_clientes.models import Cliente, Revision


class AltaClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['foto', 'nombre', 'apellidos', 'dni', 'f_nacimiento', 'sexo',
                  'direccion', 'localidad', 'cod_postal', 'telefono']

        dateOptions = {
            'startView': 4,  # Para que empieze por el año
        }
        widgets = {
            'f_nacimiento': DateWidget(options=dateOptions, bootstrap_version=3),
        }

    def clean(self):
        cd = self.cleaned_data

        if not re.match('^\d{8}[A-Za-z]$', cd.get('dni')):
            raise forms.ValidationError('Formato DNI: XXXXXXXXL')

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')


class ModificarClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['foto', 'nombre', 'apellidos', 'f_nacimiento', 'sexo',
                  'direccion', 'localidad', 'cod_postal', 'telefono']

        dateOptions = {
            'startView': 4,  # Para que empieze por el año
        }
        widgets = {
            'f_nacimiento': DateWidget(options=dateOptions, bootstrap_version=3),
        }

    def clean(self):
        cd = self.cleaned_data

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')


class RevisionForm(ModelForm):
    class Meta:
        model = Revision
        fields = ['fecha', 'oculista', 'descripcion', 'diagnostico', 'plan']

        dateOptions = {
            'startView': 4,  # Para que empieze por el año
        }

        widgets = {
            'fecha': DateWidget(options=dateOptions, bootstrap_version=3),
        }
