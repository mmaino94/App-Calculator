from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario1, Formulario2
from .forms import Formulario2Form, Formulario1Form
from django import forms

def tabla_formulario1(request):
    monedas = Formulario1.objects.all()

    if request.method == 'POST':
        form = Formulario1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_formulario1')
    else:
        form = Formulario1Form()

    return render(request, 'tabla_formulario1.html', {'monedas': monedas, 'form': form})


def tabla_formulario2(request):
    instrumentos = Formulario2.objects.all()
  

    # Si se envió el formulario de edición, procesarlo y guardar los cambios
    if request.method == 'POST':
        form = Formulario2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_formulario2')
    else:
        form = Formulario2Form()

    # Si se solicita la eliminación, borrar el registro
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        Formulario2.objects.filter(pk=delete_id).delete()
        return redirect('tabla_formulario2')

    return render(request, 'tabla_formulario2.html', {'instrumentos': instrumentos, 'form': form})

def agregar_instrumento_factor(request):
    if request.method == 'POST':
        form = Formulario2Form(request.POST)
        if form.is_valid():
            instrumento = form.cleaned_data['instrumento']
            factor = form.cleaned_data['factor']

            # Guardar el nuevo instrumento y factor en la base de datos
            Formulario2.objects.create(instrumento=instrumento, factor=factor)

            return redirect('tabla_formulario2')
    else:
        form = Formulario2Form()

    return render(request, 'agregar_instrumento_factor.html', {'form': form})


class InputForm(forms.Form):
    valor_numerico = forms.DecimalField(label='Valor numérico')
    moneda = forms.ModelChoiceField(queryset=Formulario1.objects.all(), empty_label=None, label='Moneda')
    ganancia = forms.DecimalField(label='Ganancia')
    instrumento = forms.ModelChoiceField(queryset=Formulario2.objects.all(), empty_label=None, label='Tipo de instrumento')


def calculadora(request):
    

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            valor_numerico = form.cleaned_data['valor_numerico']
            moneda = form.cleaned_data['moneda']
            ganancia = form.cleaned_data['ganancia']
            instrumento = form.cleaned_data['instrumento']
            

            # Obtener el factor del instrumento seleccionado desde la base de datos
            factor = instrumento.factor

            # Realizar el cálculo utilizando el valor de la moneda seleccionada
            resultado = round(((moneda.valor * valor_numerico * factor) / ganancia),2)

            return render(request, 'resultado.html', {'resultado': resultado})
    else:
        form = InputForm()

    return render(request, 'calculadora.html', {'form': form})

def editar_instrumento_factor(request, pk):
    instrumento = get_object_or_404(Formulario2, pk=pk)

    if request.method == 'POST':
        form = Formulario2Form(request.POST, instance=instrumento)
        if form.is_valid():
            form.save()
            return redirect('tabla_formulario2')
    else:
        form = Formulario2Form(instance=instrumento)

    return render(request, 'editar_instrumento_factor.html', {'form': form})

def eliminar_instrumento_factor(request, pk):
    instrumento = get_object_or_404(Formulario2, pk=pk)

    if request.method == 'POST':
        instrumento.delete()
        return redirect('tabla_formulario2')

    return render(request, 'eliminar_instrumento_factor.html', {'instrumento': instrumento})

