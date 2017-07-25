from django import forms
from .models import Post, Comentario


class formComentario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)
