from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet

# ModelForm for Tweet - auto-generates form fields from the Tweet model
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # Only expose text and photo fields to the user (user is set via request)
        fields = ['text', 'photo']

# Form for User Registration - based on Django's built-in UserCreationForm
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
