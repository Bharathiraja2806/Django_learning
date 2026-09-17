from dataclasses import fields

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Categories, Post

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

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

    def clean(self):

        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")

class ForgotPasswordForm(forms.Form):

    email = forms.EmailField(label="Email", required=True)

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address.")

class ResetPasswordForm(forms.Form):

    new_password = forms.CharField(max_length=100, required=True)
    confirm_password = forms.CharField(max_length=100, required=True)

    def clean(self):

        cleaned_data  = super().clean()

        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:

            raise forms.ValidationError("Password doesnot match!")

class PostForm(forms.ModelForm):

    title = forms.CharField(label="Title", max_length=200, required=True)
    content = forms.CharField(label="Content", required=True)
    category = forms.ModelChoiceField(label="Category", required=True, queryset=Categories.objects.all())
    image_url = forms.ImageField(label="Image Upload", required=False)

    class Meta:

        model = Post
        fields = ["title", "content", "category", "image_url"]

    def clean(self):

        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")

        if content and len(content) < 10:
            raise forms.ValidationError("Title must be at least 10 characters long.")

    def save(self, commit = ...):

        post = super().save(commit)
        cleaned_data = super().clean()

        if cleaned_data.get('image_url'):
            post.image_url = cleaned_data.get('image_url')
        else:
            img_url = "https://st4.depositphotos.com/14953852/22772/v/450/depositphotos_227724992-stock-illustration-image-available-icon-flat-vector.jpg"

            post.image_url = img_url

        if commit:
            post.save()
        return post