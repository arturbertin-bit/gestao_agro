from django import forms
from .models import Area


class AreasForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["nome", "tamanho"]
