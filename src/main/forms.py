from django import forms

class FormRepuesto(forms.Form):
    nombre=forms.CharField(label="Nombre del repuesto")
    stock=forms.IntegerField(label="Stock del repuesto")