from django import forms
from .models import Book, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# forma dodawania książki
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'status']   #pola formularza
        labels = {
            'title': 'Tytuł',
            'author': 'Autor',
            'description': 'Opis',
            'status': 'Status',
        }

# forma dodawania recenzji
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']  # pola formularza
        labels = {
            'review_text': 'Treść recenzji',
            'rating': 'Ocena',
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Napisz swoją recenzję...'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 11)], attrs={
                'placeholder': 'Oceń od 1 do 10'
            })
        }

#formularz logowania
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']