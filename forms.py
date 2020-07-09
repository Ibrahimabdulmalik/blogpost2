
from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    Email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    