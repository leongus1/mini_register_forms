from django import forms
from login_app.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    
class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)