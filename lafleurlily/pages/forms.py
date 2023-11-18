from django import forms
from pages.models import EmailSubscription, ContactUs


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']


class SendMSGForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
