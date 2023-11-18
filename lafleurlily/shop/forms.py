from django import forms
from shop.models import Reviews


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'review']
