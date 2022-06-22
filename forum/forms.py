from django.forms import ModelForm
from .models import Room
from django.utils.translation import gettext_lazy as _

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


