from django import forms


class SampleForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    gender = forms.CharField(label='Gender')
