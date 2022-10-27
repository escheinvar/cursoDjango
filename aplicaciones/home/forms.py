#from socket import fromshare
from django import forms

from .models import MyBase

class MyForma(forms.ModelForm):

    class Meta:
        model = MyBase
        fields = ('__all__')
    
    def clean_cantidad(self):
        MyCant = self.cleaned_data['cantidad']
        if MyCant < 10:
            raise forms.ValidationError('Error: ingresa un valor mayor a 10')
        return MyCant