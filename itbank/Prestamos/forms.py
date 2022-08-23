from django import forms


class Prestamosform(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
