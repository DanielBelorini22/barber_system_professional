from django import forms

from .models import Corte


class CorteForm(forms.ModelForm):
    class Meta:
        model = Corte
        fields = (
            'nome',
            'duracao',
            'preco',
        )
