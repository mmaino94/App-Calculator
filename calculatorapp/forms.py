from django import forms
from .models import Formulario2, Formulario1

class Formulario2Form(forms.Form):
    instrumento = forms.CharField(max_length=100, label='Instrumento')
    factor = forms.DecimalField(max_digits=5, decimal_places=2, label='Factor')


class Formulario2Form(forms.ModelForm):
    class Meta:
        model = Formulario2
        fields = ['instrumento', 'factor']

class ConfirmarEliminacionForm(forms.Form):
    confirmacion = forms.BooleanField(
        required=True,
        label='Confirmar la eliminación de este instrumento y factor'
    )


class Formulario2Form(forms.Form):
    moneda = forms.CharField(max_length=100, label='Moneda')
    valor = forms.DecimalField(max_digits=5, decimal_places=2, label='Valor')

class Formulario1Form(forms.ModelForm):
    class Meta:
        model = Formulario1
        fields = ['moneda', 'valor']  # Agrega los campos que corresponden a tu modelo


class InputForm(forms.Form):
    valor_numerico = forms.DecimalField(label='Valor numérico')
    moneda = forms.ModelChoiceField(queryset=Formulario1.objects.all(), empty_label=None, label='Moneda')
    ganancia = forms.DecimalField(label='Ganancia')
    instrumento = forms.ModelChoiceField(queryset=Formulario2.objects.all(), empty_label=None, label='Tipo de instrumento')