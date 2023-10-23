from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()
class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        help_text="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control', 'placeholder': '"Электронная почта'}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control', 'placeholder': 'Password'}),
        help_text='',
    )
    password2 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))
