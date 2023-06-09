from . models import Crud
from django import forms


class CrudForm(forms.ModelForm):
    class Meta:
        model=Crud
        fields=['Slno','Itemname','Description']