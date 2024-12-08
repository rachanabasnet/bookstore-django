from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'id_name',
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'id_email',
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'message': forms.Textarea(attrs={
                'id': 'id_message',
                'class': 'form-control',
                'placeholder': 'Type your message here',
                'rows': 4,
            }),
        }
