from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'password1', 'password2']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image', 'address', 'dob', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'id_name',
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'rows': 3,
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
