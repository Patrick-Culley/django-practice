from django import forms

class searchForm(forms.Form): 
    ticker = forms.CharField(label='ticker', max_length=4)