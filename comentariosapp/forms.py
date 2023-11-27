from .models import Comentario
from django import forms

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'correo', 'comentario']