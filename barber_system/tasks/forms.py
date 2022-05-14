from crispy_forms.bootstrap import PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Button

from django import forms

from .models import Corte


class CorteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'

        helper.layout = Layout(
            Fieldset(
                'Tipo de corte',
                'nome',
                'duracao',
                PrependedText('preco', 'R$'),
            ),
            FormActions(
                Submit('submit', 'Salvar', css_class='save btn btn-default'),
                Button('cancel', 'Cancelar'),
            )
        )

        self.helper = helper

    class Meta:
        model = Corte
        fields = (
            'nome',
            'duracao',
            'preco',
        )
