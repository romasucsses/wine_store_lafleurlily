from django import forms
from orders.models import Checkout


class CheckoutInfoForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make specific fields optional by setting required to False
        self.fields['company_name'].required = False
        self.fields['street_address_2'].required = False
        self.fields['status'].required = False
        self.fields['cart_information'].required = False

