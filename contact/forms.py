# contact/forms.py

from django import forms
from .models import ContactMessage
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control contact-form-textarea', 'placeholder': 'Your Message'}),
        }
