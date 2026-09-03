from django import forms
from django.contrib.auth.models import User

class Contactform(forms.Form):

    name = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(label="Message",required=True)

class register_form(forms.ModelForm):

    username = forms.CharField(label="Username", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Password", required=True)
    password_confirm = forms.CharField(label="Confirm Password", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):

        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password_confirm')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data