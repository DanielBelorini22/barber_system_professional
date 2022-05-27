from crispy_forms.bootstrap import PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Button, Field

from django import forms
from django.contrib.auth.models import User

from .models import TipoCorte, Corte


class TipoCorteForm(forms.ModelForm):
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
                PrependedText('desconto', '%'),
                'ativo',
            ),
            FormActions(
                Submit('submit', 'Salvar', css_class='save btn btn-success'),
                Button('cancel', 'Cancelar', css_class='cancel btn btn-danger',
                       onclick="javascript:history.back()"),
            )
        )

        self.helper = helper

    class Meta:
        model = TipoCorte
        fields = (
            'nome',
            'duracao',
            'preco',
            'desconto',
            'ativo',
        )


class CorteForm(forms.ModelForm):
    tipo_corte = forms.ModelChoiceField(TipoCorte.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'

        helper.layout = Layout(
            Fieldset(
                'Corte',
                'cliente',
                Field('horario', autocomplete="off"),
                'tipo_corte',
                'observacao',
                'status',
            ),
            FormActions(
                Submit('submit', 'Salvar', css_class='save btn btn-success'),
                Button('cancel', 'Cancelar', css_class='cancel btn btn-danger',
                       onclick="javascript:history.back()"),
            )
        )

        self.helper = helper
        self.fields['cliente'].queryset = User.objects.filter(username__endswith='o')

    class Meta:
        model = Corte
        fields = (
            'cliente',
            'horario',
            'tipo_corte',
            'observacao',
            'status',
        )
