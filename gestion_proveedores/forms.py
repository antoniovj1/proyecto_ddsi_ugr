from django.forms import ModelForm,forms
import re
from gestion_proveedores.models import Proveedor

class AltaProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['foto','nombre','email','telefono','fax','pais',
                  'direccion','localidad', 'cod_postal', 'descripcion']

    def clean(self):
        cd = self.cleaned_data

        if not re.match('^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$' , cd.get('email')):
            raise forms.ValidationError('Formato email: abcd@abcd.abcd')

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')

class ModificarProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['foto','nombre','email','telefono','fax','pais',
                  'direccion','localidad', 'cod_postal', 'descripcion']
    def clean(self):
        cd = self.cleaned_data

        if not re.match('^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$' , cd.get('email')):
            raise forms.ValidationError('Formato email: abcd@abcd.abcd')

        if not re.match('^\d{5}$', cd.get('cod_postal')):
            raise forms.ValidationError('Formato Código postal: 12345')

        if not re.match('^([+]\d{2})?\d{9}$', cd.get('telefono')):
            raise forms.ValidationError('Formato teléfono: [+XX]123456789')
