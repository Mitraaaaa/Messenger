from django import forms

class upload_file (forms.forms) :
    title = forms.CharField()
    file = forms.FileField()
    