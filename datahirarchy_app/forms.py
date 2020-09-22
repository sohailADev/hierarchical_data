from django import forms
from . import models
from mptt.forms import TreeNodeChoiceField
class FolderForm(forms.ModelForm):
    parent = TreeNodeChoiceField
    class Meta:
       
        fields = ['name','parent']

class LoginForm(forms.Form):
        username = forms.CharField(max_length=20)
        password = forms.CharField(widget=forms.PasswordInput())

   
    
        