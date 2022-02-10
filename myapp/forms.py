from unittest.util import _MAX_LENGTH
from django import forms

class emailform(forms.Form):
    fromemail = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)