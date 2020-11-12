from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text="Required. Add a valid email address", widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',

        }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a username',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))
    membership_no = forms.CharField(max_length=8, min_length=8, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter IEEE membership no. Optional',
    }))

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1',
                  'password2', 'membership_no')

        help_texts = {
            'membership_no': ('Optional!')
        }


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your password',
                                                            }))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Enter your registered Email address'
    }))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid input")
