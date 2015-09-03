from django import forms


class Search(forms.form):
    search = forms.CharField(max_length=50)
