from django import forms
from django.forms import ModelForm

class searchForm(forms.Form): 
    ticker = forms.CharField(label='ticker', max_length=4)
 