from django import forms
from pages.models import EmailSubscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']
