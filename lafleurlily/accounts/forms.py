from django import forms
from accounts.models import User


class SingUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

