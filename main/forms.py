from django import forms
from .models import CV

class CVform(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('cv')