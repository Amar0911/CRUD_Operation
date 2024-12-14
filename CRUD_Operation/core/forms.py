from django import forms
from .models import Crud

class Crudform(forms.ModelForm):

    class Meta:
        model = Crud
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control col-auto'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'})
        }