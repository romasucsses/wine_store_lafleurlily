from django import forms
from accounts.models import User
from orders.models import CheckoutAddress


class SingUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class AddCheckoutAddressForm(forms.ModelForm):
    class Meta:
        model = CheckoutAddress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make specific fields optional by setting required to False
        self.fields['company_name'].required = False
        self.fields['street_address_2'].required = False


class UpdateUserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'last_name', 'username', 'email']

