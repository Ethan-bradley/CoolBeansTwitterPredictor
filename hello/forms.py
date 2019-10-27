from django import forms

class SearchForm(forms.Form):
    #search_name = forms.CharField(label='Search user', max_length=100)
    info_text = forms.CharField(max_length=128,help_text='Search User')

