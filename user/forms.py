from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User, Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'l_name', 'name']

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    widgets = {
            'email': forms.TextInput(attrs={'class': 'container-form'}),
            'password': forms.TextInput(attrs={'class': 'container-form'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'l_name']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']