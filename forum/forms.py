from django.forms import ModelForm
from django import forms
from .models import Room
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'
        
        labels = {
            'topic': _('Tema'),
            'name': _('Nombre'),
            'description': _('Descripción'),
        }

        exclude = ['host']


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']

        labels = {
            'username': 'Nombre de usuario',
            'first_name':'Nombre',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }