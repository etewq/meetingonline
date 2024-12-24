from django import forms
from .models import DatingProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DatingProfileForm(forms.ModelForm):
    class Meta:
        model = DatingProfile
        fields = ['name', 'bio', 'image', 'date_birth', 'interests']
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
            'interests': forms.CheckboxSelectMultiple(),
        }

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'value': ''})
