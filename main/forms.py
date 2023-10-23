from django.forms import ModelForm
from django import forms
from .models import Offer
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class OfferForm(ModelForm):
    mobile = PhoneNumberField(region="RU")
    class Meta:
        model = Offer
        fields = ['user', 'region', 'city', 'street', 'house', 'mobile', 'date', 'sneakers']