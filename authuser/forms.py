from django.contrib.auth.forms import UserCreationForm
from .models import User, Book
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'city',  'name', )


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'subject', )
